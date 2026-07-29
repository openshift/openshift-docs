#!/usr/bin/env python3
"""
CSV to DITAMAP converter.
Parses a hierarchical CSV file where each row has one non-empty column,
and the position of that column indicates the hierarchical level.
"""

MIN_CHUNKED_LEVEL = 4 # entries on this level or below will be chunked to the topic above them
MAX_SUBMAP_LEVEL = 1 # entries on this level or above become submaps if is_job==True

import csv
import logging
import re
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional
import os.path
import sys
import argparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

# Track which files have been written to in this execution
_written_files = set()

# Output directory for generated files (None = current directory)
_output_dir = None

def output_pathname(filename: str) -> str:
    """Return the filesystem path for an output file, respecting --output-dir."""
    if _output_dir:
        return os.path.join(_output_dir, os.path.basename(filename))
    return filename

def title_to_basename(title: str) -> str:
    """
    Convert a title to a valid basename for a file.

    Args:
        title: The title text to convert

    Returns:
        A valid file basename

    Examples:
        "3.5.1.1. Managing cluster components" -> "managing-cluster-components"
        "Introduction to OpenShift" -> "introduction-to-openshift"
        "Chapter 1. Getting Started" -> "getting-started"
        "CHAPTER 3.5.2 Installation" -> "installation"
    """
    # Remove "chapter" (case-insensitive) at the start
    text = re.sub(r'^chapter\s*', '', title, flags=re.IGNORECASE)

    # Remove leading and trailing spaces
    text = text.strip()

    # Remove leading numbers with dots (e.g., "3.5.1.1." or "2.1.")
    text = re.sub(r'^\d+(\.\d+)*\.?\s*', '', text)

    # Strip and lowercase
    text = text.strip().lower()

    # Remove any remaining punctuation except spaces
    text = re.sub(r'[^\w\s]', '', text)

    # Replace multiple spaces with single dash
    text = re.sub(r'\s+', '-', text)

    return text



class Column:
    """Represents a non-empty column."""
    def __init__(self, idx: int, text: str):
        self.idx = idx
        self.text = text

    def __repr__(self):
        return f"Column {self.idx}: {self.text}"


class CSVEntry:
    """Represents a single entry from the CSV with its hierarchical level and text.
        Exception: categories get their own entries though can be on the same line"""

    def __init__(self, level: int, line_number: int, filename:str = None, is_job:bool = False, navtitle:str = ''):
        self.level = level
        self.line_number = line_number
        self.filename=filename
        self.is_job=is_job
        self.navtitle = navtitle.strip()
        # collapse extra spaces
        while ("  " in self.navtitle): 
            self.navtitle = self.navtitle.replace("  "," ")

    def __repr__(self):
        return f"CSVEntry(level={self.level}, line={self.line_number}, filename={self.filename}, is_job={self.is_job}, navtitle={self.navtitle})"

# helper to read a column of a row safely
def get_column(row, index):
    if len(row) > index:
        return row[index].strip()
    return ''

def parse_csv(filepath: str) -> List[CSVEntry]:
    """
    Parse a CSV file into a list of CSVEntry objects.

    Args:
        filepath: Path to the CSV file

    Returns:
        List of CSVEntry objects with level and text information
    """
    entries = []
    displayed_navtitle_warning = False

    with open(filepath, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        # Skip lines until we find the header line (first column says "Category")
        line_number = 0
        for row in reader:
            line_number += 1
            if row and (len(row)>5) and ('ategor' in row[0].strip().lower()):
                # Found the header line, skip it and start processing after
                break

        # Now process the rest of the rows
        for row in reader:
            shift_idx = 0
            line_number += 1

            # Find all non-empty columns
            non_empty_columns = [Column(idx, col.strip()) for idx, col in enumerate(row) if col.strip()]
            
            # if the first column is non-empty, create a category entry and delete from the list
            # A category never has a topic file name
            if (len(non_empty_columns) > 0) and (non_empty_columns[0].idx == 0):
                category_entry = CSVEntry(level=0, line_number=line_number, is_job=True, 
                                          filename=None, navtitle=non_empty_columns[0].text)
 
                entries.append(category_entry)
                del non_empty_columns[0]
#                shift_idx = 1


            # Skip lines with no non-empty columns (or just the "job" marker)
            if len(non_empty_columns) == 0:
                continue
            if (len (non_empty_columns) == 1) and (non_empty_columns[0].text.upper() in ["TRUE","FALSE"]):
                continue 

            entry_idx = non_empty_columns[0].idx
            entry_filename = None
            entry_is_job = False
            entry_navtitle = non_empty_columns[0].text.strip()

            try:
                entry_filename = non_empty_columns[1].text.strip().lstrip("/")
                if (entry_filename.lower().find(".dita") == -1) and (entry_filename.lower().find(".adoc") == -1):
                    logger.warning(f"Line {line_number}: filename does not seem to have the right extension? {entry_filename}")
                entry_filename, _ = os.path.splitext(entry_filename)
                

                entry_is_job = (non_empty_columns[2].text.strip().upper() == "TRUE")
                if not (non_empty_columns[2].text.strip().upper() in ["TRUE","FALSE"]):
                    logger.warning(f"Line {line_number}: is_job not TRUE nor FALSE? {non_empty_columns[2].text}")

            except IndexError:
                logger.warning(f"Line {line_number} does not seem to have all fields")
                continue

            try:
                entry_navtitle = non_empty_columns[3].text
            except IndexError: pass


            entry = CSVEntry(level=shift_idx+entry_idx, line_number=line_number, is_job=entry_is_job, filename=entry_filename, navtitle=entry_navtitle)
            entries.append(entry)


    logger.debug("Entries parsed from CSV:")
    for entry in entries: logger.debug(str(entry))

    return entries


def create_ditamap(map_id: str, map_title: str, chunk: bool = False) -> ET.Element:
    """
    Create a DITAMAP structure with the root <map> element.

    Args:
        map_id: The ID attribute for the map element
        map_title: The title for the map
        chunk: If True, set chunk="to-content" on the map element

    Returns:
        ElementTree root element for the map
    """
    # Create root <map> element with id attribute
    attribs = {'id': map_id}
    if chunk:
        attribs['chunk'] = 'to-content'
    map_root = ET.Element('map', attrib=attribs)

    # Add <title> element
    title_elem = ET.SubElement(map_root, 'title')
    title_elem.text = map_title

    return map_root


def add_topicref(parent: ET.Element, href: str, topic_type: Optional[str] = None,
                 navtitle: str = '', chunk: bool = False, tocno: bool = False) -> ET.Element:
    """
    Add a topicref element to a parent element.

    Args:
        parent: The parent element to add the topicref to (typically <map>, <topichead>, or another <topicref>)
        href: The href attribute (filename to reference)
        topic_type: Optional type attribute for the topicref (e.g., 'task', 'concept', 'reference')
        navtitle: Optional navigation title for the topicref
        chunk: If True, set chunk="to-content" on the topicref element
        tocno: If True, set toc="no" on the topicref element

    Returns:
        The created topicref element (allows for nesting by adding children to it)
    """
    if href is None:
        href = "placeholder.dita"
    attribs = {'href': href}
    if topic_type:
        attribs['type'] = topic_type
    if navtitle:
        attribs['navtitle'] = navtitle
    if chunk:
        attribs['chunk'] = 'to-content'
    if tocno:
        attribs['toc'] = 'no'


    topicref = ET.SubElement(parent, 'topicref', attrib=attribs)
    return topicref

def add_topichead(parent: ET.Element, navtitle: str) -> ET.Element:
    """
    Add a topichead element to a parent element.

    Args:
        parent: The parent element to add the topichead to (typically <map>)
        navtitle: navigation title for the topichead

    Returns:
        The created topichead element (allows for nesting by adding children to it)
    """
    attribs = {'navtitle': navtitle}

    topichead = ET.SubElement(parent, 'topichead', attrib=attribs)
    return topichead



def add_mapref(parent: ET.Element, href: str) -> ET.Element:
    """
    Add a mapref element to a parent element.

    Args:
        parent: The parent element to add the mapref to (typically <map> or a <topicref>)
        href: The href attribute (filename to reference)

    Returns:
        The created topicref element (allows for nesting by adding children to it)
    """
    attribs = {'href': href}

    topicref = ET.SubElement(parent, 'mapref', attrib=attribs)
    return topicref


def write_ditamap(map_root: ET.Element, output_file: str):
    """
    Write the DITAMAP to a file with proper DOCTYPE declaration and formatting.

    Args:
        map_root: The root map element
        output_file: Path to the output file
    """
    # Indent the XML for pretty printing
    ET.indent(map_root, space='  ')

    # We need to manually construct the output to include DOCTYPE
    with open(output_pathname(output_file), 'w', encoding='utf-8') as f:
        # Write XML declaration
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')

        # Write DOCTYPE declaration
        f.write('<!DOCTYPE map PUBLIC "-//OASIS//DTD DITA Map//EN" "technicalContent/dtd/map.dtd">\n')

        # Write the XML tree
        # Use ET.tostring to get the XML content
        xml_string = ET.tostring(map_root, encoding='unicode')
        f.write(xml_string)
        if not xml_string.endswith('\n'):
            f.write('\n')

    logger.info(f"DITAMAP written to {output_file}")

def writeline(filename: str, line: str):
    """Write a line to a file, overwriting on first write, appending subsequently."""
    logger.debug(f"Writing to {filename}:\n{line}")
    mode = "w" if filename not in _written_files else "a"
    with open(output_pathname(filename), mode) as f:
        f.write(line.rstrip() + "\n\n")
    _written_files.add(filename)


def process_level(parent: ET.Element, entries: List[CSVEntry], index: int,
                  asciidoc_name: str, asciidoc_level: int, prefix: str) -> int:
    """Process the entry at the index and any entries of the same or subordinate levels, adding to the parent element
    returns the next index - either the level there is higher or it is past the end"""
    current_entry = entries[index]
    current_index = index
    min_level = current_entry.level
    last_level = current_entry.level
    parent_for_children = None
    ditamap_for_children = None
    ditamap_name_for_children = None
    asciidoc_name_for_children = asciidoc_name
    asciidoc_level_for_children = asciidoc_level + 1

    logger.debug(f"process_level called: asciidoc_level={asciidoc_level}, entry is {entries[index]}")

    while current_entry.level >= min_level:
        if current_entry.level == min_level:
            last_level = current_entry.level
            # if we created a ditamap for children earlier, we are now done with those children, save the map
            if ditamap_for_children is not None and ditamap_name_for_children is not None:
                write_ditamap(ditamap_for_children, ditamap_name_for_children)


            # as we are on the current level, UNDO any changes for writing children to submap
            asciidoc_name_for_children = asciidoc_name
            asciidoc_level_for_children = asciidoc_level + 1

            # determine if the current entry needs chunk="to-content"
            # this determination requires look-ahead to the next entry
            chunk = False
            chunk_string=''
            if current_entry.level < MIN_CHUNKED_LEVEL:
                next_index = current_index + 1
                if next_index < len(entries):
                    if entries[next_index].level >= MIN_CHUNKED_LEVEL:
                        chunk = True
                        chunk_string = ',chunk="to-content"'

            # determine if the current entry needs toc="no"
            tocno = (current_entry.level >= MIN_CHUNKED_LEVEL)
            tocno_string = ',toc="no"' if tocno else ''


            # No child ditamap for non-job entries
            ditamap_for_children = None
            ditamap_name_for_children = None


            if current_entry.is_job:
                logger.debug(f"Processing job, asciidoc_level_for_children={asciidoc_level_for_children}")

                # determine if a filename is to be processed
                filename = current_entry.filename 
                if filename and ("master" in filename):
                    # determine if content is in the master.adoc file and if so, save a renamed version
                    content = None
                    try:
                        content = open(filename+".adoc").read()
                    except Exception:
                        logger.warning(f"Cannot read {filename}.adoc - the file is not included in the maps")
                        filename = None 
                    if content:
                        if (":_mod-docs-content-type" in content):
                            # Get filename based on title or id
                            new_filename = None

                            # Try to find level 1 title (= Title)
                            title_pattern = re.compile(r'''
                                ^           # Start of line (must be exactly at newline)
                                =\s+        # Single = followed by whitespace (level 1 heading)
                                (.+)        # Capture the title text
                                $           # End of line
                            ''', re.MULTILINE | re.VERBOSE)

                            title_match = title_pattern.search(content)
                            if title_match:
                                title = title_match.group(1).strip()
                                new_filename = title_to_basename(title)
                            else:
                                # Try to find id setting [id="..." or id='...']
                                id_pattern = re.compile(r'''
                                    ^           # Start of line (must be exactly at newline)
                                    \[id=       # Literal [id=
                                    (["'])      # Capture opening quote (single or double)
                                    ([^"']+)    # Capture the id value (everything until a quote)
                                    \1          # Backreference: match the same quote type as opening
                                    \]          # Closing ]
                                ''', re.MULTILINE | re.VERBOSE)

                                id_match = id_pattern.search(content)
                                if id_match:
                                    new_filename = id_match.group(2).strip()  # Group 2 is the id value
                                else:
                                    logger.warning(f"Cannot find title or id in {filename}.adoc - skipping file")
                                    new_filename = None
                        else:
                            logger.warning(f"No content type in {filename}.adoc - the file is not included in the maps")
                            new_filename = None
                        if new_filename:
                            try:
                                with open(output_pathname(new_filename+".adoc"),"w") as o:
                                    o.write(content)
                                logger.info(f"Copied {filename}.adoc to {new_filename}.adoc")
                                filename = new_filename
                            except Exception:
                                logger.warning(f"Failed to write file {new_filename}.adoc based on {filename}.adoc - the file is not included in the maps")
                                filename = None
                        else:
                            filename = None

                # Create child DITA map and asciidoc map if needed
                parent_for_adding = parent
                asciidoc_name_for_adding = asciidoc_name
                if current_entry.level <= MAX_SUBMAP_LEVEL:

                    map_basename = title_to_basename(current_entry.navtitle)
                    if current_entry.level == 0: # add prefix for the category
                        map_basename = prefix + "-" + map_basename

                    chunk_root = chunk and not filename

                    chunk_root_string = chunk_string if chunk_root else ""

                    logger.debug(f"Will create submap: {map_basename}")

                    asciidoc_name_for_children = map_basename+".adoc"
                    asciidoc_name_for_adding = asciidoc_name_for_children
                    writeline(asciidoc_name,f"include::{asciidoc_name_for_children}[leveloffset=+{asciidoc_level}{chunk_root_string}]")
                    writeline(asciidoc_name_for_children,":_mod-docs-content-type: MAP")
                    writeline(asciidoc_name_for_children, f"= {current_entry.navtitle}")
                    asciidoc_level_for_children = 1

                    # Create child ditamap and add it to the parent map
                    ditamap_name_for_children = map_basename + ".ditamap"
                    add_mapref(parent, ditamap_name_for_children)
                    parent_for_adding = create_ditamap(map_basename, current_entry.navtitle, chunk_root)
                    ditamap_for_children = parent_for_adding


                # If this is a category (level 0), or else if no submap got created and there is no filename, create the topichead
                if (current_entry.level == 0) or ((not filename) and (parent_for_adding == parent)):
                    parent_for_children = add_topichead(parent_for_adding, current_entry.navtitle)
                else:
                    parent_for_children = parent_for_adding


                # If there's a filename, add it as a topicref (in the child ditamap if applicable) 
                #  and also add it to the applicable asciidoc map
                if filename:
                    parent_for_children = add_topicref(parent_for_children, filename+".dita", 
                                                       navtitle=current_entry.navtitle, chunk=chunk, tocno=tocno)
                    # if a new asciidoc map was created, we must add at level 1 and set asciidoc_level_for_children to 2
                    if asciidoc_name_for_adding != asciidoc_name:
                        writeline(asciidoc_name_for_adding,f"include::{filename}.adoc[leveloffset=+1{chunk_string}{tocno_string}]")
                        asciidoc_level_for_children = 2
                    else:
                        # if continuing the current asciidoc map, add at the current level, chuldren will be processed normally
                        writeline(asciidoc_name_for_adding,f"include::{filename}.adoc[leveloffset=+{asciidoc_level}{chunk_string}{tocno_string}]")
                elif asciidoc_name_for_adding == asciidoc_name:
                    # no filename and no child asciidoc map created - create subtopic in existing ascidoc map
                    asciidoc_level_for_children += 1
                    header_prefix = asciidoc_level_for_children*"="
                    writeline(asciidoc_name_for_adding,f"{header_prefix} {current_entry.navtitle}")
    
            else:
                # add the line to the current asciidoc map
                navtitle_string = f',navtitle="{current_entry.navtitle}"' if current_entry.navtitle else ""
                writeline(asciidoc_name,f"include::{current_entry.filename}.adoc[leveloffset=+{asciidoc_level}{chunk_string}{tocno_string}{navtitle_string}]")
                # Add topicref for this entry (non-job always has filename)
                parent_for_children = add_topicref(parent, current_entry.filename+".dita", 
                                                   navtitle=current_entry.navtitle, chunk=chunk, tocno=tocno)

            current_index += 1
        else:
            # if we were processing "deeper children" then encounter a "shallower child", 
            #   warn that this will be processed wrong
            if last_level > current_entry.level:
                logger.warning(f"Encountered level {current_entry.level} after level {last_level}, the levels might be flattened, filename: {current_entry.filename}")
            last_level = current_entry.level

            # Process children - use child ditamap if it was created, otherwise use parent_for_children
            current_index = process_level(parent_for_children, entries, current_index,
                                          asciidoc_name_for_children, asciidoc_level_for_children, prefix)

        if current_index >= len(entries):
            break # the current index is past the end
        current_entry = entries[current_index]

    # if we created a ditamap for children earlier, we are now done with those children, save the map
    if ditamap_for_children is not None and ditamap_name_for_children is not None:
        write_ditamap(ditamap_for_children, ditamap_name_for_children)

    return current_index
            

def main():
    """Main function to demonstrate CSV parsing and DITAMAP creation."""

    parser = argparse.ArgumentParser(description='Convert CSV to DITAMAP')
    parser.add_argument('csv_file', help='Path to the CSV file')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug logging')
    parser.add_argument('--prefix', help='Prefix (product and version) for file names')
    parser.add_argument('--output-dir', metavar='DIR', help='Directory for all generated files (created if absent)')

    args = parser.parse_args()

    # Set logging level based on debug flag
    if args.debug:
        logger.setLevel(logging.DEBUG)

    # Set output directory
    global _output_dir
    if args.output_dir:
        _output_dir = args.output_dir
        os.makedirs(_output_dir, exist_ok=True)
        logger.info(f"Output directory: {_output_dir}")

    # Clear written files set for this run
    _written_files.clear()

    csv_file = args.csv_file

    # Determine prefix: use --prefix if provided, otherwise use input filename without extension
    if args.prefix:
        prefix = args.prefix
    else:
        prefix = os.path.splitext(os.path.basename(csv_file))[0]

    output_file = prefix + "-navigation.ditamap"
    asciimap_file = prefix + "-navigation.adoc"

    logger.info(f"Parsing {csv_file}...")
    entries = parse_csv(csv_file)

    logger.info(f"Parsed {len(entries)} entries")
    #TEMP
    #sys.exit()


    if output_file:
        # Use prefix as map ID
        map_id = prefix
        map_title = prefix  # Can be customized

        logger.info(f"\nCreating DITAMAP with id='{map_id}'...")
        map_root = create_ditamap(map_id, map_title)

        writeline(asciimap_file,":_mod-docs-content-type: MAP")


        process_level(map_root, entries, 0, asciimap_file, 1, prefix)
        
        write_ditamap(map_root, output_file)
        print(f"\nDITAMAP structure created at: {output_file}")


if __name__ == "__main__":
    main()

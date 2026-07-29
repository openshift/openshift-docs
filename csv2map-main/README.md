# CSV2MAP

The `csv2map.py` script reads a CSV-exported JTBD spreadsheet and creates two sets of map files:

* Draft DITA maps
* Asciidoc maps

The script was developed by Misha Ramendik <mramendi@redhat.com>. It is a development version; testing and feature requests are much appreciated.

An example of the JTBD spreadsheet format can be found at https://docs.google.com/spreadsheets/d/1RTP9-dM6UpBsh2GR4lzJ3smHLDWt8I-aynTzI_50F10/edit?gid=0#gid=0 .

IMPORTANT: The header line must contain the word "Category" in the first column; this is how the script detects the start of the content.

To use the script, take the following steps:

1. Open the spreadsheet in Google Sheets and select the correct tab.
1. In the menu, select **File -> Download -> Comma Separated Values (.csv)** to save the spreadsheet as a CSV file.
1. Run the script with the following command:

```
python csv2map.py <filename>.csv --prefix <product>-<version>
```

For example:

```
python csv2map.py thokp.csv --prefix offline-knowledge-portal-1
```

The prefix value is used for naming the navigation map and the category maps in accordance with the [Filenames in AEM](https://docs.google.com/document/d/1pXEmqX74ShzKJEC2erOI9ZRFtXDbkjaEDtVUg4WqN24/edit?tab=t.0) document.

To write all generated files into a specific directory instead of the current directory, use the `--output-dir` option:

```
python csv2map.py thokp.csv --prefix offline-knowledge-portal-1 --output-dir output/
```

The directory is created automatically if it does not exist.

**Important**: If the spreadsheet refers to `master.adoc` files for the jobs and these files contain documentation content, you must make these files available at the specified path when running the script. In this case, the script copies the files, creating new names for them from their titles, and then adds them to the maps. 

If `master.adoc` files are not available during the run of the script, or if they are available but contain no documentation content, the script does not include these files in the maps. To detect whether a `master.adoc` file has documentation content, the script checks for the presence of the content type attribute.

## comment-out-includes.py

If you include assemblies in your TOC and then build from Asciidoc maps, by default the include directories in the assemblies are processed, pulling in the old structure as well as the new one. To avoid this, you can run the `comment-out-includes.py` script, specifying the path to the root of your asciidoc tree. The script goes through all the *.adoc files, identifies assemblies by the content type, and comments out include directoves that come after the title (to keep any attribute includes, normally done befoer the title). Only fules with ASSEMBLY and IGNORE doc type attributes are changed; sometimes people use IGNORE for assemblies but these assemblies really should not be in the TOC at all, so a warning that such files should noit be in the build is added to the files.


## Change history

27 July 2026: comment-out-includes.py added (initial version)

18 July 2026: fixed a bug in asciidoc map levels and added  --output-dir

30 April 2026: no submaps below level 2; toc="no" now also added in asciidoc maps

24 April 2026: hierarchy in job ditamaps fixed; chunking should always be on topicrefs in normal setups; `toc="no"` added for chunked topics; navtitles should be optional now

17 April 2026: chunking now supported. If a topic is in column E or further to the right, it the topic or map on the level above it, so in column D or below, gets the `chunk="to-content"` attribute.

24 April 2026: improved the support for chunking and clarified the hierarchy

30 Aprol 2026: changed the submap creation logic; no submaps are created below level 2 now

13 May 2026: in asiidoc maps, added a content type line at the start and saving the navtitle

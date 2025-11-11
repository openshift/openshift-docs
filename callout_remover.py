#!/usr/bin/env python3
"""
AsciiDoc Callout Remover
Converts numbered callouts in AsciiDoc code blocks to cleaner inline or definition list formats.
"""

import re
import sys
import os
from pathlib import Path
from typing import List, Tuple, Dict

class CalloutRemover:
    def __init__(self):
        # Matches callouts with optional comment markers: <1>, # <1>, // <1>, etc.
        self.callout_pattern = re.compile(r'(?://|#)?\s*<(\d+)>')
        
    def process_file(self, content: str) -> str:
        """Process entire AsciiDoc file content."""
        lines = content.split('\n')
        result = []
        i = 0
        
        while i < len(lines):
            # Check if we're at the start of a code block
            if self._is_code_block_start(lines[i]):
                block_end = self._find_code_block_end(lines, i)
                if block_end != -1:
                    # Process this code block and its callouts
                    processed = self._process_code_block_section(lines[i:block_end+1])
                    result.extend(processed)
                    i = block_end + 1
                else:
                    result.append(lines[i])
                    i += 1
            else:
                result.append(lines[i])
                i += 1
        
        return '\n'.join(result)
    
    def _is_code_block_start(self, line: str) -> bool:
        """Check if line starts a code block."""
        return line.strip().startswith('[source,') or line.strip() == '----'
    
    def _find_code_block_end(self, lines: List[str], start: int) -> int:
        """Find the end of a code block section including callout explanations."""
        # Find the code block delimiters
        delimiter_count = 0
        code_end = start
        
        for i in range(start, len(lines)):
            if lines[i].strip() == '----':
                delimiter_count += 1
                if delimiter_count == 2:
                    code_end = i
                    break
        
        if delimiter_count < 2:
            return -1
        
        # Check if there are actual callout explanations immediately after code block
        # Only look in the next few lines to avoid capturing unrelated content
        explanation_end = code_end
        found_explanation = False
        
        for i in range(code_end + 1, min(code_end + 5, len(lines))):
            line = lines[i].strip()
            
            # Check for AsciiDoc callout list markers: <1>, <2>, etc. at start of line
            if re.match(r'^<\d+>\s', line):
                found_explanation = True
                explanation_end = i
                break
            # Check for numbered list items: 1., 2., etc. but only if not preceded by blank line
            elif re.match(r'^\d+\.\s', line) and i == code_end + 1:
                found_explanation = True
                explanation_end = i
                break
            # Skip empty lines
            elif line == '':
                continue
            # If we hit other content, stop looking
            else:
                break
        
        # If we found explanations, continue collecting them
        if found_explanation:
            for i in range(explanation_end + 1, len(lines)):
                line = lines[i].strip()
                
                # Continue with numbered explanations or callout format
                if re.match(r'^<\d+>\s', line) or re.match(r'^\d+\.\s', line):
                    explanation_end = i
                # Continue with continuation text (indented or part of list)
                elif line and not line.startswith('==') and not line.startswith('.*') and not line.startswith('['):
                    # Check if it looks like continuation of explanation
                    prev_line = lines[i-1].strip() if i > 0 else ''
                    if prev_line and (re.match(r'^<\d+>\s', prev_line) or re.match(r'^\d+\.\s', prev_line) or explanation_end == i - 1):
                        explanation_end = i
                    else:
                        break
                # Empty line might be part of explanation
                elif line == '' and i < len(lines) - 1:
                    next_line = lines[i+1].strip()
                    if re.match(r'^<\d+>\s', next_line) or re.match(r'^\d+\.\s', next_line):
                        explanation_end = i
                    else:
                        break
                else:
                    break
        
        return explanation_end
    
    def _process_code_block_section(self, section: List[str]) -> List[str]:
        """Process a code block and its callout explanations."""
        # Extract code block
        code_start = -1
        code_end = -1
        delimiter_count = 0
        
        for i, line in enumerate(section):
            if line.strip() == '----':
                delimiter_count += 1
                if delimiter_count == 1:
                    code_start = i
                elif delimiter_count == 2:
                    code_end = i
                    break
        
        if code_start == -1 or code_end == -1:
            return section
        
        # Extract code lines and callout explanations
        code_lines = section[code_start+1:code_end]
        explanation_section = section[code_end+1:]
        
        # Find callouts in code
        callouts = self._extract_callouts_from_code(code_lines)
        
        # If no callouts found in code, return original section unchanged
        if not callouts:
            return section
        
        # Extract explanations
        explanations = self._extract_explanations(explanation_section, len(callouts))
        
        # If no explanations found, return original section unchanged
        if not explanations:
            return section
        
        # Remove callout markers from code
        cleaned_code = self._remove_callout_markers(code_lines)
        
        # Build result
        result = section[:code_start+1]  # Include everything before code
        result.extend(cleaned_code)
        result.append('----')
        
        # Add explanations in appropriate format
        formatted_explanations = self._format_explanations(callouts, explanations, cleaned_code)
        result.extend(formatted_explanations)
        
        return result
    
    def _extract_callouts_from_code(self, code_lines: List[str]) -> Dict[int, str]:
        """Extract callout positions and associated code."""
        callouts = {}
        for line in code_lines:
            matches = self.callout_pattern.findall(line)
            for match in matches:
                num = int(match)
                # Extract the code portion (without callout)
                code_part = re.sub(r'(?://|#)?\s*<\d+>', '', line).strip()
                callouts[num] = code_part
        return callouts
    
    def _extract_explanations(self, explanation_lines: List[str], num_callouts: int) -> Dict[int, str]:
        """Extract explanation text for each callout."""
        explanations = {}
        current_num = None
        current_text = []
        
        for line in explanation_lines:
            stripped = line.strip()
            
            # Skip empty lines at the start
            if not stripped and current_num is None:
                continue
            
            # Check for AsciiDoc callout list format: <1>, <2>, etc.
            callout_match = re.match(r'^<(\d+)>\s+(.*)
    
    def _remove_callout_markers(self, code_lines: List[str]) -> List[str]:
        """Remove callout markers from code lines."""
        cleaned = []
        for line in code_lines:
            # Remove callout markers with optional comment prefixes (# <1>, // <1>, <1>)
            cleaned_line = re.sub(r'(?://|#)?\s*<\d+>\s*$', '', line)
            # Also handle callouts in the middle of lines
            cleaned_line = re.sub(r'(?://|#)\s*<\d+>', '', cleaned_line)
            cleaned.append(cleaned_line.rstrip())
        return cleaned
    
    def _format_explanations(self, callouts: Dict[int, str], 
                           explanations: Dict[int, str], 
                           code_lines: List[str]) -> List[str]:
        """Format explanations based on content type."""
        result = []
        
        # Single callout - use inline paragraph (no definition list)
        if len(callouts) == 1:
            num = list(callouts.keys())[0]
            if num in explanations:
                # Add blank line before explanation for proper spacing
                result.append('')
                result.append(explanations[num])
            return result
        
        # Multiple callouts - check for user-replaceable values (placeholders like <n>, $var)
        has_user_values = any(
            re.search(r'<\w+>', line) or re.search(r'\$\w+', line) 
            for line in code_lines
        )
        
        # Check if it looks like configuration (YAML, properties)
        is_config = self._looks_like_config(code_lines)
        
        if is_config and not has_user_values:
            # Configuration file - use definition list with parameter names
            result.append('')
            for num in sorted(callouts.keys()):
                if num in explanations:
                    term = self._extract_config_term(callouts[num])
                    result.append(f'{term}:: {explanations[num]}')
        elif has_user_values:
            # Code with user-replaceable values - use "where:" format
            result.append('')
            result.append('where:')
            result.append('')
            for num in sorted(callouts.keys()):
                if num in explanations:
                    term = self._extract_placeholder_term(callouts[num])
                    result.append(f'{term}:: {explanations[num]}')
        else:
            # Regular code - use definition list with code references
            result.append('')
            for num in sorted(callouts.keys()):
                if num in explanations:
                    term = self._extract_code_term(callouts[num])
                    result.append(f'{term}:: {explanations[num]}')
        
        return result
    
    def _looks_like_config(self, code_lines: List[str]) -> bool:
        """Check if code looks like configuration (YAML, properties, etc.)."""
        config_patterns = [': ', '=', 'baseDN', 'scope', 'timeout']
        code_text = ' '.join(code_lines)
        return any(pattern in code_text for pattern in config_patterns)
    
    def _extract_config_term(self, code_line: str) -> str:
        """Extract term for configuration parameters."""
        # Extract parameter name from YAML/config format
        if ':' in code_line:
            param = code_line.split(':')[0].strip()
            return f'`{param}`'
        elif '=' in code_line:
            param = code_line.split('=')[0].strip()
            return f'`{param}`'
        # Look for just the parameter name
        param = code_line.split()[0] if code_line.split() else code_line
        return f'`{param}`'
    
    def _extract_placeholder_term(self, code_line: str) -> str:
        """Extract term for user-replaceable placeholders."""
        # Look for <placeholder> format
        placeholder_match = re.search(r'<(\w+)>', code_line)
        if placeholder_match:
            return f'<{placeholder_match.group(1)}>'
        
        # Look for $variable format
        var_match = re.search(r'\$(\w+)', code_line)
        if var_match:
            return f'`${var_match.group(1)}`'
        
        # Look for method/function calls
        method_match = re.search(r'(\w+)\s*\(', code_line)
        if method_match:
            return f'`{method_match.group(1)}`'
        
        # Default to first significant token
        tokens = code_line.split()
        if tokens:
            return f'`{tokens[0]}`'
        return f'`{code_line[:30]}`'
    
    def _extract_code_term(self, code_line: str) -> str:
        """Extract term for code explanations."""
        # Look for variable assignments
        if '=' in code_line:
            var = code_line.split('=')[0].strip()
            return f'`{var}`'
        
        # Look for method calls
        method_match = re.search(r'(\w+)\s*\(', code_line)
        if method_match:
            return f'`{method_match.group(1)}`'
        
        # Use first meaningful part
        return f'`{code_line[:40]}`' if len(code_line) > 40 else f'`{code_line}`'


def process_directory(directory_path: str, output_dir: str = None, dry_run: bool = False):
    """Process all .adoc files in a directory."""
    directory = Path(directory_path)
    
    if not directory.exists():
        print(f"Error: Directory '{directory_path}' does not exist")
        return
    
    if not directory.is_dir():
        print(f"Error: '{directory_path}' is not a directory")
        return
    
    # Find all .adoc files
    adoc_files = list(directory.glob('**/*.adoc'))
    
    if not adoc_files:
        print(f"No .adoc files found in {directory_path}")
        return
    
    print(f"Found {len(adoc_files)} .adoc file(s)")
    
    remover = CalloutRemover()
    processed_count = 0
    error_count = 0
    
    for adoc_file in adoc_files:
        try:
            print(f"Processing: {adoc_file}")
            
            with open(adoc_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file has callouts
            if not re.search(r'<\d+>', content):
                print(f"  ⊘ No callouts found, skipping")
                continue
            
            result = remover.process_file(content)
            
            if dry_run:
                print(f"  ✓ Would process (dry-run mode)")
            else:
                # Determine output path
                if output_dir:
                    output_path = Path(output_dir) / adoc_file.name
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                else:
                    output_path = adoc_file
                
                # Write result
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(result)
                
                print(f"  ✓ Processed successfully")
            
            processed_count += 1
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
            error_count += 1
    
    print(f"\nSummary:")
    print(f"  Processed: {processed_count}")
    print(f"  Errors: {error_count}")
    print(f"  Total files: {len(adoc_files)}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file: python callout_remover.py <input_file> [output_file]")
        print("  Directory:   python callout_remover.py --dir <directory> [--output <output_dir>] [--dry-run]")
        print("\nOptions:")
        print("  --dir <directory>       Process all .adoc files in directory")
        print("  --output <output_dir>   Save processed files to output directory (default: overwrite originals)")
        print("  --dry-run               Show what would be processed without making changes")
        sys.exit(1)
    
    # Check if directory mode
    if '--dir' in sys.argv:
        dir_index = sys.argv.index('--dir')
        if dir_index + 1 >= len(sys.argv):
            print("Error: --dir requires a directory path")
            sys.exit(1)
        
        directory = sys.argv[dir_index + 1]
        output_dir = None
        dry_run = '--dry-run' in sys.argv
        
        if '--output' in sys.argv:
            output_index = sys.argv.index('--output')
            if output_index + 1 < len(sys.argv):
                output_dir = sys.argv[output_index + 1]
        
        process_directory(directory, output_dir, dry_run)
    else:
        # Single file mode
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            remover = CalloutRemover()
            result = remover.process_file(content)
            
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(result)
                print(f"Processed file written to: {output_file}")
            else:
                print(result)
        
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found")
            sys.exit(1)
        except Exception as e:
            print(f"Error processing file: {e}")
            sys.exit(1)


if __name__ == '__main__':
    main()
, stripped)
            if callout_match:
                if current_num is not None:
                    explanations[current_num] = ' '.join(current_text).strip()
                current_num = int(callout_match.group(1))
                current_text = [callout_match.group(2)]
                continue
            
            # Check for numbered list item (1., 2., etc.)
            numbered_match = re.match(r'^(\d+)\.\s+(.*)
    
    def _remove_callout_markers(self, code_lines: List[str]) -> List[str]:
        """Remove callout markers from code lines."""
        cleaned = []
        for line in code_lines:
            # Remove callout markers with optional comment prefixes (# <1>, // <1>, <1>)
            cleaned_line = re.sub(r'(?://|#)?\s*<\d+>\s*$', '', line)
            # Also handle callouts in the middle of lines
            cleaned_line = re.sub(r'(?://|#)\s*<\d+>', '', cleaned_line)
            cleaned.append(cleaned_line.rstrip())
        return cleaned
    
    def _format_explanations(self, callouts: Dict[int, str], 
                           explanations: Dict[int, str], 
                           code_lines: List[str]) -> List[str]:
        """Format explanations based on content type."""
        result = []
        
        # Single callout - use inline paragraph
        if len(callouts) == 1:
            num = list(callouts.keys())[0]
            if num in explanations:
                result.append(explanations[num])
            return result
        
        # Check for user-replaceable values (placeholders like <n>, $var)
        has_user_values = any(
            re.search(r'<\w+>', line) or re.search(r'\$\w+', line) 
            for line in code_lines
        )
        
        # Check if it looks like configuration (YAML, properties)
        is_config = self._looks_like_config(code_lines)
        
        if is_config and not has_user_values:
            # Configuration file - use definition list with parameter names
            result.append('')
            for num in sorted(callouts.keys()):
                if num in explanations:
                    term = self._extract_config_term(callouts[num])
                    result.append(f'{term}:: {explanations[num]}')
        elif has_user_values:
            # Code with user-replaceable values - use "where:" format
            result.append('')
            result.append('where:')
            result.append('')
            for num in sorted(callouts.keys()):
                if num in explanations:
                    term = self._extract_placeholder_term(callouts[num])
                    result.append(f'{term}:: {explanations[num]}')
        else:
            # Regular code - use definition list with code references
            result.append('')
            for num in sorted(callouts.keys()):
                if num in explanations:
                    term = self._extract_code_term(callouts[num])
                    result.append(f'{term}:: {explanations[num]}')
        
        return result
    
    def _looks_like_config(self, code_lines: List[str]) -> bool:
        """Check if code looks like configuration (YAML, properties, etc.)."""
        config_patterns = [': ', '=', 'baseDN', 'scope', 'timeout']
        code_text = ' '.join(code_lines)
        return any(pattern in code_text for pattern in config_patterns)
    
    def _extract_config_term(self, code_line: str) -> str:
        """Extract term for configuration parameters."""
        # Extract parameter name from YAML/config format
        if ':' in code_line:
            param = code_line.split(':')[0].strip()
            return f'`{param}`'
        elif '=' in code_line:
            param = code_line.split('=')[0].strip()
            return f'`{param}`'
        # Look for just the parameter name
        param = code_line.split()[0] if code_line.split() else code_line
        return f'`{param}`'
    
    def _extract_placeholder_term(self, code_line: str) -> str:
        """Extract term for user-replaceable placeholders."""
        # Look for <placeholder> format
        placeholder_match = re.search(r'<(\w+)>', code_line)
        if placeholder_match:
            return f'<{placeholder_match.group(1)}>'
        
        # Look for $variable format
        var_match = re.search(r'\$(\w+)', code_line)
        if var_match:
            return f'`${var_match.group(1)}`'
        
        # Look for method/function calls
        method_match = re.search(r'(\w+)\s*\(', code_line)
        if method_match:
            return f'`{method_match.group(1)}`'
        
        # Default to first significant token
        tokens = code_line.split()
        if tokens:
            return f'`{tokens[0]}`'
        return f'`{code_line[:30]}`'
    
    def _extract_code_term(self, code_line: str) -> str:
        """Extract term for code explanations."""
        # Look for variable assignments
        if '=' in code_line:
            var = code_line.split('=')[0].strip()
            return f'`{var}`'
        
        # Look for method calls
        method_match = re.search(r'(\w+)\s*\(', code_line)
        if method_match:
            return f'`{method_match.group(1)}`'
        
        # Use first meaningful part
        return f'`{code_line[:40]}`' if len(code_line) > 40 else f'`{code_line}`'


def process_directory(directory_path: str, output_dir: str = None, dry_run: bool = False):
    """Process all .adoc files in a directory."""
    directory = Path(directory_path)
    
    if not directory.exists():
        print(f"Error: Directory '{directory_path}' does not exist")
        return
    
    if not directory.is_dir():
        print(f"Error: '{directory_path}' is not a directory")
        return
    
    # Find all .adoc files
    adoc_files = list(directory.glob('**/*.adoc'))
    
    if not adoc_files:
        print(f"No .adoc files found in {directory_path}")
        return
    
    print(f"Found {len(adoc_files)} .adoc file(s)")
    
    remover = CalloutRemover()
    processed_count = 0
    error_count = 0
    
    for adoc_file in adoc_files:
        try:
            print(f"Processing: {adoc_file}")
            
            with open(adoc_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file has callouts
            if not re.search(r'<\d+>', content):
                print(f"  ⊘ No callouts found, skipping")
                continue
            
            result = remover.process_file(content)
            
            if dry_run:
                print(f"  ✓ Would process (dry-run mode)")
            else:
                # Determine output path
                if output_dir:
                    output_path = Path(output_dir) / adoc_file.name
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                else:
                    output_path = adoc_file
                
                # Write result
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(result)
                
                print(f"  ✓ Processed successfully")
            
            processed_count += 1
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
            error_count += 1
    
    print(f"\nSummary:")
    print(f"  Processed: {processed_count}")
    print(f"  Errors: {error_count}")
    print(f"  Total files: {len(adoc_files)}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file: python callout_remover.py <input_file> [output_file]")
        print("  Directory:   python callout_remover.py --dir <directory> [--output <output_dir>] [--dry-run]")
        print("\nOptions:")
        print("  --dir <directory>       Process all .adoc files in directory")
        print("  --output <output_dir>   Save processed files to output directory (default: overwrite originals)")
        print("  --dry-run               Show what would be processed without making changes")
        sys.exit(1)
    
    # Check if directory mode
    if '--dir' in sys.argv:
        dir_index = sys.argv.index('--dir')
        if dir_index + 1 >= len(sys.argv):
            print("Error: --dir requires a directory path")
            sys.exit(1)
        
        directory = sys.argv[dir_index + 1]
        output_dir = None
        dry_run = '--dry-run' in sys.argv
        
        if '--output' in sys.argv:
            output_index = sys.argv.index('--output')
            if output_index + 1 < len(sys.argv):
                output_dir = sys.argv[output_index + 1]
        
        process_directory(directory, output_dir, dry_run)
    else:
        # Single file mode
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            remover = CalloutRemover()
            result = remover.process_file(content)
            
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(result)
                print(f"Processed file written to: {output_file}")
            else:
                print(result)
        
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found")
            sys.exit(1)
        except Exception as e:
            print(f"Error processing file: {e}")
            sys.exit(1)


if __name__ == '__main__':
    main()
, stripped)
            if numbered_match:
                if current_num is not None:
                    explanations[current_num] = ' '.join(current_text).strip()
                current_num = int(numbered_match.group(1))
                current_text = [numbered_match.group(2)]
                continue
            
            # Continue collecting text for current explanation
            if current_num is not None:
                if stripped:
                    # Check if it's a continuation line or sub-list
                    if stripped.startswith('*') or stripped.startswith('-'):
                        current_text.append('\n' + stripped)
                    else:
                        current_text.append(stripped)
                elif current_text:  # Empty line after text - save current explanation
                    explanations[current_num] = ' '.join(current_text).strip()
                    current_num = None
                    current_text = []
            elif stripped:
                # Hit non-empty line without being in an explanation - stop
                break
        
        # Save last explanation
        if current_num is not None and current_text:
            explanations[current_num] = ' '.join(current_text).strip()
        
        return explanations
    
    def _remove_callout_markers(self, code_lines: List[str]) -> List[str]:
        """Remove callout markers from code lines."""
        cleaned = []
        for line in code_lines:
            # Remove callout markers with optional comment prefixes (# <1>, // <1>, <1>)
            cleaned_line = re.sub(r'(?://|#)?\s*<\d+>\s*$', '', line)
            # Also handle callouts in the middle of lines
            cleaned_line = re.sub(r'(?://|#)\s*<\d+>', '', cleaned_line)
            cleaned.append(cleaned_line.rstrip())
        return cleaned
    
    def _format_explanations(self, callouts: Dict[int, str], 
                           explanations: Dict[int, str], 
                           code_lines: List[str]) -> List[str]:
        """Format explanations based on content type."""
        result = []
        
        # Single callout - use inline paragraph
        if len(callouts) == 1:
            num = list(callouts.keys())[0]
            if num in explanations:
                result.append(explanations[num])
            return result
        
        # Check for user-replaceable values (placeholders like <n>, $var)
        has_user_values = any(
            re.search(r'<\w+>', line) or re.search(r'\$\w+', line) 
            for line in code_lines
        )
        
        # Check if it looks like configuration (YAML, properties)
        is_config = self._looks_like_config(code_lines)
        
        if is_config and not has_user_values:
            # Configuration file - use definition list with parameter names
            result.append('')
            for num in sorted(callouts.keys()):
                if num in explanations:
                    term = self._extract_config_term(callouts[num])
                    result.append(f'{term}:: {explanations[num]}')
        elif has_user_values:
            # Code with user-replaceable values - use "where:" format
            result.append('')
            result.append('where:')
            result.append('')
            for num in sorted(callouts.keys()):
                if num in explanations:
                    term = self._extract_placeholder_term(callouts[num])
                    result.append(f'{term}:: {explanations[num]}')
        else:
            # Regular code - use definition list with code references
            result.append('')
            for num in sorted(callouts.keys()):
                if num in explanations:
                    term = self._extract_code_term(callouts[num])
                    result.append(f'{term}:: {explanations[num]}')
        
        return result
    
    def _looks_like_config(self, code_lines: List[str]) -> bool:
        """Check if code looks like configuration (YAML, properties, etc.)."""
        config_patterns = [': ', '=', 'baseDN', 'scope', 'timeout']
        code_text = ' '.join(code_lines)
        return any(pattern in code_text for pattern in config_patterns)
    
    def _extract_config_term(self, code_line: str) -> str:
        """Extract term for configuration parameters."""
        # Extract parameter name from YAML/config format
        if ':' in code_line:
            param = code_line.split(':')[0].strip()
            return f'`{param}`'
        elif '=' in code_line:
            param = code_line.split('=')[0].strip()
            return f'`{param}`'
        # Look for just the parameter name
        param = code_line.split()[0] if code_line.split() else code_line
        return f'`{param}`'
    
    def _extract_placeholder_term(self, code_line: str) -> str:
        """Extract term for user-replaceable placeholders."""
        # Look for <placeholder> format
        placeholder_match = re.search(r'<(\w+)>', code_line)
        if placeholder_match:
            return f'<{placeholder_match.group(1)}>'
        
        # Look for $variable format
        var_match = re.search(r'\$(\w+)', code_line)
        if var_match:
            return f'`${var_match.group(1)}`'
        
        # Look for method/function calls
        method_match = re.search(r'(\w+)\s*\(', code_line)
        if method_match:
            return f'`{method_match.group(1)}`'
        
        # Default to first significant token
        tokens = code_line.split()
        if tokens:
            return f'`{tokens[0]}`'
        return f'`{code_line[:30]}`'
    
    def _extract_code_term(self, code_line: str) -> str:
        """Extract term for code explanations."""
        # Look for variable assignments
        if '=' in code_line:
            var = code_line.split('=')[0].strip()
            return f'`{var}`'
        
        # Look for method calls
        method_match = re.search(r'(\w+)\s*\(', code_line)
        if method_match:
            return f'`{method_match.group(1)}`'
        
        # Use first meaningful part
        return f'`{code_line[:40]}`' if len(code_line) > 40 else f'`{code_line}`'


def process_directory(directory_path: str, output_dir: str = None, dry_run: bool = False):
    """Process all .adoc files in a directory."""
    directory = Path(directory_path)
    
    if not directory.exists():
        print(f"Error: Directory '{directory_path}' does not exist")
        return
    
    if not directory.is_dir():
        print(f"Error: '{directory_path}' is not a directory")
        return
    
    # Find all .adoc files
    adoc_files = list(directory.glob('**/*.adoc'))
    
    if not adoc_files:
        print(f"No .adoc files found in {directory_path}")
        return
    
    print(f"Found {len(adoc_files)} .adoc file(s)")
    
    remover = CalloutRemover()
    processed_count = 0
    error_count = 0
    
    for adoc_file in adoc_files:
        try:
            print(f"Processing: {adoc_file}")
            
            with open(adoc_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file has callouts
            if not re.search(r'<\d+>', content):
                print(f"  ⊘ No callouts found, skipping")
                continue
            
            result = remover.process_file(content)
            
            if dry_run:
                print(f"  ✓ Would process (dry-run mode)")
            else:
                # Determine output path
                if output_dir:
                    output_path = Path(output_dir) / adoc_file.name
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                else:
                    output_path = adoc_file
                
                # Write result
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(result)
                
                print(f"  ✓ Processed successfully")
            
            processed_count += 1
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
            error_count += 1
    
    print(f"\nSummary:")
    print(f"  Processed: {processed_count}")
    print(f"  Errors: {error_count}")
    print(f"  Total files: {len(adoc_files)}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file: python callout_remover.py <input_file> [output_file]")
        print("  Directory:   python callout_remover.py --dir <directory> [--output <output_dir>] [--dry-run]")
        print("\nOptions:")
        print("  --dir <directory>       Process all .adoc files in directory")
        print("  --output <output_dir>   Save processed files to output directory (default: overwrite originals)")
        print("  --dry-run               Show what would be processed without making changes")
        sys.exit(1)
    
    # Check if directory mode
    if '--dir' in sys.argv:
        dir_index = sys.argv.index('--dir')
        if dir_index + 1 >= len(sys.argv):
            print("Error: --dir requires a directory path")
            sys.exit(1)
        
        directory = sys.argv[dir_index + 1]
        output_dir = None
        dry_run = '--dry-run' in sys.argv
        
        if '--output' in sys.argv:
            output_index = sys.argv.index('--output')
            if output_index + 1 < len(sys.argv):
                output_dir = sys.argv[output_index + 1]
        
        process_directory(directory, output_dir, dry_run)
    else:
        # Single file mode
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            remover = CalloutRemover()
            result = remover.process_file(content)
            
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(result)
                print(f"Processed file written to: {output_file}")
            else:
                print(result)
        
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found")
            sys.exit(1)
        except Exception as e:
            print(f"Error processing file: {e}")
            sys.exit(1)


if __name__ == '__main__':
    main()

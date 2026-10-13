import os
import sys
import tomllib
from docx import Document
from ansi_colors import Colors
from parse_arguments import parse_args
from replace_docx_paragraphs import replace_by_text_match_and_para_no

def main():
    cli_args = parse_args()
    
    print(f"Applying changes made to {Colors.BLUE}{cli_args.infile}{Colors.RESET} "
        f"using the configuration found in {Colors.MAGENTA}{cli_args.config}{Colors.RESET} "
        f"to {Colors.BLUE}{cli_args.outfile}{Colors.RESET}\n")
    
    doc = Document(cli_args.infile)
    
    CONFIG_FILE_PATH = cli_args.config
    # Open and parse the TOML config file
    with open(CONFIG_FILE_PATH, "rb") as file:
        config = tomllib.load(file)
    
    # Initial line break
    print(
        f"{Colors.MAGENTA}", 
        '\t', 
        '-' * 30, 
        '\t', 
        '-' * 30, 
        '\t', 
        '-' * 30, 
        f"{Colors.RESET}"
        )
    
    for param, attr in config.items(): 
        print(f"{Colors.CYAN}Processing{Colors.RESET} {param} ...")
        
        replace_by_text_match_and_para_no(
            doc, 
            search_text=attr["text_to_match"], 
            new_text=attr["modified_text"], 
            start_idx=attr["index_start"], 
            end_idx=attr["index_end"], 
            fmt=attr["fmt"], 
            output_path=cli_args.outfile
            )
        
        # Line break per edit
        print(
            f"{Colors.MAGENTA}", 
            '\t', 
            '-' * 30, 
            '\t', 
            '-' * 30, 
            '\t', 
            '-' * 30, 
            f"{Colors.RESET}"
            )
    
    return 0
    
if __name__ == "__main__":
    sys.exit(main())
from docx import Document
from docx.shared import Pt

from ansi_colors import Colors

def replace_by_text_match_and_para_no(doc, search_text, new_text, start_idx, end_idx, fmt, output_path):
    total_paragraphs = len(doc.paragraphs)
    
    # Ensure our search window stays within document bounds
    start = max(0, start_idx)
    end = min(total_paragraphs, end_idx)
    
    found = False
    
    print(f"{Colors.CYAN}Searching{Colors.RESET} for '{search_text[:15]}...' between index {Colors.BLUE}{start}{Colors.RESET} and {Colors.BLUE}{end}{Colors.RESET}...")

    # Iterate only through the specified window
    for i in range(start, end):
        para = doc.paragraphs[i]
        
        if search_text.lower() in para.text.lower():
            print(f"{Colors.GREEN}Match found{Colors.RESET} at {Colors.BLUE}paragraph {i}{Colors.RESET}: '{Colors.RED}{para.text[:30]}{Colors.RESET}...'")
            print(f"{Colors.YELLOW}Replacing{Colors.RESET} text...")
            
            # Update the text while preserving basic paragraph style
            # para.text = new_text 
            
            para.clear()  # remove existing runs

            run = para.add_run(new_text)

            # Apply formatting from tuple
            if "font_name" in fmt:
                run.font.name = fmt["font_name"]

            if "font_size" in fmt:
                run.font.size = Pt(fmt["font_size"])

            if "bold" in fmt:
                run.bold = fmt["bold"]
            
            if "italic" in fmt:
                run.italic = fmt["italic"]

            if "underline" in fmt:
                run.underline = fmt["underline"]
            
            found = True
            # Break if you only want to change the FIRST match in this area
            break 

    if found:
        print(f"Saving changes to {output_path}")
        doc.save(output_path)
        print(f"{Colors.GREEN}Save Complete{Colors.RESET}")
    else:
        print(f"{Colors.RED}No match found{Colors.RESET} in the specified range.\n")
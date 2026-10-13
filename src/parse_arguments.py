import argparse
from pathlib import Path

def parse_args():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(
      description=(
          "A command-line tool to edit out personal data from a docx file parameter."
      )
    )

    # Define the parameters
    parser.add_argument(
      "--infile", type=Path, required=True, help="The input docx file"
    )
    parser.add_argument(
      "--config", type=Path, required=True, help="The location of configuration file"
    )
    parser.add_argument(
      "--outfile", type=Path, required=True, help="The output docx file"
    )

    # Parse the arguments from the command line
    args = parser.parse_args()

    return args
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Count words in files.")
    parser.add_argument(
        "-i",
        "--input",
        help="Path to the input folder containing files to process",
        default="data/input/",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Path to the output folder for results",
        default="data/output/",
    )

    # Ignore any unknown arguments (e.g., pytest flags) and only parse known ones
    parsed_args, _ = parser.parse_known_args()
    return parsed_args.input, parsed_args.output


def main():
    input_folder, output_folder = parse_args()

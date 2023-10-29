from generator.grammar_parser import GrammarParser
from generator.program_builder import ProgramBuilder
import os

def main():
    # Ensure the output directory exists
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Parse the grammar
    parser = GrammarParser()
    grammar_structure = parser.parse_grammar()

    if not grammar_structure:
        print("Failed to parse grammar. Exiting program.")
        return

    # Build the program
    builder = ProgramBuilder(grammar_structure)
    generated_program = builder.build_program()

    if not generated_program:
        print("Failed to generate program. Exiting program.")
        return

    # Output the generated program
    print("Generated Program:")
    print("-------------------")
    # print(grammar_structure)
    print(generated_program)

    # Save the generated program to a file in the output directory
    output_file = os.path.join(output_dir, "generated_program_1.py")
    with open(output_file, "w") as file:
        file.write(generated_program)
    print(f"Generated program saved as '{output_file}'")

if __name__ == "__main__":
    main()

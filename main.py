from generator.grammar_parser import GrammarParser
from generator.program_builder import ProgramBuilder
import os

def main():
    # Load and parse the predefined grammar
    grammar_parser = GrammarParser()
    grammar_structure = grammar_parser.parse_grammar()

    # Generate the program based on the parsed grammar
    program_builder = ProgramBuilder(grammar_structure)
    generated_code = program_builder.build_program()

    # Create the output folder if it doesn't exist
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the generated program in the output folder
    with open(os.path.join(output_dir, "generated_program.py"), "w") as file:
        file.write(generated_code)

    print("Program generated successfully.")

if __name__ == "__main__":
    main()

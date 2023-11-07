import json

class GrammarParser:
    def __init__(self):
        self.grammar_file = "utils/templates/grammar/basic_remote.json"
    
    def parse_grammar(self):
        # Read the JSON file containing the grammar
        try:
            with open(self.grammar_file, 'r') as file:
                grammar_structure = json.load(file)
            return grammar_structure
        except FileNotFoundError:
            print(f"Grammar file not found at {self.grammar_file}.")
            return {}
        except json.JSONDecodeError:
            print(f"Error parsing JSON from {self.grammar_file}.")
            return {}

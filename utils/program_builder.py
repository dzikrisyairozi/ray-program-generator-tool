import random
import re

class ProgramBuilder:
    def __init__(self, grammar_structure):
        self.grammar_structure = grammar_structure
        self.context = {}  # Context to maintain consistency
        self.argument_vars = set()  # Track variables for arguments
        self.function_arg_count = {}  # Track number of arguments for each function

    def build_program(self):
        # Starting point for building the program
        generated_code = self.generate_code("Starting_rule")
        return generated_code

    def generate_code(self, current_rule):
        if current_rule not in self.grammar_structure:
            return current_rule + " "

        rule_options = self.grammar_structure[current_rule]
        chosen_option = random.choice(rule_options)
        generated = ""

        for part in chosen_option:
            if part.startswith("t_"):
                generated += self.generate_token(part, current_rule)
            else:
                generated += self.generate_code(part)

        # Clear argument variables after generating a function
    # After generating a function, reset argument variables
        if current_rule == "Ray_Remote_Function":
            self.function_arg_count[self.context.get("t_function_name", "")] = len(self.argument_vars)
            self.argument_vars.clear()

        # Handle dynamic function calls
        if current_rule == "Dynamic_Function_Call":
            func_name = self.context.get("t_function_name", "")
            arg_count = self.function_arg_count.get(func_name, 1)
            return self.generate_dynamic_function_call(func_name, arg_count)

        
        return generated
    
    
    def generate_dynamic_function_call(self, func_name, arg_count):
        args = ['i']
        if arg_count > 1:
            args.append(str(random.randint(1, 10)))  # Add a second argument if needed
        args_str = ', '.join(args)
        return f"{func_name}.remote({args_str}) "
    


    def generate_token(self, token_name, current_rule):
        if token_name == "t_new_line":
            return "\n"
        elif token_name == "t_tab":
            return "    "  # Four spaces for a tab
        elif token_name == "t_equals":
            return "="  # Four spaces for a tab
        elif token_name == "t_variable" and current_rule == "Arguments_list":
            return self.generate_argument_variable()
        elif token_name == "t_expression":
            return self.generate_expression()
        elif token_name in ["t_function_name", "t_var_declaration"]:
            return self.context.setdefault(token_name, self.generate_new_token(token_name))
        else:
            return self.generate_new_token(token_name)

    def generate_new_token(self, token_name):
        token_regex = self.grammar_structure["Tokens"].get(token_name)
        if token_regex:
            generated_token = self.random_string_matching_regex(token_regex)
            return generated_token + " "
        else:
            return token_name + " "
    
       
    def generate_argument_variable(self):
        # Generate and add a new argument variable only if less than two arguments exist
        if len(self.argument_vars) < 2:
            var_name = "var" + str(random.randint(0, 10))
            while var_name in self.argument_vars:  # Ensure unique names
                var_name = "var" + str(random.randint(0, 10))
            self.argument_vars.add(var_name)
            return var_name + " "
        else:
            return ""

    def generate_expression(self):
        arg_list = list(self.argument_vars)
        if len(arg_list) >= 2:
            # Randomly select two different arguments
            var1, var2 = random.sample(arg_list, 2)
            return f"{var1} * {var2} "
        elif len(arg_list) == 1:
            # Use the single argument twice if only one is available
            return f"{arg_list[0]} * {arg_list[0]} "
        return "example "

    @staticmethod
    def random_string_matching_regex(regex):
        if regex == "\\d+":
            return str(random.randint(0, 10))
        elif regex == "[a-zA-Z_][a-zA-Z0-9_]*":
            return "var" + str(random.randint(0, 10))
        return "example"

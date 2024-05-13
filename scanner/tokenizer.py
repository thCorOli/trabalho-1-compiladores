from scanner.Automato import Automato

class Scanner:

    def __init__(self):
        pass
    
    def scan_gen(token_specs):
        automata = [Automato(name, pattern) for name, pattern in token_specs]

        def tokenizer(input_string):
            tokens = []
            input_string += ' '  
            last_match_end = 0  

            for i in range(len(input_string)):
                matched_this_round = False
                for automaton in automata:
                    automaton.reset()
                    for j in range(i, len(input_string)):
                        if not automaton.match(input_string[j]):
                            break
                    if automaton.current:
                        if j > last_match_end:  
                            last_match_end = j
                            longest_match = automaton.get_token()
                            match_start_position = i
                            matched_this_round = True

                if matched_this_round and i == match_start_position:
                    tokens.append(longest_match)
                    i = last_match_end - 1  

            return tokens

        return tokenizer

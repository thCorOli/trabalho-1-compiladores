from scanner.Automato import Automato
class Scanner:
    @staticmethod
    def scan_gen(token_specs):
        automata = [Automato(name, pattern, is_keyword) for name, pattern, is_keyword in token_specs]

        def tokenizer(input_string):
            tokens = []
            i = 0
            while i < len(input_string):
                matched = False
                for automaton in automata:
                    result = automaton.match(input_string[i:])
                    if result:
                        tokens.append((automaton.name, result))
                        i += len(result) 
                        matched = True
                        break
                if not matched:
                    i += 1  

            return tokens
        return tokenizer

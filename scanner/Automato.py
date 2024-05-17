import re

class Automato:
    def __init__(self, name, pattern, is_keyword=False):
        self.name = name
        self.pattern = re.compile(pattern)
        self.is_keyword = is_keyword
        self.reset()

    def reset(self):
        self.current = ''
        self.is_final = False

    def match(self, text):
        # Usamos match para verificar o início do texto
        m = self.pattern.match(text)
        if m:
            return m.group(0)  # Retorna a correspondência exata
        return None


    def get_token(self):
        if self.is_final:
            token = (self.name, self.current.strip())
            self.reset()
            return token
        return None
    
    def build_simple_automaton(self):
        current_state = 0
        for i, char in enumerate(self.pattern):
            next_state = current_state + 1
            if char.isalnum() or char in ['+', '*', '?', '-', '[', ']', '(', ')']:
                self.transitions.append((current_state, next_state, char))
            elif char == '.':
                self.transitions.append((current_state, next_state, 'ANY'))
            current_state = next_state
        self.states = list(range(current_state + 1))

    def display(self):
        print(f"Automaton: {self.name}")
        print("States:", self.states)
        print("Transitions:")
        for from_state, to_state, symbol in self.transitions:
            print(f"{from_state} -> {to_state} on '{symbol}'")



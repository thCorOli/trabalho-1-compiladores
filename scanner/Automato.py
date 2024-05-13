import re

class Automato:
    def __init__(self, name, pattern):
        self.name = name
        self.pattern = re.compile(pattern)
        self.reset()
        self.states = []
        self.transitions = []

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


    def reset(self):
        self.current = ''

    def match(self, char):
        test_string = self.current + char
        if re.fullmatch(self.pattern, test_string):
            self.current = test_string
            return True
        return False

    def get_token(self):
        token = (self.name, self.current)
        self.reset()  
        return token

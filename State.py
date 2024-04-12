class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}  # Symbol -> set of States

    def add_transition(self, symbol, next_states):
        if symbol in self.transitions:
            self.transitions[symbol].update(next_states)
        else:
            self.transitions[symbol] = set(next_states)

    def __str__(self):
        return f"State({self.name})"

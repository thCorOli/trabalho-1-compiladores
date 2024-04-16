class State:
    def __init__(self, is_accept_state=False):
        self.is_accept_state = is_accept_state
        self.transitions = {}  # key: symbol, value: set of states

    def add_transition(self, symbol, state):
        if symbol in self.transitions:
            self.transitions[symbol].add(state)
        else:
            self.transitions[symbol] = {state}

    def get_transitions(self, symbol):
        return self.transitions.get(symbol, set())

    def __str__(self):
        return f"State({id(self)}, Accept={self.is_accept_state})"

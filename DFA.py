from State import State

class DFA:
    def __init__(self):
        self.start_state = State()
        self.states = {self.start_state}

    @staticmethod
    def from_nfa(nfa):
        # Implement the subset construction algorithm here
        pass

    def minimize(self):
        # Implement DFA minimization here
        pass

    def __str__(self):
        return "DFA with states: " + ", ".join(str(s) for s in self.states)

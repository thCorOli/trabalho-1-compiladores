class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, symbol, state):
        if symbol in self.transitions:
            self.transitions[symbol].add(state)
        else:
            self.transitions[symbol] = {state}
    
    def getState(self):
        return self.list_states
    
    def setState(cls, content: str ):
        cls.list_states = content

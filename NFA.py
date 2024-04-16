from State import State

class NFA:
    def __init__(self):
        self.start_state = State()
        self.states = {self.start_state}

    def add_state(self, is_accept_state=False):
        new_state = State(is_accept_state)
        self.states.add(new_state)
        return new_state

    def add_transition(self, from_state, symbol, to_state):
        from_state.add_transition(symbol, to_state)

    def epsilon_closure(self, states):
        closure = set(states)
        stack = list(states)
        while stack:
            state = stack.pop()
            for next_state in state.get_transitions(None):  # None represents epsilon
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure

    def move(self, states, symbol):
        result = set()
        for state in states:
            result.update(state.get_transitions(symbol))
        return result

    def to_dfa(self):
        from DFA import DFA
        return DFA.from_nfa(self)

    def __str__(self):
        return "NFA with states: " + ", ".join(str(s) for s in self.states)

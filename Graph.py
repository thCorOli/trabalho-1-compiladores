from State import State

class Graph:
    def __init__(self):
        self.start_state = None
        self.accept_states = set()
        self.transitions = []

    def add_transition(self, transition):
        self.transitions.append(transition)

    def set_start_state(self, state):
        self.start_state = state

    def add_accept_state(self, state):
        self.accept_states.add(state)
        
    def get_transitions(self):
        return self.transitions
    
    def display(self):
        print("NFA States and Transitions:")
        for state in self.transitions:
            for symbol, next_states in state.transitions.items():
                for next_state in next_states:
                    print(f"State {state.name} --{symbol}--> State {next_state.name}")
        print(f"Start State: {self.start_state.name}")
        print("Accept States:", ", ".join(str(state.name) for state in self.accept_states))

    def regex_to_afn(self,regex):
        start_state = State(0)
        self.graph.set_start_state(start_state)
        current_state = start_state
        state_count = 1
        for char in regex:
            if char == '*':
                current_state.add_transition('ε', start_state)
            else:
                new_state = State(state_count)
                state_count += 1
                current_state.add_transition(char, new_state)
                current_state = new_state
        self.graph.add_accept_state(current_state)
        print("AQUI",self.graph.display())
        return self.graph
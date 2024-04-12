class Graph:
    def __init__(self):
        self.states = []
        self.start_state = None
        self.accept_states = set()

    def add_state(self, state):
        self.states.append(state)
        return state

    def add_accept_state(self, state):
        self.accept_states.add(state)

    def display(self):
        print("Autômato Finito Não Determinístico:")
        for state in self.states:
            for symbol, next_states in state.transitions.items():
                for next_state in next_states:
                    print(f"  {state.name} --{symbol}--> {next_state.name}")
        print(f"Estado inicial: {self.start_state.name}")
        accept_states = ', '.join(str(state.name) for state in self.accept_states)
        print(f"Estados de aceitação: {accept_states}")

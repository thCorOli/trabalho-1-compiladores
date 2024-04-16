class State:
    _id_counter = 0  # Contador estático para gerar IDs únicos para cada estado

    def __init__(self, is_accept_state=False):
        self.id = State._id_counter
        State._id_counter += 1  # Incrementa o contador cada vez que um estado é criado
        self.name = f"State{self.id}"
        self.is_accept_state = is_accept_state
        self.transitions = {}  # key: symbol, value: set of states

    def add_transition(self, symbol, state):
        if symbol is None:
            symbol = 'ε'  # Usando 'ε' para transições epsilon
        if symbol in self.transitions:
            self.transitions[symbol].add(state)
        else:
            self.transitions[symbol] = {state}

    def get_transitions(self, symbol):
        if symbol is None:
            symbol = 'ε'
        return self.transitions.get(symbol, set())

    def __str__(self):
        transitions = {symb: ','.join(state.name for state in states) for symb, states in self.transitions.items()}
        transitions_str = ', '.join(f"{symb}: [{st}] " for symb, st in transitions.items())
        return f"{self.name} ({'Accept' if self.is_accept_state else 'Non-Accept'}) -> {transitions_str if transitions_str else 'No Transitions'}"

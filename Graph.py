from State import State

class Graph:
    def __init__(self):
        self.start_state =  None
        self.accept_states = []
        self.transitions = []

    def add_transition(self, transition):
        self.transitions.append(transition)

    def add_epsilon_transition(self, state, next_state):
        epsilon = 'ε'
        state.add_transition(epsilon, next_state)
        self.add_transition((state, (epsilon, next_state)))

    def set_start_state(self, state):
        self.start_state = state

    def add_accept_state(self, state):
        self.accept_states.append(state)
        
    def get_transitions(self):
        return self.transitions
    
    def config_graph(self):
        self.start_state = State(0)
        self.set_start_state(self.start_state)
        
    
    def regex_to_afn(self, current_state, regex):
        state_count = current_state.name + 1
        pos = 1
        while pos < len(regex):
            char = regex[pos]
            if char == '[':
                # Tratar conjunto [...]
                pos += 1
                tool = ""
                while pos < len(regex) and regex[pos] != ']':
                    tool += regex[pos]
                    pos += 1
                if pos < len(regex):
                    pos += 1  # Avança para o próximo caractere após ']'
                    next_state = State(state_count)
                    state_count += 1
                    current_state.add_transition(tool, next_state)
                    self.add_transition((current_state, (tool, next_state)))
                    current_state = next_state
            elif char == '(':
                # Tratar grupo (...)
                pos += 1
                sub_expression = ""
                while pos < len(regex) and regex[pos] != ')':
                    sub_expression += regex[pos]
                    pos += 1
                if pos < len(regex):
                    pos += 1  # Avança para o próximo caractere após ')'
                    # Chamada recursiva para processar o conteúdo dentro dos parênteses
                    current_state = self.regex_to_afn(current_state, sub_expression)
                elif char == '\\':
                # Lidar com o caso de escape
                    pos += 1
                    if pos < len(regex):
                        next_state = State(state_count)
                        state_count += 1
                        current_state.add_transition(regex[pos], next_state)
                        self.add_transition((current_state, (regex[pos], next_state)))
                        current_state = next_state
                        pos += 1
                elif char == '*':
                        # Lidar com o quantificador *
                        prev_state = current_state
                        current_state = State(state_count)
                        state_count += 1
                        prev_state.add_epsilon_transition(current_state)
                        self.add_transition((prev_state, ('ε', current_state)))  # Adiciona uma transição epsilon
                        pos += 1
                elif char == '+':
                        # Lidar com o quantificador +
                        prev_state = current_state
                        current_state = State(state_count)
                        state_count += 1
                        prev_state.add_epsilon_transition(current_state)
                        self.add_transition((prev_state, ('ε', current_state)))  # Adiciona uma transição epsilon
                        pos += 1
            else:
                # Caractere normal
                next_state = State(state_count)
                state_count += 1
                current_state.add_transition(char, next_state)
                self.add_transition((current_state, (char, next_state)))
                current_state = next_state
                pos += 1
        return current_state


    def display(self):
        print("NFA States and Transitions:")
        visited = set()  # Para evitar imprimir transições repetidas
        for transition in self.transitions:
            state, (symbol, next_state) = transition
            if state not in visited:
                visited.add(state)
                for symbol, next_states in state.transitions.items():
                    for next_state in next_states:
                        print(f"State {state.name} --{symbol}--> State {next_state.name}")
        print(f"Start State: {self.start_state.name}")
        print("Accept States:", ", ".join(str(state.name) for state in self.accept_states))
        
        

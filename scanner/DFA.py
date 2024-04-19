from State import State
from collections import deque, defaultdict

class DFA:
    def __init__(self):
        self.start_state = None
        self.states = set()

    def add_state(self, is_accept_state=False):
        new_state = State(is_accept_state=is_accept_state)
        self.states.add(new_state)
        return new_state

    def set_start_state(self, state):
        self.start_state = state
        self.states.add(state)

    def add_transition(self, from_state, symbol, to_state):
        from_state.add_transition(symbol, to_state)

    def __str__(self):
        return "\n".join(str(state) for state in sorted(self.states, key=lambda x: x.name))

    def from_nfa(nfa):
        dfa = DFA()
        initial_closure = nfa.epsilon_closure({nfa.start_state})
        state_map = {frozenset(initial_closure): dfa.add_state(is_accept_state=any(s.is_accept_state for s in initial_closure))}
        dfa.set_start_state(state_map[frozenset(initial_closure)])
        
        worklist = deque([frozenset(initial_closure)])
        seen = set(worklist)

        while worklist:
            current = worklist.popleft()
            # Mapear transições de todos os estados no conjunto NFA
            transitions = defaultdict(set)
            for state in current:
                for symbol, states in state.transitions.items():
                    if symbol != 'ε':  # Ignorar transições epsilon
                        transitions[symbol].update(nfa.epsilon_closure(states))

            # Para cada símbolo, criar um novo estado no DFA se necessário
            for symbol, states in transitions.items():
                state_set = frozenset(states)
                if state_set not in state_map:
                    is_accept = any(s.is_accept_state for s in states)
                    state_map[state_set] = dfa.add_state(is_accept_state=is_accept)
                    if state_set not in seen:
                        worklist.append(state_set)
                        seen.add(state_set)
                dfa.add_transition(state_map[current], symbol, state_map[state_set])

        return dfa

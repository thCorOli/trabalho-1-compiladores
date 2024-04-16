from NFA import NFA
from State import State

def basic_nfa(char_range):
    start = State()
    accept = State(is_accept_state=True)
    if '-' in char_range:
        start_range, end_range = char_range.split('-')
        for char_code in range(ord(start_range), ord(end_range) + 1):
            char = chr(char_code)
            start.add_transition(char, accept)
    else:
        start.add_transition(char_range, accept)
    nfa = NFA()
    nfa.start_state = start
    nfa.states.add(start)
    nfa.states.add(accept)
    return nfa

def star(nfa):
    start = State()
    accept = State(is_accept_state=True)
    start.add_transition(None, nfa.start_state)  # Epsilon transition to original start
    start.add_transition(None, accept)          # Epsilon transition to new accept state
    for state in nfa.states:
        if state.is_accept_state:
            state.add_transition(None, nfa.start_state)  # Epsilon back to start of NFA
            state.add_transition(None, accept)          # Epsilon to new accept state
            state.is_accept_state = False
    nfa.start_state = start
    nfa.states.update({start, accept})
    return nfa

def plus(nfa):
    start = State()
    accept = State(is_accept_state=True)
    start.add_transition(None, nfa.start_state)
    for state in nfa.states:
        if state.is_accept_state:
            state.add_transition(None, nfa.start_state)
            state.add_transition(None, accept)
            state.is_accept_state = False
    nfa.start_state = start
    nfa.states.update({start, accept})
    return nfa

def optional(nfa):
    start = State()
    accept = State(is_accept_state=True)
    start.add_transition(None, nfa.start_state)
    start.add_transition(None, accept)
    for state in nfa.states:
        if state.is_accept_state:
            state.add_transition(None, accept)
            state.is_accept_state = False
    nfa.start_state = start
    nfa.states.update({start, accept})
    return nfa

def concatenate(nfa1, nfa2):
    for state in nfa1.states:
        if state.is_accept_state:
            state.add_transition(None, nfa2.start_state)  # Epsilon transition to the start of the second NFA
            state.is_accept_state = False  # Turn off acceptance of concatenated state
    nfa1.states.update(nfa2.states)
    return nfa1

def union(nfa1, nfa2):
    start = State()
    accept = State(is_accept_state=True)
    start.add_transition(None, nfa1.start_state)
    start.add_transition(None, nfa2.start_state)
    for state in nfa1.states.union(nfa2.states):
        if state.is_accept_state:
            state.add_transition(None, accept)
            state.is_accept_state = False
    nfa1.start_state = start
    nfa1.states.update(nfa2.states)
    nfa1.states.update({start, accept})
    return nfa1

def regex_to_nfa(regex):
    """ Converts a regular expression to an NFA using Thompson's construction. """
    stack = []
    i = 0
    while i < len(regex):
        if regex.startswith('[A-z]', i):
            # Assuming we're working with [A-z]
            char_nfa = basic_nfa('A-z')
            if i + 5 < len(regex) and regex[i+5] == '*':
                char_nfa = star(char_nfa)
                i += 1  # Skip the '*' character
            stack.append(char_nfa)
            i += 4  # Skip the '[A-z]'
        i += 1
    return stack.pop() if stack else None
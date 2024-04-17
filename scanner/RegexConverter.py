from NFA import NFA
from State import State
import re

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
        if regex[i] == '[':
            # Encontrar o fechamento do colchete
            end = regex.find(']', i)
            if end == -1:
                raise ValueError("Unmatched '[' in regex")
            # Interpretar o conteúdo dentro dos colchetes
            char_range = regex[i+1:end]
            if '-' in char_range:
                start_char, end_char = char_range.split('-')
                nfa = basic_nfa(f'{start_char}-{end_char}')
            else:
                nfa = basic_nfa(char_range)

            # Verificar se o próximo caractere é um operador de repetição
            if end + 1 < len(regex) and regex[end+1] in '*+?':
                if regex[end+1] == '*':
                    nfa = star(nfa)
                elif regex[end+1] == '+':
                    nfa = plus(nfa)
                elif regex[end+1] == '?':
                    nfa = optional(nfa)
                end += 1  # Avançar o índice para pular o operador de repetição

            stack.append(nfa)
            i = end + 1  # Avançar o índice para continuar após o colchete fechado e operador
        else:
            # Tratar caracteres e operadores individuais
            if regex[i] in '*+?|':
                # Aplicar operadores sobre o último NFA na pilha
                if regex[i] == '*':
                    nfa = star(stack.pop())
                elif regex[i] == '+':
                    nfa = plus(stack.pop())
                elif regex[i] == '?':
                    nfa = optional(stack.pop())
                elif regex[i] == '|':
                    nfa2 = stack.pop()
                    nfa1 = stack.pop()
                    nfa = union(nfa1, nfa2)
                stack.append(nfa)
            else:
                # Tratar caracteres individuais que não são metacaracteres
                stack.append(basic_nfa(regex[i]))
            i += 1

    # Resolver concatenações implícitas
    while len(stack) > 1:
        nfa2 = stack.pop()
        nfa1 = stack.pop()
        stack.append(concatenate(nfa1, nfa2))

    return stack.pop() if stack else None
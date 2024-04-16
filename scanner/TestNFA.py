import unittest
from RegexConverter import regex_to_nfa

def accepts(nfa, string):
    # Começa com a clausura epsilon do estado inicial
    current_states = nfa.epsilon_closure({nfa.start_state})

    # Processa cada caractere da string
    for char in string:
        # Move para o próximo conjunto de estados
        next_states = set()
        for state in current_states:
            # Pega os estados alcançáveis pelo caractere atual
            if char in state.transitions:
                next_states.update(state.transitions[char])
        
        # Aplica a clausura epsilon a cada estado alcançado
        current_states = nfa.epsilon_closure(next_states)

    # Verifica se algum dos estados finais é um estado de aceitação
    return any(state.is_accept_state for state in current_states)

class TestNFA(unittest.TestCase):

    def test_basic_nfa_acceptance(self):
        # Criar NFA para a expressão [A-z]*
        nfa = regex_to_nfa('[A-z]*')

        # Testar strings que deveriam ser aceitas
        self.assertTrue(accepts(nfa, "Abc"))
        self.assertTrue(accepts(nfa, "XYZ"))
        self.assertTrue(accepts(nfa, ""))  # Vazio deve ser aceito, pois * permite repetição zero

        # Testar strings que não deveriam ser aceitas
        self.assertFalse(accepts(nfa, "123"))  # Dígitos não são permitidos
        self.assertFalse(accepts(nfa, "abc123"))  # Dígitos misturados com letras

if __name__ == '__main__':
    unittest.main()

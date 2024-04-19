from RegexConverter import regex_to_nfa
from NFA import NFA

def main():
    regex = "[0-9]*"
    nfa = regex_to_nfa(regex)
    print(nfa)
    print("NFA -> DFA")
    dfa = NFA.to_dfa(nfa)
    print(dfa)

if __name__ == "__main__":
    main()
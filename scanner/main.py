from RegexConverter import regex_to_nfa
from NFA import NFA

def main():
    regex = "[A-z]"
    nfa = regex_to_nfa(regex)
    print(nfa)

if __name__ == "__main__":
    main()
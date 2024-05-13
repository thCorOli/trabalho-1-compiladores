from RegexConverter import regex_to_nfa
from NFA import NFA

def main():
<<<<<<< HEAD
    regex = "[int]"
    nfa = regex_to_nfa(regex)
    print(nfa)
    
=======
    regex = "[A-z][0-9]*"
    nfa = regex_to_nfa(regex)
    print(nfa)
>>>>>>> c1a03cc446ad533974128d70dbf347d454fbe676

if __name__ == "__main__":
    main()
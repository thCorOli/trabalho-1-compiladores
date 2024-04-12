from RegexParser import RegexParser

if __name__ == "__main__":
    regex = "(a|b)*abb"
    parser = RegexParser(regex)
    parser.parse()
    parser.graph.display()
from Graph import Graph
graph = Graph()

if __name__ == '__main__':
    graph.regex_to_afn("([A-z]|[0-9])+@([A-z]|[0-9])+.com")
    graph.display()
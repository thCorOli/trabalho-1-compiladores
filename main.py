from Graph import Graph
graph = Graph()

if __name__ == '__main__':
    graph.config_graph()
    graph.regex_to_afn(graph.start_state,"([A-z]|[0-9])+@([A-z]|[0-9])+.com")
    graph.display()
from Graph import Graph
from State import State

class RegexParser:
    def __init__(self, regex):
        self.regex = self.preprocess_regex(regex)
        self.graph = Graph()
        self.state_count = 0

    def preprocess_regex(self, regex):
        output = []
        special_chars = {'|', '*', '+', '?', '(', ')'}
        for i, char in enumerate(regex):
            if i > 0 and regex[i - 1] not in special_chars and char not in special_chars.union({'('}):
                output.append('.')
            output.append(char)
        return ''.join(output)

    def create_state(self):
        state = State(self.state_count)
        self.graph.add_state(state)
        self.state_count += 1
        return state

    def parse(self):
        if not self.regex:
            return
        self.graph.start_state = self.create_state()
        self.parse_regex(self.regex, 0, len(self.regex), self.graph.start_state, None)

    def handle_parentheses(self, pattern, i, end, current_state, parent_state):
        count = 1
        j = i + 1
        while j < end and count > 0:
            if pattern[j] == '(':
                count += 1
            elif pattern[j] == ')':
                count -= 1
            j += 1
        sub_end_state = self.create_state()
        self.parse_regex(pattern, i + 1, j - 1, current_state, sub_end_state)
        return j, sub_end_state

    def handle_alternation(self, pattern, start, i, end, current_state, parent_state):
        alt_end_state = self.create_state()
        if parent_state is None:
            parent_state = self.create_state()
        self.parse_regex(pattern, start, i, current_state, parent_state)
        self.parse_regex(pattern, i + 1, end, current_state, parent_state)
        return alt_end_state

    def handle_star(self, i, current_state):
        loop_start = current_state
        loop_end = self.create_state()
        loop_start.add_transition('ε', {loop_end})
        self.parse_regex(self.regex, i + 1, i + 2, loop_start, loop_end)
        loop_end.add_transition('ε', {loop_start})
        return i + 1, loop_end

    def handle_plus(self, i, current_state):
        loop_start = current_state
        loop_end = self.create_state()
        self.parse_regex(self.regex, i + 1, i + 2, loop_start, loop_end)
        loop_end.add_transition('ε', {loop_start})
        return i + 1, loop_end

    def handle_optional(self, i, current_state):
        optional_end = self.create_state()
        current_state.add_transition('ε', {optional_end})
        self.parse_regex(self.regex, i + 1, i + 2, current_state, optional_end)
        return i + 1, optional_end

    def parse_regex(self, pattern, start, end, current_state, parent_state):
        i = start
        while i < end:
            if pattern[i] == '(':
                i, current_state = self.handle_parentheses(pattern, i, end, current_state, parent_state)
            elif pattern[i] == '|':
                current_state = self.handle_alternation(pattern, start, i, end, current_state, parent_state)
                break
            elif pattern[i] == '*':
                i, current_state = self.handle_star(i, current_state)
            elif pattern[i] == '+':
                i, current_state = self.handle_plus(i, current_state)
            elif pattern[i] == '?':
                i, current_state = self.handle_optional(i, current_state)
            else: 
                if pattern[i] != '.':
                    next_state = self.create_state()
                    current_state.add_transition(pattern[i], {next_state})
                    current_state = next_state
                i += 1

        if parent_state:
            current_state.add_transition('ε', {parent_state})
        else:
            self.graph.add_accept_state(current_state)

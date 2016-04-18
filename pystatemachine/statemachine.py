import networkx as nx
import matplotlib.pyplot as plt

class StateMachine:
    def __init__(self):
        self.network = nx.DiGraph()
        self.handlers = {}
        self.start_state = None
        self.end_states = []

    def add_state(self, name, handler, end_state = False):
        name = name.upper()
        self.handlers[name] = handler
        self.network.add_node(name)
        if end_state:
            self.end_states.append(name)

    def add_transition(self, source, sink, event):
        source = source.upper()
        sink = sink.upper()
        self.network.add_edge((source, sink))

    def set_start(self, name):
        self.start_state = name.upper()

    def show(self):
        nx.draw(self.network)
        plt.show()

    def save(self, name):
        nx.draw(self.network)
        plt.savefig(name, bbox_inches="tight")

    def run(self, cargo):
        try:
            handler = self.handlers[self.start_state]
        except:
            raise InitializationError("must call .set_start() before .run()")
        if not self.end_states:
            raise  InitializationError("at least one state must be an end_state")

        while True:
            (new_state, cargo) = handler(cargo)
            if new_state.upper() in self.end_states:
                print "reached ", new_state
                break
            else:
                handler = self.handlers[new_state.upper()]

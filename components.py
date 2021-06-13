from dataclasses import dataclass
from typing import Optional


@dataclass
class Edge():
    name: str
    from_: int
    to_: int
    weight: int

    def __str__(self):
        return f"{self.name}: {self.from_},{self.to_} : {self.weight}"


@dataclass
class Graph:
    edges: Optional[list[Edge]] = None

    def get_edge(self, name):
        for edge in self.edges:
            if edge.name == name:
                return edge

    def add_edge(self, name, from_, to_, weight):
        self.edges.append(
            Edge(
                name=name,
                from_=from_,
                to_=to_,
                weight=weight
            )
        )

    def fill_graph(self,
                   values: list[int],
                   decisions: list[str],
                   weights: list[int]):
        current = 0

        for node in values[:-1]:
            # print(node, decisions[current])
            if node % 2:
                # print(current, decisions[current], weights[current])
                self.add_edge(decisions[current], node, node + 2,
                              weights[current])
                # print(node, decisions[current])
                current += 1
                # print(current, decisions[current], weights[current])
                if node != 7:
                    self.add_edge(decisions[current], node, node + 3,
                                  weights[current])
                    # print(node, decisions[current])
                    current += 1
            else:
                if node == 8:
                    self.add_edge(decisions[current], node, node + 1,
                                  weights[current])
                else:
                    # print(current, decisions[current], weights[current])
                    self.add_edge(decisions[current], node, node + 1,
                                  weights[current])
                    # print(node, decisions[current])
                    current += 1
                    # print(current, decisions[current], weights[current])

                    self.add_edge(decisions[current], node, node + 2,
                                  weights[current])
                    # print(node, decisions[current])
                    current += 1

        for edge in self.edges:
            print(edge)


@dataclass()
class GraphTrace:
    name: str
    weight: int

    def __add__(self, other):
        total_name = self.name + other.name
        total_weight = self.weight + other.weight
        return GraphTrace(total_name, total_weight)


if __name__ == "__main__":
    g = Graph([Edge("A", 1, 3, 8)])

    g.add_edge("B", 1, 4, 6)
    g.add_edge("C", 2, 3, 5)
    g.add_edge("D", 2, 4, 6)

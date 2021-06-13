from collections import defaultdict

from components import Graph, GraphTrace
from operator import attrgetter


def main():
    ...
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # możę dwa M ? a nie M N ?
    decisions = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
    weights = [
        8, 6, 5, 6, 7, 8, 6, 7, 5, 9, 6, 5, 5, 6
    ]

    graph = Graph([])
    graph.fill_graph(values, decisions, weights)
    stages = {
        "first_stage": graph.edges[:4],
        "second_stage": graph.edges[4:8],
        "third_stage": graph.edges[8:12],
        "fourth_stage": graph.edges[12:]
    }
    fourth_traces = []
    third_traces = []
    second_traces = []
    first_traces = []

    for edge in stages["fourth_stage"]:
        fourth_traces.append(GraphTrace(edge.name, edge.weight))

    for edge in stages["third_stage"]:
        # third_traces.append(GraphTrace(edge.name, edge.weight))
        for trace in fourth_traces:
            if graph.get_edge(trace.name[-1]).from_ == edge.to_:
                third_traces.append(trace + GraphTrace(edge.name, edge.weight))

    for edge in stages["second_stage"]:
        # third_traces.append(GraphTrace(edge.name, edge.weight))
        for trace in third_traces:
            if graph.get_edge(trace.name[-1]).from_ == edge.to_:
                second_traces.append(trace + GraphTrace(edge.name, edge.weight))

    for edge in stages["first_stage"]:
        # third_traces.append(GraphTrace(edge.name, edge.weight))
        for trace in second_traces:
            if graph.get_edge(trace.name[-1]).from_ == edge.to_:
                first_traces.append(trace + GraphTrace(edge.name, edge.weight))

    print("WHOLE SOLUTION: ")
    min_num = min(first_traces, key=attrgetter('weight'))
    print(min_num)

    print("SECOND STAGE: ")
    min_num = min(second_traces, key=attrgetter('weight'))
    print(min_num)

    print("THIRD STAGE: ")
    min_num = min(third_traces, key=attrgetter('weight'))
    print(min_num)

    print("FOURTH STAGE: ")
    min_num = min(fourth_traces, key=attrgetter('weight'))
    print(min_num)

    # print(first_traces)
    # print(second_traces)
    # print(third_traces)
    # print(fourth_traces)


    # for stage in stages.values():
    #
    #     print(stage)




if __name__ == "__main__":
    main()

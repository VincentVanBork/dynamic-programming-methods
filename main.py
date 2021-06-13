from collections import defaultdict

from components import Graph, GraphTrace
from operator import attrgetter

"""
VERY BAD IMPLEMENTATION BUT I DONT HAVE TIME TO MAKE IT BETTER XD
"""
def main(second_choice: bool):
    ...
    if second_choice:
        values = [2, 3, 4, 5, 6, 7, 8, 9]
    else:
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # możę dwa M ? a nie M N ?
    # w oryginale dwa M ale to chyba źle

    if second_choice:
        decisions = [
             "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
        weights = [
             5, 6, 7, 8, 6, 7, 5, 9, 6, 5, 5, 6
        ]
    else:
        decisions = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
        weights = [
            8, 6, 5, 6, 7, 8, 6, 7, 5, 9, 6, 5, 5, 6
        ]

    graph = Graph([])
    graph.fill_graph(values, decisions, weights)

    # print(graph)


    if second_choice:
        stages = {
            "first_stage": graph.edges[:2],
            "second_stage": graph.edges[2:6],
            "third_stage": graph.edges[6:10],
            "fourth_stage": graph.edges[10:]
        }

        print("STAGES")
        for stage in stages.values():
            print(stage)
    else:
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


    # w kążdym kolejnym kroku opieramy się na rozwiązaniach z poprzedniego
    # można by zrobić to ładnie rekurencyjnie ale meeh
    # nie rozumiem do końca różnicy pomiędzy strategią a rozwiązaniem
    # zaczynamy listowac wszystkie krawedzie
    for edge in stages["fourth_stage"]:
        fourth_traces.append(GraphTrace(edge.name, edge.weight))

    # liczymy najlepsze rozwiązanie dla 3 etapu
    for edge in stages["third_stage"]:
        # third_traces.append(GraphTrace(edge.name, edge.weight))
        for trace in fourth_traces:
            if graph.get_edge(trace.name[-1]).from_ == edge.to_:
                third_traces.append(trace + GraphTrace(edge.name, edge.weight))

    # liczymy najlepsze rozwiązanie dla 2 etapu
    for edge in stages["second_stage"]:
        # third_traces.append(GraphTrace(edge.name, edge.weight))
        for trace in third_traces:
            if graph.get_edge(trace.name[-1]).from_ == edge.to_:
                second_traces.append(trace + GraphTrace(edge.name, edge.weight))

    # liczymy najlepsze rozwiązanie dla 1 etapu
    for edge in stages["first_stage"]:
        # third_traces.append(GraphTrace(edge.name, edge.weight))
        for trace in second_traces:
            if graph.get_edge(trace.name[-1]).from_ == edge.to_:
                first_traces.append(trace + GraphTrace(edge.name, edge.weight))

    print(first_traces)
    print(second_traces)
    print(third_traces)
    print(fourth_traces)


    print("WHOLE SOLUTION:")
    min_num = min(first_traces, key=attrgetter('weight'))
    print("[--] ORDER OF EDGES: ", list(min_num.name[::-1]))
    print("[--] SOLUTION: ", min_num.weight)
    print("[--] BEST OPTION: ", min_num.name[0])

    print("------------------------")
    print("SECOND STAGE: ")
    min_num = min(second_traces, key=attrgetter('weight'))
    print("ORDER OF EDGES: ", list(min_num.name[::-1]))
    print("BEST OPTION: ", min_num.name[0])
    print("------------------------")
    print("THIRD STAGE: ")
    min_num = min(third_traces, key=attrgetter('weight'))
    print("ORDER OF EDGES: ", list(min_num.name[::-1]))
    print("BEST OPTION: ", min_num.name[0])
    print("------------------------")
    print("FOURTH STAGE: ")
    min_num = min(fourth_traces, key=attrgetter('weight'))
    print("ORDER OF EDGES: ", list(min_num.name[::-1]))
    print("BEST OPTION: ", min_num.name[0])





if __name__ == "__main__":
    main(second_choice=True)

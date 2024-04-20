"""
Module to build a graph from notes and convert it to a dot file.
"""

from memory_profiler import profile
import cProfile
import re


@profile
def build_graph_from_note(note_path: str, graph=None) -> dict:
    """
    Function takes a path to a note and returns a dictionary
    with all links to other notes in this note, and all notes which direct to the given note.
    """

    if graph is None:
        graph = {}

    note = note_path.split("/")[-1][:-3]
    pwd = note_path[: note_path.rfind("/") + 1]

    try:
        with open(note_path, "r", encoding="utf-8") as note_file:
            matches = re.findall(r"\[\[([^]]*)\]\]", note_file.read())
            for match_ in matches:
                if note in graph:
                    if match_ not in graph[note]:
                        graph[note].append(match_)
                        graph = build_graph_from_note(pwd + match_ + ".md", graph)
                else:
                    graph[note] = [match_]
                    graph = build_graph_from_note(pwd + match_ + ".md", graph)
    except FileNotFoundError:
        graph = {key: sorted(values) for key, values in sorted(graph.items())}
        return graph

    return {key: sorted(values) for key, values in sorted(graph.items())}


def convert_to_dot(graph: dict):
    """
    Converts dictionary to graph
    """

    with open("graph.dot", "w", encoding="utf-8") as graph_dot:
        graph_dot.write("digraph {\n")
        for key, value in sorted(graph.items()):
            for node in sorted(value):
                graph_dot.write(f"{key} -> {node}\n")

        graph_dot.write("}\n")


if __name__ == "__main__":
    # cProfile.run("print(build_graph_from_note('./notes/file1.md'))")
    print(build_graph_from_note("./notes/file1.md"))

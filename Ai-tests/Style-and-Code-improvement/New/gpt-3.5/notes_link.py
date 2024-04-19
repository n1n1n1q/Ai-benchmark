from memory_profiler import profile
import re
import cProfile
import os


@profile
def build_graph_from_note(note_path: str, graph=None) -> dict:
    """
    Function takes a path to a note and returns a dictionary
    with all links to other notes in this note, and all notes which direct to given note.
    """

    if graph is None:
        graph = {}

    note = os.path.splitext(os.path.basename(note_path))[0]

    try:
        with open(note_path, "r", encoding="utf-8") as note_file:
            matches = re.findall(r"\[\[([^]]*)\]\]", note_file.read())
            for match_ in matches:
                if note not in graph:
                    graph[note] = []
                if match_ not in graph[note]:
                    graph[note].append(match_)
                    graph = build_graph_from_note(
                        os.path.join(os.path.dirname(note_path), match_ + ".md"), graph
                    )
    except FileNotFoundError:
        pass

    return {k: sorted(v) for k, v in sorted(graph.items()) if v}  # Exclude empty lists


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
    # cProfile.run("build_graph_from_note('./notes/file1.md')")
    build_graph_from_note("./notes/file1.md")

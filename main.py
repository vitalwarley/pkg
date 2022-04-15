import logging
from argparse import ArgumentParser
import graphviz


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def roam():
    dot = graphviz.Digraph(
        "roam",
        comment="Roam Protocol",
        node_attr={"shape": "plaintext"},
        format="png",
    )
    dot.node("0", "Daily notes")
    dot.node("A", "Daily learning")
    dot.node("B", "Daily routine")
    dot.node("C", "Daily writing")
    dot.edges(["0A", "0B", "0C"])
    dot.render(filename="roam", directory="graphs")
    output_file = "graphs/roam.png"
    LOGGER.info("roam graph generated at %s.", output_file)


def pkg():
    dot = graphviz.Digraph(
        "pkg",
        comment="Personal Knowledge Graph",
        node_attr={"shape": "plaintext"},
        format="png",
    )
    dot.node("A", "Source of Knowledge (article, book, video etc)")
    dot.node("B", "Processing (i.e., read and take notes)")
    dot.node("C", "Understanding (write down original thoughts from notes)")
    dot.edges(["AB", "BC"])
    dot.render(filename="pkg", directory="graphs")
    output_file = "graphs/pkg.png"
    LOGGER.info("pkg graph generated at %s.", output_file)


def all():
    roam()
    pkg()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--graph", type=str, default="all")
    args = parser.parse_args()

    main = __import__(__name__)
    func = getattr(main, args.graph)
    func()

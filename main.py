import graphviz

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

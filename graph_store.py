import networkx as nx
from typing import Dict

GRAPH_DB: Dict[str, nx.Graph] = {}

def load_graph(graph_id: str) -> nx.Graph:
    return GRAPH_DB.get(graph_id)

def save_graph(graph_id: str, G: nx.Graph):
    GRAPH_DB[graph_id] = G
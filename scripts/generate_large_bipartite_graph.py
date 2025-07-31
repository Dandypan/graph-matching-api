
import networkx as nx
from graph_store import save_graph

def generate_complex_bipartite_graph():
    B = nx.Graph()

    # 左侧节点 U: u1 ~ u10
    U = [f"u{{i}}" for i in range(1, 11)]
    # 右侧节点 V: v1 ~ v10
    V = [f"v{{i}}" for i in range(1, 11)]

    B.add_nodes_from(U, bipartite=0)
    B.add_nodes_from(V, bipartite=1)

    edges = [
        ("u1", "v1"), ("u1", "v2"),
        ("u2", "v2"), ("u2", "v3"),
        ("u3", "v3"), ("u3", "v4"),
        ("u4", "v1"), ("u4", "v5"),
        ("u5", "v5"), ("u5", "v6"),
        ("u6", "v6"), ("u6", "v7"),
        ("u7", "v7"), ("u7", "v8"),
        ("u8", "v8"), ("u8", "v9"),
        ("u9", "v9"), ("u9", "v10"),
        ("u10", "v10"), ("u10", "v1"),
        ("u1", "v5"), ("u2", "v6"), ("u3", "v7"),
        ("u4", "v8"), ("u5", "v9"), ("u6", "v10"),
    ]

    B.add_edges_from(edges)
    return B

if __name__ == "__main__":
    G = generate_complex_bipartite_graph()
    save_graph("large-bipartite", G)
    print("✅ 复杂图 large-bipartite 成功生成并写入 GRAPH_DB。")

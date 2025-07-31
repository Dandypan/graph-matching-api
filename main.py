
from fastapi import FastAPI
from routers.match import router as match_router
from fastapi.middleware.cors import CORSMiddleware
from graph_store import save_graph
from scripts.generate_large_bipartite_graph import generate_complex_bipartite_graph

app = FastAPI(title="Graph Matching API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(match_router)

# ✅ 启动时生成一个较复杂的二分图并注册为 'default'
@app.on_event("startup")
def preload_graph():
    G = generate_bipartite_graph(n1=30, n2=30, edge_prob=0.4)
    save_graph("default", G)
    print("✅ 图 'default' 已加载，共有", len(G.nodes), "个节点。")

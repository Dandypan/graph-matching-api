from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import match
from graph_store import save_graph
from scripts.generate_large_bipartite_graph import generate_complex_bipartite_graph

app = FastAPI()

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 你可以根据需要替换为指定域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(match.router)

@app.on_event("startup")
def preload_graph():
    G = generate_complex_bipartite_graph()
    save_graph("large-bipartite", G)

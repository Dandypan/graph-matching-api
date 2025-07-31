from fastapi import FastAPI
from routers import match
from graph_store import save_graph
from scripts.generate_large_bipartite_graph import generate_complex_bipartite_graph

app = FastAPI()
app.include_router(match.router)

@app.on_event("startup")
def preload_graph():
    G = generate_complex_bipartite_graph()
    save_graph("large-bipartite", G)

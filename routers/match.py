from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from algorithms.match_utils import run_hopcroft_karp_with_steps, run_blossom_with_steps
from graph_store import load_graph

router = APIRouter(prefix="/api/graph", tags=["Matching"])

class MatchRequest(BaseModel):
    algorithm: str

@router.post("/{graph_id}/match")
def match(graph_id: str, req: MatchRequest):
    G = load_graph(graph_id)
    if G is None:
        raise HTTPException(status_code=404, detail="Graph not found")

    if req.algorithm == "hopcroft-karp":
        steps, summary = run_hopcroft_karp_with_steps(G)
    elif req.algorithm == "blossom":
        steps, summary = run_blossom_with_steps(G)
    else:
        raise HTTPException(status_code=400, detail="Unsupported algorithm")

    return {"steps": steps, "summary": summary}
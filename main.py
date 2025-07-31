from fastapi import FastAPI
from routers.match import router as match_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Graph Matching API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(match_router)
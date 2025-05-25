from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware


import json

app = FastAPI ()

@app.get("/")
def index ():
    return {
                "message": "Welcome to the First FastAPI App!"
            }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

with open("q-vercel-python.json") as f:
    data = json.load(f)

@app.get("/api/params")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [data.get(name, 0) for name in names]
    return {"marks": marks}
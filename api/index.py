from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI ()

@app.get("/")
def read_root():
    return {"message": "Welcome to the First FastAPI App!"}

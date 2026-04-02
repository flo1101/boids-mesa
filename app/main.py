from fastapi import FastAPI
from app.router import simulation_router

app = FastAPI()

app.include_router(simulation_router.router)


@app.get("/")
def read_root():
    return {"message": "Hello there!"}

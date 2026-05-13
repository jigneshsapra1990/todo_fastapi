from fastapi import FastAPI

app = FastAPI()

@app.get("/{id}")
async def root(id:int):
    return {"message": f"Hello Fast Api {id}"}
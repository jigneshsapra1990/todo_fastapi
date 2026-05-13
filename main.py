from fastapi import FastAPI

app = FastAPI()

@app.get("/{id}")
def root(id:int):
    return {"message": f"Hello Fast Api {id}"}

@app.post("/todo")
def addPost(item: dict):
    return {"message": f"Hello Fast Api {item}"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def data():
    return {"message":"hello My class how are you? I am fine well "}

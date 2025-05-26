from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def data():
    return {"message":"hello My class how are you? I am fine well "}

@app.get("/api")
def data2():
    return [
        {
            "name":"Shoaib",
            "age":28,
            "class": "MS Artificial Intelligence"
        },
         {
            "name":"atif",
            "age":23,
            "class": "BS Artificial Intelligence"
        },
         {
            "name":"ashutosh",
            "age":25,
            "class": "BS Artificial Intelligence"
        },
    ]

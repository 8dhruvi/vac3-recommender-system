from fastapi import FastAPI

app= FastAPI()

@app.get("/hello")
def index():
      return {"message":"hello World"}

@app.get("/test")
def index():
    return{"message":"test Api"}
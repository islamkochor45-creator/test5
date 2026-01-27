from fastapi import FastAPI


app = FastAPI()


@app.get("/get-data")
def response():
    return {"message": "github Actions"}

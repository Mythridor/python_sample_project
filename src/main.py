from fastapi import FastAPI

app = FastAPI()

@app.get("/healthz")
def is_up():
    return {"Status": "OK"}

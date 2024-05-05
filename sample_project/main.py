from fastapi import (
    FastAPI,
    __version__
)
from enum import Enum

app = FastAPI()


class Status(str, Enum):
    OK = "OK"
    NOK = "NOK"


@app.get("/healthz")
def is_up():
    status = (__version__ == '0.111.0') * Status.OK or Status.NOK
    return {"Status": status}

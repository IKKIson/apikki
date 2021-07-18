import os

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from typing import Optional
import uvicorn

from utils.conf import config
from utils.file import isdir #import isdir
# import utils.logger

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event("startup")
async def startup_event():
    print("startup FastAPI")

@app.on_event("shutdown")
def shutdown_event():
    print("shutdown FastAPI")
    # with open("log.txt", mode="a") as log:
    #     log.write("Application shutdown")





fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

from enum import Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# app.include_router(router_auth.router, prefix="/auth",
#                    tags=["auth"],  responses={404: {"description": "Not found"}})


if __name__ == "__main__":
    conf=config
    host=conf["host"]
    port=conf["port"]
    log_level=conf["log_level"]
    _log_dir=conf["log_dir"]
    log_dir=_log_dir
    if isdir(log_dir) is False:
        print("no exist log directory")
        log_dir = os.getcwd() + "/logs"
        os.mkdir(log_dir)
    if _log_dir == "." or _log_dir is None or _log_dir is "":
        log_dir = os.getcwd() + "/logs"
        os.mkdir(log_dir)
    print(log_dir)

    path=os.getcwd() + '/.apikkipid'

    with open(path, 'w') as out:
        pid=str(os.getpid())
        out.write(pid)
    
    uvicorn.run(app, host=host, port=port, log_level=log_level)

from typing import Optional
import uvicorn
from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def read_root():
  return {"hello" : "world"}

if __name__ == "__main__":
 uvicorn.run(api, host="0.0.0.0", port=5000)
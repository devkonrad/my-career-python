import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from starlette.middleware.cors import CORSMiddleware

from models import Job as ModelJob
api = FastAPI()

api.add_middleware(DBSessionMiddleware, db_url="postgresql+psycopg2://postgres:postgres@db/mycarrer")

# Cors for local tests
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/")
async def root():
    return {"message": "hello world"}

@api.get('/jobs/')
async def jobs():
    jobs = db.session.query(ModelJob).all()
    return jobs
    
# To run locally
if __name__ == '__main__':
    uvicorn.run(api, host='0.0.0.0', port=5000)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
import requests
#########################################################

# app = FastAPI()
# app.mount("/", StaticFiles(directory="public", html = True), name="static")
# Cloudtyp 레거시 코드

app = FastAPI()
origins = ["*"]

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

#위의 설정은 모든 origin, 모든 cookie, 모든 method, 모든 header를 allow한다.
########################POST를 위한 모델 설정#############################
class test(BaseModel):
    test: str
    test: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def read_root():
  return { 
    "message": "Welcome to my Project by JONGHEON LEE"
   }
   
@app.post("/test")
async def TEST(item: test):
    params = dict(item)
    return params
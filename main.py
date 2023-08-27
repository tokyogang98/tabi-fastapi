from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
import json
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
    "https://port-0-tabi-fastapi-54ouz2lllql1pci.sel3.cloudtype.app/getPlaceAll"
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
   
@app.get("/getPlaceAll")
async def getPlaceAll():
    # 데이터베이스 연결 파라미터
    params = {
        "user": "default",
        "password": "5kKDsz0UhSdn",
        "host": "ep-withered-base-425049-pooler.eu-central-1.postgres.vercel-storage.com",
        "port": "5432",
        "database": "verceldb"
    }

    # 데이터베이스에 연결
    conn = psycopg2.connect(**params)

    # 커서 생성
    cursor = conn.cursor()

    # "Place" 테이블의 모든 데이터 조회
    cursor.execute('SELECT * FROM "Place";')


    row = ""
    # 결과 출력
    result_data = []
    print("Place 테이블의 내용:")
    for row in cursor:
        result = {}
        
        result["id"] = row[0]
        result["name"] =row[1]
        result["movieId"] =row[2]
        result["location"] =row[3]
        result["latitude"] =str(row[4])
        result["longitude"] =str(row[5])
        result["contact"] =row[6]
        result["link"] =row[7]
        result["photo"] =row[8]
        result_data.append(result)


    # 커서와 연결 종료
    cursor.close()
    conn.close()

    final_result = json.dumps(result_data, ensure_ascii=False)
    return final_result

@app.post("/test")
async def TEST(item: test):
    params = dict(item)
    return params





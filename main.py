from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

app = FastAPI()
templates = Jinja2Templates(directory = "templates")

#index 함수 정의. 
@app.get("/")
def index(request:Request):
    return templates.TemplateResponse(
        "login.html", {
            "request" : request
        }
    )

#BaseModel을 상속받은 클래스 정의
class UserInfoModel(BaseModel):
    #type을 꼭 정의
    userid:str = Field()
    password:str = Field()

members = [
    {'userid' : 'sh', 'password' : 'qwer'},
    {'userid' : 'hs', 'password' : 'qwer1234'},
]

#'/login' 패스로 접속하면 login 함수를 post실행한다
@app.post("/login")
#UserInfoModel를 객체로 받는 login 함수 정의
def login(request:Request, user_info:UserInfoModel):
    userid = user_info.userid
    password = user_info.password

    #member 리스트 안에서 객체m을 받아와서 userid로 저장
    member = [m for m in members if m['userid'] == userid]
    if len(member) == 0:
        return {'msg' : '회원정보가 없습니다.'}
    
    elif member[0]['password'] != password:
        return {'msg' : '패스워드가 일치하지 않습니다.'}
    
    else:
        return {'msg' : f'{userid} 고객님 환영합니다.'}
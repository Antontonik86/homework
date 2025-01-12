from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

templates = Jinja2Templates(directory="templates")

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get('/')
async def read(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {"request": request, "users": users})

@app.get('/users')
async def get_users() -> List[User]:
    return users

@app.get('/user/{user_id}')
async def read_user(
        request: Request,
        user_id: Annotated[int, Path(description='Enter user ID', example=1)]) -> HTMLResponse:

    user = next((user for user in users if user.id == user_id), None)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    return templates.TemplateResponse("users.html", {"request": request, "user": user})

@app.post('/user/{username}/{age}')
async def add_user(
        request: Request,
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> HTMLResponse:

    user_id = len(users) + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)

    return templates.TemplateResponse("users.html", {"request": request, "user": new_user})

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(description='Enter user ID', example=1)],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanProfi')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=28)]) -> User:

    user = next((user for user in users if user.id == user_id), None)

    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    user.username = username
    user.age = age
    return user

@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(description='Enter user ID', example=2)]) -> User:

    user = next((user for user in users if user.id == user_id), None)

    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    users.remove(user)  
    return user
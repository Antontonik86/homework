from fastapi import FastAPI
import anyio
import module_16_1

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return { "Главная страница"}

@app.get("/user/admin")
async def welcome_admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def welcome_user_id(user_id) -> str:
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user")
async def user_info(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
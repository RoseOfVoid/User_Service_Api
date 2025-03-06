from routes.auth_routes import router as auth_router

from fastapi import FastAPI
import uvicorn

app = FastAPI()

app.include_router(auth_router)


if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8000)


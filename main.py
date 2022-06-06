
from fastapi import FastAPI,HTTPException,status
from fastapi.responses import RedirectResponse
from routes.create import create_route

app = FastAPI(title="TechStrome")

@app.get("/")
def root():
    return RedirectResponse('/docs')

app.include_router(create_route)
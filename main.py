
from fastapi import FastAPI,HTTPException,status
from fastapi.responses import RedirectResponse
from create import create_route
from read import read_route

app = FastAPI(title="TechStrome")

@app.get("/")
def root():
    return RedirectResponse('/docs')

app.include_router(create_route)
app.include_router(read_route)

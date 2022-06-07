
from fastapi import FastAPI,HTTPException,status
from fastapi.responses import RedirectResponse
from create import create_route


app = FastAPI(title="TechStrome")

app.include_router(create_route)

@app.get("/")
def root():
    return RedirectResponse('/docs')



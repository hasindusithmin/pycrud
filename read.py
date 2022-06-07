
from fastapi import APIRouter,HTTPException,status
import model
from playhouse.shortcuts import model_to_dict
# ---------------------------------------
read_route = APIRouter(
    prefix="/read",
    tags=["read"]
)

@read_route.get("/{entity}")
async def read(id:int=None,entity:str=None):
    try:
        entity = entity.strip()
        if id != None:
            return eval(f"model_to_dict(model.{entity}.get_by_id({id}))")
        lst = []
        coll = eval(f"model.{entity}.select()")
        for elem in coll:
            lst.append(model_to_dict(elem))
        return lst
    except:
        raise HTTPException(status_code=404,detail="item not found")




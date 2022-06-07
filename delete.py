
from fastapi import APIRouter,HTTPException,status
import model
from playhouse.shortcuts import model_to_dict
# ---------------------------------------
delete_route = APIRouter(
    prefix="/delete",
    tags=["delete"]
)

deleteable = ["Event","Video","Photo","Announcement","Review","Campsite","CamperCampSite","CamperEvent","CampsitePackageGuider","CampsitePackageTransport","CampsitePackageDriver","CampsitePackageEqipment","CampsitePackageMeal","AdminReview"]

@delete_route.delete("/{entity}")
async def delete(id:int,entity:str):
    entity = entity.strip()
    if entity in deleteable:
        eval(f"model.{entity}.delete_by_id({id})")
        raise HTTPException(status_code=202,detail="deleted")
    else:
        raise HTTPException(status_code=400,detail="can't operate")



from fastapi import APIRouter,HTTPException,status
from fastapi.responses import RedirectResponse
from dto import Admin,CampsiteOwner,Camper,Guilder,TransPort,Meal,Driver,Equipment,Event,Video,Photo,Campsite_Package,Announcement,Review,Campsite,CamperCampSite,CamperEvent,CampsitePackageGuider,CampsitePackageTransport,CampsitePackageDriver,CampsitePackageEqipment,CampsitePackageMeal,AdminReview
import model
from playhouse.shortcuts import model_to_dict


update_route = APIRouter(prefix="/update",tags=["update"])

@update_route.put("/admin/{id}")
async def update_admin(req_body:Admin,id:int):
    query = model.Admin.update(**req_body.dict()).where(model.Admin.admin_id==id)
    query.execute()
    return status.HTTP_202_ACCEPTED


@update_route.put("/camp-site-owner/{id}")
async def update_campsite_owner(req_body:CampsiteOwner,id:int):
    query = model.CampsiteOwner.update(**req_body.dict()).where(model.CampsiteOwner.campsite_owner_id==id)
    query.execute()
    return status.HTTP_202_ACCEPTED

@update_route.put("/camper/{id}")
async def update_camper(req_body:Camper,id:int):
    query = model.Camper.update(**req_body.dict()).where(model.Camper.campsite_id==id)
    query.execute()
    return status.HTTP_202_ACCEPTED

@update_route.put("/guilder/{id}")
async def update_guilder(req_body:Guilder,id:int):
    query = model.Guilder.update(**req_body.dict()).where(model.Guilder.guilder_id==id)
    query.execute()
    return status.HTTP_202_ACCEPTED

@update_route.put("/transport/{id}")
async def update_transport(req_body:TransPort,id:int):
    query = model.TransPort.update(**req_body.dict()).where(model.TransPort.vehicle_id==id)
    query.execute()
    return status.HTTP_202_ACCEPTED

@update_route.put("/meal/{id}")
async def update_meal(req_body:Meal,id:int):
    query = model.Meal.update(**req_body.dict()).where(model.Meal.meal_id==id)
    query.execute()
    return status.HTTP_202_ACCEPTED

@update_route.put("/driver/{id}")
async def update_driver(req_body:Driver,id:int):
    query = model.Driver.update(**req_body.dict()).where(model.Driver.driver_id==id)
    query.execute()
    return status.HTTP_202_ACCEPTED

@update_route.put("/equipment/{id}")
async def update_equipment(req_body:Equipment,id:int):
    query = model.Equipment.update(**req_body.dict()).where(model.Equipment.equipment_id==id)
    query.execute()
    return status.HTTP_202_ACCEPTED


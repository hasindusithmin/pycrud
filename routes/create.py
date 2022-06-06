
from fastapi import APIRouter,HTTPException,status
from fastapi.responses import RedirectResponse
from dto import Admin,CampsiteOwner,Camper,Guilder,TransPort,Meal,Driver,Equipment,Event,Video,Photo,Campsite_Package,Announcement,Review,Campsite,CamperCampSite,CamperEvent,CampsitePackageGuider,CampsitePackageTransport,CampsitePackageDriver,CampsitePackageEqipment,CampsitePackageMeal,AdminReview

create_route = APIRouter(
    prefix="/create",
    tags=["create"]
)

@create_route.post("/admin")
async def create_admin(req_body:Admin):
    return status.HTTP_200_OK

@create_route.post("/camp-site-owner")
async def create_campsite_owner(req_body:CampsiteOwner):
    return status.HTTP_200_OK

@create_route.post("/camper")
async def create_camper(req_body:Camper):
    return status.HTTP_200_OK

@create_route.post("/guilder")
async def create_guilder(req_body:Guilder):
    return status.HTTP_200_OK

@create_route.post("/transport")
async def create_transport(req_body:TransPort):
    return status.HTTP_200_OK

@create_route.post("/meal")
async def create_meal(req_body:Meal):
    return status.HTTP_200_OK

@create_route.post("/driver")
async def create_driver(req_body:Driver):
    return status.HTTP_200_OK

@create_route.post("/equipment")
async def create_equipment(req_body:Equipment):
    return status.HTTP_200_OK

@create_route.post("/event")
async def create_event(req_body:Event):
    return status.HTTP_200_OK

@create_route.post("/video")
async def create_video(req_body:Video):
    return status.HTTP_200_OK

@create_route.post("/photo")
async def create_photo(req_body:Photo):
    return status.HTTP_200_OK

@create_route.post("/campsite-package")
async def create_campsite_package(req_body:Campsite_Package):
    return status.HTTP_200_OK

@create_route.post("/announcement")
async def create_announcement(req_body:Announcement):
    return status.HTTP_200_OK

@create_route.post("/review")
async def create_review(req_body:Review):
    return status.HTTP_200_OK

@create_route.post("/campsite")
async def create_campsite(req_body:Campsite):
    return status.HTTP_200_OK

@create_route.post("/camper-campsite")
async def create_camper_campsite(req_body:CamperCampSite):
    return status.HTTP_200_OK

@create_route.post("/camper-event")
async def create_camper_event(req_body:CamperEvent):
    return status.HTTP_200_OK

@create_route.post("/campsite-package-guilder")
async def create_campsite_package_guilder(req_body:CampsitePackageGuider):
    return status.HTTP_200_OK

@create_route.post("/campsite-package")
async def create_campsite_package_transport(req_body:CampsitePackageTransport):
    return status.HTTP_200_OK

@create_route.post("/campsite-package-driver")
async def create_campsite_package_driver(req_body:CampsitePackageDriver):
    return status.HTTP_200_OK

@create_route.post("/campsite-package-eqipment")
async def create_campsite_package_eqipment(req_body:CampsitePackageEqipment):
    return status.HTTP_200_OK

@create_route.post("/campsite-package-meal")
async def create_campsite_package_meal(req_body:CampsitePackageMeal):
    return status.HTTP_200_OK

@create_route.post("/admin-review")
async def create_admin_review(req_body:AdminReview):
    return status.HTTP_200_OK
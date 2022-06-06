
from fastapi import FastAPI,HTTPException,status
from fastapi.responses import RedirectResponse
from dto import Admin,CampsiteOwner,Camper,Guilder,TransPort,Meal,Driver,Equipment,Event,Video,Photo,Campsite_Package,Announcement,Review,Campsite,CamperCampSite,CamperEvent,CampsitePackageGuider,CampsitePackageTransport,CampsitePackageDriver,CampsitePackageEqipment,CampsitePackageMeal,AdminReview
app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse('/docs')

@app.post("/admin")
async def create_admin(req_body:Admin):
    return status.HTTP_200_OK

@app.post("/camp-site-owner")
async def create_campsite_owner(req_body:CampsiteOwner):
    return status.HTTP_200_OK

@app.post("/camper")
async def create_camper(req_body:Camper):
    return status.HTTP_200_OK

@app.post("/guilder")
async def create_guilder(req_body:Guilder):
    return status.HTTP_200_OK

@app.post("/transport")
async def create_transport(req_body:TransPort):
    return status.HTTP_200_OK

@app.post("/meal")
async def create_meal(req_body:Meal):
    return status.HTTP_200_OK

@app.post("/driver")
async def create_driver(req_body:Driver):
    return status.HTTP_200_OK

@app.post("/equipment")
async def create_equipment(req_body:Equipment):
    return status.HTTP_200_OK

@app.post("/event")
async def create_event(req_body:Event):
    return status.HTTP_200_OK

@app.post("/video")
async def create_video(req_body:Video):
    return status.HTTP_200_OK

@app.post("/photo")
async def create_photo(req_body:Photo):
    return status.HTTP_200_OK

@app.post("/campsite-package")
async def create_campsite_package(req_body:Campsite_Package):
    return status.HTTP_200_OK

@app.post("/announcement")
async def create_announcement(req_body:Announcement):
    return status.HTTP_200_OK

@app.post("/review")
async def create_review(req_body:Review):
    return status.HTTP_200_OK

@app.post("/campsite")
async def create_campsite(req_body:Campsite):
    return status.HTTP_200_OK

@app.post("/camper-campsite")
async def create_camper_campsite(req_body:CamperCampSite):
    return status.HTTP_200_OK

@app.post("/camper-event")
async def create_camper_event(req_body:CamperEvent):
    return status.HTTP_200_OK

@app.post("/campsite-package-guilder")
async def create_campsite_package_guilder(req_body:CampsitePackageGuider):
    return status.HTTP_200_OK

@app.post("/campsite-package")
async def create_campsite_package_transport(req_body:CampsitePackageTransport):
    return status.HTTP_200_OK

@app.post("/campsite-package-driver")
async def create_campsite_package_driver(req_body:CampsitePackageDriver):
    return status.HTTP_200_OK

@app.post("/campsite-package-eqipment")
async def create_campsite_package_eqipment(req_body:CampsitePackageEqipment):
    return status.HTTP_200_OK

@app.post("/campsite-package-meal")
async def create_campsite_package_meal(req_body:CampsitePackageMeal):
    return status.HTTP_200_OK

@app.post("/admin-review")
async def create_admin_review(req_body:AdminReview):
    return status.HTTP_200_OK
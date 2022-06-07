
from fastapi import APIRouter,HTTPException,status
from fastapi.responses import RedirectResponse
from dto import Admin,CampsiteOwner,Camper,Guilder,TransPort,Meal,Driver,Equipment,Event,Video,Photo,Campsite_Package,Announcement,Review,Campsite,CamperCampSite,CamperEvent,CampsitePackageGuider,CampsitePackageTransport,CampsitePackageDriver,CampsitePackageEqipment,CampsitePackageMeal,AdminReview
import model
from playhouse.shortcuts import model_to_dict

create_route = APIRouter(
    prefix="/create",
    tags=["create"]
)

@create_route.post("/admin")
async def create_admin(req_body:Admin):
    return model_to_dict(model.Admin.create(**req_body.dict()))

@create_route.post("/camp-site-owner")
async def create_campsite_owner(req_body:CampsiteOwner):
    return model_to_dict(model.CampsiteOwner.create(**req_body.dict()))

@create_route.post("/camper")
async def create_camper(req_body:Camper):
    return model_to_dict(model.Camper.create(**req_body.dict()))

@create_route.post("/guilder")
async def create_guilder(req_body:Guilder):
    return model_to_dict(model.Guilder.create(**req_body.dict()))

@create_route.post("/transport")
async def create_transport(req_body:TransPort):
    return model_to_dict(model.TransPort.create(**req_body.dict()))

@create_route.post("/meal")
async def create_meal(req_body:Meal):
    return model_to_dict(model.Meal.create(**req_body.dict()))

@create_route.post("/driver")
async def create_driver(req_body:Driver):
    return model_to_dict(model.Driver.create(**req_body.dict()))

@create_route.post("/equipment")
async def create_equipment(req_body:Equipment):
    return model_to_dict(model.Equipment.create(**req_body.dict()))

@create_route.post("/event")
async def create_event(req_body:Event):
    dict = req_body.dict()
    camper = model.Camper.create(**dict['camper_id'])
    camper_owner = model.CampsiteOwner.create(**dict['camper_owner_id'])
    event =  model.Event.create(
        name = dict['name'],
        event_location = dict['event_location'],
        starting_date = dict['starting_date'],
        starting_time = dict['starting_time'],
        participants_capasity = dict['participants_capasity'],
        description = dict['description'],
        camper_id = camper,
        camper_owner_id = camper_owner
    )
    return model_to_dict(event)

@create_route.post("/video")
async def create_video(req_body:Video):
    dict = req_body.dict()
    camper = model.Camper.create(**dict['camper_id'])
    camper_owner = model.CampsiteOwner.create(**dict['camper_owner_id'])
    video = model.Video.create(
        type = dict['type'],
        update_date = dict['update_date'],
        camper_id = camper,
        camper_owner_id = camper_owner
    )
    return model_to_dict(video)

@create_route.post("/photo")
async def create_photo(req_body:Photo):
    dict = req_body.dict()
    camper = model.Camper.create(**dict['camper_id'])
    camper_owner = model.CampsiteOwner.create(**dict['camper_owner_id'])
    photo = model.Photo.create(
        type = dict['type'],
        update_date = dict['update_date'],
        camper_id = camper,
        camper_owner_id = camper_owner
    )
    return model_to_dict(photo)

@create_route.post("/campsite-package")
async def create_campsite_package(req_body:Campsite_Package):
    dict = req_body.dict()
    camper = model.Camper.create(**dict['camper_id'])
    Campsite_Package = model.Campsite_Package.create(
        name = dict['name'],
        price = dict['price'],
        camper_id = camper
    )
    return model_to_dict(Campsite_Package)

@create_route.post("/announcement")
async def create_announcement(req_body:Announcement):
    dict = req_body.dict()
    camper_owner = model.CampsiteOwner.create(**dict['camper_owner_id'])
    announcement = model.Announcement.create(
        content = dict['content'],
        dates = dict['dates'],
        times = dict['times'],
        camper_owner_id = camper_owner
    )
    return model_to_dict(announcement)

@create_route.post("/review")
async def create_review(req_body:Review):
    dict = req_body.dict()
    camper = model.Camper.create(**dict['camper_id'])
    review = model.Review.create(
        content = dict['content'],
        dates = dict['dates'],
        times = dict['times'],
        camper_id = camper
    )
    return model_to_dict(review)

@create_route.post("/campsite")
async def create_campsite(req_body:Campsite):
    dict = req_body.dict()
    camper = model.Camper.create(**dict['camper_id'])
    camper_owner = model.CampsiteOwner.create(**dict['camper_owner_id'])
    campsite = model.Campsite.create(
        name=dict['name'],
        address=dict['address'],
        location=dict['location'],
        email=dict['email'],
        contact_number=dict['contact_number'],
        camper_id = camper,
        camper_owner_id = camper_owner
    )
    return model_to_dict(campsite)

@create_route.post("/camper-campsite")
async def create_camper_campsite(req_body:CamperCampSite):
    dict = req_body.dict()
    camper = model.Camper.create(**dict['camper_id'])
    camper_owner = model.CampsiteOwner.create(**dict['camper_owner_id'])
    camper_campsite = model.CamperCampSite.create(
        camper_id = camper,
        camper_owner_id = camper_owner
    )
    return model_to_dict(camper_campsite)

@create_route.post("/camper-event")
async def create_camper_event(req_body:CamperEvent):
    dict = req_body.dict()
    camper = model.Camper.create(**dict['camper_id'])
    camper_id = model.Camper.create(**dict['event_id']['camper_id'])
    camper_owner_id = model.CampsiteOwner.create(**dict['event_id']['camper_owner_id'])
    event = model.Event.create(
        name = dict['event_id']['name'],
        event_location = dict['event_id']['event_location'],
        starting_date = dict['event_id']['starting_date'],
        starting_time = dict['event_id']['starting_time'],
        participants_capasity = dict['event_id']['participants_capasity'],
        description = dict['event_id']['description'],
        camper_id = camper_id,
        camper_owner_id = camper_owner_id
    )
    camper_event = model.CamperEvent.create(
        camper_id = camper,
        event_id = event
    )
    return model_to_dict(camper_event)

@create_route.post("/campsite-package-guilder")
async def create_campsite_package_guilder(req_body:CampsitePackageGuider):
    dict = req_body.dict()
    guilder = model.Guilder.create(**dict['guilder_id'])
    camper = model.Camper.create(**dict['package_id']['camper_id'])
    package = model.Campsite_Package.create(
        name = dict['package_id']['name'],
        price = dict['package_id']['price'],
        camper_id = camper
    )
    campsite_package_guilder = model.CampsitePackageGuider.create(
        package_id = package,
        guilder_id = guilder
    )
    return model_to_dict(campsite_package_guilder)

@create_route.post("/campsite-package-transport")
async def create_campsite_package_transport(req_body:CampsitePackageTransport):
    dict = req_body.dict()
    vehicle = model.TransPort.create(**dict['vehicle_details'])
    camper = model.Camper.create(**dict['package_id']['camper_id'])
    package = model.Campsite_Package.create(
        name = dict['package_id']['name'],
        price = dict['package_id']['price'],
        camper_id = camper
    )
    campsite_package_transport = model.CampsitePackageTransport.create(
        package_id = package,
        vehicle_details = vehicle
    )
    return model_to_dict(campsite_package_transport)

@create_route.post("/campsite-package-driver")
async def create_campsite_package_driver(req_body:CampsitePackageDriver):
    dict = req_body.dict()
    driver = model.Driver.create(**dict['driver_id'])
    camper = model.Camper.create(**dict['package_id']['camper_id'])
    package = model.Campsite_Package.create(
        name = dict['package_id']['name'],
        price = dict['package_id']['price'],
        camper_id = camper
    )
    campsite_package_driver = model.CampsitePackageDriver.create(
        package_id = package,
        driver_id = driver
    )
    return model_to_dict(campsite_package_driver)

@create_route.post("/campsite-package-eqipment")
async def create_campsite_package_eqipment(req_body:CampsitePackageEqipment):
    dict = req_body.dict()
    equipment = model.Equipment.create(**dict['equipment_id'])
    camper = model.Camper.create(**dict['package_id']['camper_id'])
    package = model.Campsite_Package.create(
        name = dict['package_id']['name'],
        price = dict['package_id']['price'],
        camper_id = camper
    )
    campsite_package_eqipment = model.CampsitePackageEqipment.create(
        package_id = package,
        equipment_id = equipment
    )
    return model_to_dict(campsite_package_eqipment)

@create_route.post("/campsite-package-meal")
async def create_campsite_package_meal(req_body:CampsitePackageMeal):
    dict = req_body.dict()
    meal = model.Meal.create(**dict['meal_id'])
    camper = model.Camper.create(**dict['package_id']['camper_id'])
    package = model.Campsite_Package.create(
        name = dict['package_id']['name'],
        price = dict['package_id']['price'],
        camper_id = camper
    )
    campsite_package_meal = model.CampsitePackageMeal.create(
        meal_id = meal,
        package_id = package
    )
    return model_to_dict(campsite_package_meal)

@create_route.post("/admin-review")
async def create_admin_review(req_body:AdminReview):
    dict = req_body.dict()
    admin = model.Admin.create(**dict['admin_id'])
    camper = model.Camper.create(**dict['review_id']['camper_id'])
    review = model.Review.create(
        content = dict['review_id']['content'],
        dates = dict['review_id']['dates'],
        times = dict['review_id']['times'],
        camper_id = camper
    )
    admin_review = model.AdminReview.create(
        admin_id = admin,
        review_id = review
    )
    return model_to_dict(admin_review)
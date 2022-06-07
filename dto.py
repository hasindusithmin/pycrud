import pydantic
from datetime import date, time, datetime
class Admin(pydantic.BaseModel):
    first_name:str
    last_name:str
    email:str
    password:str
    contact_number:str

class CampsiteOwner(pydantic.BaseModel):
    first_name:str = pydantic.Field(max_length=55)
    last_name:str = pydantic.Field(max_length=55)
    email:str = pydantic.Field(max_length=85)
    password:str
    contact_number:str = pydantic.Field(max_length=10)

class Camper(pydantic.BaseModel):
    first_name:str = pydantic.Field(max_length=55)
    last_name:str = pydantic.Field(max_length=55)
    email:str = pydantic.Field(max_length=85)
    password:str
    contact_number:str = pydantic.Field(max_length=10)
    address:str
    age:int

class Guilder(pydantic.BaseModel):
    name:str =  pydantic.Field(max_length=55)
    charge_per_hour:float
    contact_number:str = pydantic.Field(max_length=10)
    gender:str = pydantic.Field(max_length=10)
    experience:str

class TransPort(pydantic.BaseModel):
    type:str = pydantic.Field(max_length=55)
    model:str = pydantic.Field(max_length=55)
    charge_per_km:float
    passenger_capacity:int
    fuel_type:str = pydantic.Field(max_length=10)
    vehicle_number:str

class Meal(pydantic.BaseModel):
    name:str = pydantic.Field(max_length=55)
    type:str = pydantic.Field(max_length=55)
    price:float

class Driver(pydantic.BaseModel):
    name:str = pydantic.Field(max_length=55)
    contact_number:str = pydantic.Field(max_length=12)
    gender:str = pydantic.Field(max_length=10)
    experience:str
    charge_per_km:float

class Equipment(pydantic.BaseModel):
    name:str = pydantic.Field(max_length=55)
    description:str
    available_quantity:int
    charging_rate:float

class Event(pydantic.BaseModel):
    name:str = pydantic.Field(max_length=55)
    event_location:str = pydantic.Field(max_length=55)
    starting_date:date =  None
    starting_time:time = pydantic.Field(default=datetime.now().time())
    participants_capasity:float
    description:str
    camper_id:Camper
    camper_owner_id :CampsiteOwner

class Video(pydantic.BaseModel):
    type:str = pydantic.Field(max_length=55)
    update_date:date = None
    camper_id:Camper
    camper_owner_id:CampsiteOwner

class Photo(pydantic.BaseModel):
    type:str = pydantic.Field(max_length=55)
    update_date:date = None
    camper_id:Camper
    camper_owner_id :CampsiteOwner

class Campsite_Package(pydantic.BaseModel):
    name:str = pydantic.Field(max_length=55)
    price:float
    camper_id:Camper

class Announcement(pydantic.BaseModel):
    content:str
    dates:date = None
    times:time = pydantic.Field(default=datetime.now().time())
    camper_owner_id:CampsiteOwner

class Review(pydantic.BaseModel):
    content:str
    dates:date = None
    times:time  = pydantic.Field(default=datetime.now().time())
    camper_id:Camper

class Campsite(pydantic.BaseModel):
    name:str = pydantic.Field(max_length=55)
    address:str
    location:str = pydantic.Field(max_length=55)
    email:str
    contact_number:str
    camper_id:Camper
    camper_owner_id:CampsiteOwner

class CamperCampSite(pydantic.BaseModel):
    camper_id:Camper
    camper_owner_id:CampsiteOwner

class CamperEvent(pydantic.BaseModel):
    camper_id:Camper
    event_id:Event

class CampsitePackageGuider(pydantic.BaseModel):
    package_id:Campsite_Package
    guilder_id:Guilder

class CampsitePackageTransport(pydantic.BaseModel):
    package_id:Campsite_Package
    vehicle_details:TransPort

class CampsitePackageDriver(pydantic.BaseModel):
    package_id:Campsite_Package
    driver_id:Driver

class CampsitePackageEqipment(pydantic.BaseModel):
    package_id:Campsite_Package
    equipment_id:Equipment

class CampsitePackageMeal(pydantic.BaseModel):
    package_id:Campsite_Package
    meal_id:Meal

class AdminReview(pydantic.BaseModel):
    admin_id:Admin
    review_id:Review


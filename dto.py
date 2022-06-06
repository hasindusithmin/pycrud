from pydantic import BaseModel,Field
from datetime import date, time

class Admin(BaseModel):
    first_name:str = Field(max_length=55)
    last_name:str = Field(max_length=55)
    email:str = Field(max_length=85)
    password:str
    contact_number:str = Field(max_length=10)

class CampsiteOwner(BaseModel):
    first_name:str = Field(max_length=55)
    last_name:str = Field(max_length=55)
    email:str = Field(max_length=85)
    password:str
    contact_number:str = Field(max_length=10)

class Camper(BaseModel):
    first_name:str = Field(max_length=55)
    last_name:str = Field(max_length=55)
    email:str = Field(max_length=85)
    password:str
    contact_number:str = Field(max_length=10)
    address:str
    age:int

class Guilder(BaseModel):
    name:str =  Field(max_length=55)
    charge_per_hour:float
    contact_number:str = Field(max_length=10)
    gender:str = Field(max_length=10)
    experience:str

class TransPort(BaseModel):
    type:str = Field(max_length=55)
    model:str = Field(max_length=55)
    charge_per_km:float
    passenger_capacity:int
    fuel_type:str = Field(max_length=10)
    vehicle_number:str

class Meal(BaseModel):
    name:str = Field(max_length=55)
    type:str = Field(max_length=55)
    price:float

class Driver(BaseModel):
    name:str = Field(max_length=55)
    contact_number:str = Field(max_length=12)
    gender:str = Field(max_length=10)
    experience:str
    charge_per_km:float

class Equipment(BaseModel):
    name:str = Field(max_length=55)
    description:str
    available_quantity:int
    charging_rate:float

class Event(BaseModel):
    name:str = Field(max_length=55)
    event_location:str = Field(max_length=55)
    starting_date:date =  None
    starting_time:time = None
    participants_capasity:float
    description:str
    camper_id:Camper
    camper_owner_id :CampsiteOwner

class Video(BaseModel):
    type:str = Field(max_length=55)
    update_date:date = None
    camper_id:Camper
    camper_owner_id:CampsiteOwner

class Photo(BaseModel):
    type:str = Field(max_length=55)
    update_date:date = None
    camper_id:Camper
    camper_owner_id :CampsiteOwner

class Campsite_Package(BaseModel):
    name:str = Field(max_length=55)
    price:float
    camper_id:Camper

class Announcement(BaseModel):
    content:str
    date:date = None
    time:time = None
    camper_owner_id:CampsiteOwner

class Review(BaseModel):
    content:str
    date:date = None
    time:time  = None
    camper_id:Camper

class Campsite(BaseModel):
    name:str = Field(max_length=55)
    address:str
    location:str = Field(max_length=55)
    email:str
    contact_number:str
    admin_id:Admin
    camper_id:Camper
    camper_owner_id:CampsiteOwner

class CamperCampSite(BaseModel):
    camper_id:Camper
    camper_owner_id:CampsiteOwner

class CamperEvent(BaseModel):
    camper_id:Camper
    event_id:Event

class CampsitePackageGuider(BaseModel):
    package_id:Campsite_Package
    guilder_id:Guilder

class CampsitePackageTransport(BaseModel):
    package_id:Campsite_Package
    vehicle_details:TransPort

class CampsitePackageDriver(BaseModel):
    package_id:Campsite_Package
    driver_id:Driver

class CampsitePackageEqipment(BaseModel):
    package_id:Campsite_Package
    equipment_id:Equipment

class CampsitePackageMeal(BaseModel):
    package_id:Campsite_Package
    meal_id:Meal

class AdminReview(BaseModel):
    admin_id:Admin
    review_id:Review

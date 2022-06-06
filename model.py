import peewee
from dotenv import load_dotenv
import os
import datetime
# ------------
load_dotenv()
db = peewee.PostgresqlDatabase(
    'postgres',
    user='postgres',
    password=os.getenv('PASSWORD'),
    host=os.getenv('HOST'),
)

class BaseModel(peewee.Model):
    class Meta:
        database=db

class Admin(BaseModel):
    admin_id = peewee.AutoField()
    first_name = peewee.CharField(max_length=55)
    last_name = peewee.CharField(max_length=55)
    email = peewee.CharField(unique=True)
    password = peewee.CharField(max_length=10)
    contact_number = peewee.CharField(max_length=12)

class CampsiteOwner(BaseModel):
    campsite_owner_id = peewee.AutoField()
    first_name = peewee.CharField(max_length=55)
    last_name = peewee.CharField(max_length=55)
    email = peewee.CharField(unique=True)
    password = peewee.CharField(max_length=10)
    contact_number = peewee.CharField(max_length=12)

class Camper(BaseModel):
    campsite_id = peewee.AutoField()
    first_name = peewee.CharField(max_length=55)
    last_name = peewee.CharField(max_length=55)
    email = peewee.CharField(unique=True)
    password = peewee.CharField(max_length=10)
    contact_number = peewee.CharField(max_length=12)
    address = peewee.CharField()
    age = peewee.SmallIntegerField()

class Guilder(BaseModel):
    guilder_id = peewee.AutoField()
    name = peewee.CharField(max_length=55)
    charge_per_hour = peewee.SmallIntegerField()
    contact_number = peewee.CharField(max_length=12)
    gender = peewee.CharField(max_length=10)
    experience = peewee.TextField()

class TransPort(BaseModel):
    vehicle_id = peewee.AutoField()
    type = peewee.CharField(max_length=55)
    model = peewee.CharField(max_length=55)
    charge_per_km = peewee.DecimalField()
    passenger_capacity = peewee.SmallIntegerField()
    fuel_type = peewee.CharField(max_length=10)
    vehicle_number = peewee.CharField(max_length=55)

class Meal(BaseModel):
    meal_id = peewee.AutoField()
    name = peewee.CharField(max_length=55)
    type = peewee.CharField(max_length=55)
    price = peewee.DecimalField()

class Driver(BaseModel):
    driver_id = peewee.AutoField()
    name = peewee.CharField(max_length=55)
    contact_number = peewee.CharField(max_length=12)
    gender = peewee.CharField(max_length=10)
    experience = peewee.TextField()
    charge_per_km = peewee.DecimalField()

class Equipment(BaseModel):
    equipment_id = peewee.AutoField()
    name = peewee.CharField(max_length=55)
    description = peewee.TextField()
    available_quantity = peewee.SmallIntegerField()
    charging_rate = peewee.DecimalField()

class Event(BaseModel):
    event_id = peewee.AutoField()
    name = peewee.CharField(max_length=55)
    event_location = peewee.CharField(max_length=55)
    starting_date = peewee.DateField()
    starting_time = peewee.TimeField()
    participants_capasity = peewee.SmallIntegerField()
    description = peewee.TextField()
    camper_id = peewee.ForeignKeyField(Camper,related_name="camper_details")
    camper_owner_id = peewee.ForeignKeyField(CampsiteOwner,related_name="campsite_owner_id")

class Video(BaseModel):
    video_id = peewee.AutoField()
    type = peewee.CharField(max_length=55)
    update_date = peewee.DateField()
    camper_id = peewee.ForeignKeyField(Camper,related_name="camper_details")
    camper_owner_id = peewee.ForeignKeyField(CampsiteOwner,related_name="campsite_owner_id")

class Photo(BaseModel):
    photo_id = peewee.AutoField()
    type = peewee.CharField(max_length=55)
    update_date = peewee.DateField()
    camper_id = peewee.ForeignKeyField(Camper,related_name="camper_details")
    camper_owner_id = peewee.ForeignKeyField(CampsiteOwner,related_name="campsite_owner_id")

class Campsite_Package(BaseModel):
    package_id = peewee.AutoField()
    name = peewee.CharField(max_length=55)
    price = peewee.DecimalField()
    camper_id = peewee.ForeignKeyField(Camper,related_name="camper_details")

class Announcement(BaseModel):
    announcement_id = peewee.AutoField()
    content = peewee.CharField()
    date = peewee.DateField()
    time = peewee.TimeField()
    camper_owner_id = peewee.ForeignKeyField(CampsiteOwner,related_name="campsite_owner_id")

class Review(BaseModel):
    review_id = peewee.AutoField()
    content = peewee.CharField()
    date = peewee.DateField()
    time = peewee.TimeField()
    camper_id = peewee.ForeignKeyField(Camper,related_name="camper_details")

class Campsite(BaseModel):
    campsite_id = peewee.AutoField()
    name = peewee.CharField(max_length=55)
    address = peewee.CharField()
    location = peewee.CharField(max_length=55)
    email = peewee.CharField(unique=True)
    contact_number = peewee.CharField(max_length=12)
    admin_id = peewee.ForeignKeyField(Admin,related_name="admin_id")
    camper_id = peewee.ForeignKeyField(Camper,related_name="camper_details")
    camper_owner_id = peewee.ForeignKeyField(CampsiteOwner,related_name="campsite_owner_id")

class CamperCampSite(BaseModel):
    camper_id = peewee.ForeignKeyField(Camper,related_name="camper_details")
    camper_owner_id = peewee.ForeignKeyField(CampsiteOwner,related_name="campsite_owner_id")

class CamperEvent(BaseModel):
    camper_id = peewee.ForeignKeyField(Camper,related_name="camper_details")
    event_id = peewee.ForeignKeyField(Event,related_name="event_id")

class CampsitePackageGuider(BaseModel):
    package_id = peewee.ForeignKeyField(Campsite_Package,related_name="campsite_package_details")
    guilder_id = peewee.ForeignKeyField(Guilder,related_name="guilder_id")

class CampsitePackageTransport(BaseModel):
    package_id = peewee.ForeignKeyField(Campsite_Package,related_name="campsite_package_details")
    vehicle_details = peewee.ForeignKeyField(TransPort,related_name="transport_details")

class CampsitePackageDriver(BaseModel):
    package_id = peewee.ForeignKeyField(Campsite_Package,related_name="campsite_package_details")
    driver_id = peewee.ForeignKeyField(Driver,related_name="driver_details")

class CampsitePackageEqipment(BaseModel):
    package_id = peewee.ForeignKeyField(Campsite_Package,related_name="campsite_package_details")
    equipment_id = peewee.ForeignKeyField(Equipment,related_name="equipment_details")

class CampsitePackageMeal(BaseModel):
    package_id = peewee.ForeignKeyField(Campsite_Package,related_name="campsite_package_details")
    meal_id = peewee.ForeignKeyField(Meal,related_name="meal_details")

class AdminReview(BaseModel):
    admin_id = peewee.ForeignKeyField(Admin,related_name="admin_details")
    review_id = peewee.ForeignKeyField(Review,related_name="review_details")

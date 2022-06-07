import peewee
from dotenv import load_dotenv
import os
import datetime
from playhouse.shortcuts import model_to_dict
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
    first_name = peewee.CharField()
    last_name = peewee.CharField()
    email = peewee.CharField()
    password = peewee.CharField()
    contact_number = peewee.CharField()

class CampsiteOwner(BaseModel):
    campsite_owner_id = peewee.AutoField()
    first_name = peewee.CharField()
    last_name = peewee.CharField()
    email = peewee.CharField()
    password = peewee.CharField()
    contact_number = peewee.CharField()


class Camper(BaseModel):
    campsite_id = peewee.AutoField()
    first_name = peewee.CharField()
    last_name = peewee.CharField()
    email = peewee.CharField()
    password = peewee.CharField()
    contact_number = peewee.CharField()
    address = peewee.CharField()
    age = peewee.SmallIntegerField()


class Guilder(BaseModel):
    guilder_id = peewee.AutoField()
    name = peewee.CharField(max_length=55)
    charge_per_hour = peewee.DecimalField()
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
    camper_id = peewee.ForeignKeyField(Camper,related_name="camper_details1")
    camper_owner_id = peewee.ForeignKeyField(CampsiteOwner,related_name="campsite_owner_id1")


class Video(BaseModel):
    video_id = peewee.AutoField()
    type = peewee.CharField(max_length=55)
    update_date = peewee.DateField()
    camper_id = peewee.ForeignKeyField(Camper,related_name="camper_details2")
    camper_owner_id = peewee.ForeignKeyField(CampsiteOwner,related_name="campsite_owner_id2")


class Photo(BaseModel):
    photo_id = peewee.AutoField()
    type = peewee.CharField(max_length=55)
    update_date = peewee.DateField()
    camper_id = peewee.ForeignKeyField(Camper,related_name="camper_details3")
    camper_owner_id = peewee.ForeignKeyField(CampsiteOwner,related_name="campsite_owner_id3")


class Campsite_Package(BaseModel):
    package_id = peewee.AutoField()
    name = peewee.CharField(max_length=55)
    price = peewee.DecimalField()
    camper_id = peewee.ForeignKeyField(Camper,related_name="camper_details4")


class Announcement(BaseModel):
    announcement_id = peewee.AutoField()
    content = peewee.CharField()
    dates = peewee.DateField()
    times = peewee.TimeField()
    camper_owner_id = peewee.ForeignKeyField(CampsiteOwner,related_name="campsite_owner_id4")


class Review(BaseModel):
    review_id = peewee.AutoField()
    content = peewee.CharField()
    dates = peewee.DateField()
    times = peewee.TimeField()
    camper_id = peewee.ForeignKeyField(Camper,related_name="camper_details5")


class Campsite(BaseModel):
    campsite_id = peewee.AutoField()
    name = peewee.CharField(max_length=55)
    address = peewee.CharField()
    location = peewee.CharField(max_length=55)
    email = peewee.CharField()
    contact_number = peewee.CharField()
    camper_id = peewee.ForeignKeyField(Camper,related_name="camper_details6")
    camper_owner_id = peewee.ForeignKeyField(CampsiteOwner,related_name="campsite_owner_id5")

class CamperCampSite(BaseModel):
    camper_id = peewee.ForeignKeyField(Camper)
    camper_owner_id = peewee.ForeignKeyField(CampsiteOwner)


class CamperEvent(BaseModel):
    camper_id = peewee.ForeignKeyField(Camper)
    event_id = peewee.ForeignKeyField(Event)


class CampsitePackageGuider(BaseModel):
    package_id = peewee.ForeignKeyField(Campsite_Package)
    guilder_id = peewee.ForeignKeyField(Guilder)


class CampsitePackageTransport(BaseModel):
    package_id = peewee.ForeignKeyField(Campsite_Package)
    vehicle_details = peewee.ForeignKeyField(TransPort)


class CampsitePackageDriver(BaseModel):
    package_id = peewee.ForeignKeyField(Campsite_Package)
    driver_id = peewee.ForeignKeyField(Driver)


class CampsitePackageEqipment(BaseModel):
    package_id = peewee.ForeignKeyField(Campsite_Package)
    equipment_id = peewee.ForeignKeyField(Equipment)


class CampsitePackageMeal(BaseModel):
    package_id = peewee.ForeignKeyField(Campsite_Package)
    meal_id = peewee.ForeignKeyField(Meal)


class AdminReview(BaseModel):
    admin_id = peewee.ForeignKeyField(Admin,null=True)
    review_id = peewee.ForeignKeyField(Review)




# Admin.create_table(safe=True)
# CampsiteOwner.create_table(safe=True)
# Camper.create_table(safe=True)
# Guilder.create_table(safe=True)
# TransPort.create_table(safe=True)
# Meal.create_table(safe=True)
# Driver.create_table(safe=True)
# Equipment.create_table(safe=True)
# Event.create_table(safe=True)
# Video.create_table(safe=True)
# Photo.create_table(safe=True)
# Campsite_Package.create_table(safe=True)
# Announcement.create_table(safe=True)
# Review.create_table(safe=True)
# Campsite.create_table(safe=True)
# CamperCampSite.create_table(safe=True)
# CamperEvent.create_table(safe=True)
# CampsitePackageGuider.create_table(safe=True)
# CampsitePackageTransport.create_table(safe=True)
# CampsitePackageDriver.create_table(safe=True)
# CampsitePackageEqipment.create_table(safe=True)
# CampsitePackageMeal.create_table(safe=True)
# AdminReview.create_table(safe=True)
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

# Admin Add CampSite Start
class Admin(BaseModel):
    user_id = peewee.AutoField()
    first_name = peewee.CharField(max_length=25)
    last_name = peewee.CharField(max_length=25)
    email = peewee.CharField(max_length=55,unique=True)
    contact_number = peewee.CharField(max_length=15)
    password = peewee.CharField(max_length=10)
class CampSite(BaseModel):
    campsite_id = peewee.AutoField()
    name = peewee.CharField(max_length=55)
    address = peewee.CharField()
    location = peewee.CharField(max_length=55)
    contact_number = peewee.CharField(max_length=15)
    email = peewee.CharField(max_length=55,unique=True)
    admin = peewee.ForeignKeyField(Admin,related_name="admin_details")
# Admin Add CampSite End
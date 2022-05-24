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
    host='db.obkjeuaammnhmifnnyyh.supabase.co',
)

class BaseModel(peewee.Model):
    class Meta:
        database=db

class Admin(BaseModel):
    user_id = peewee.AutoField()
    first_name = peewee.CharField()
    last_name = peewee.CharField()
    email = peewee.CharField()
    contact_number = peewee.CharField()
    password = peewee.CharField()

class CampSite(BaseModel):
    campsite_id = peewee.AutoField()
    name = peewee.CharField()
    address = peewee.CharField()
    location = peewee.CharField()
    contact_number = peewee.CharField()
    email = peewee.CharField()
    admin = peewee.ForeignKeyField(Admin,related_name="admin_details")

class Review(BaseModel):
    review_id = peewee.AutoField()
    content = peewee.CharField()
    time = peewee.TimeField(default=datetime.datetime.now().time())
    date = peewee.DateField(default=datetime.date.today())

class AdminReview(BaseModel):
    admin = peewee.ForeignKeyField(Admin)
    review = peewee.ForeignKeyField(Review)
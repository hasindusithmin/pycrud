import peewee
from dotenv import load_dotenv
import os
load_dotenv()
db = peewee.PostgresqlDatabase(
    'postgres',
    user='postgres',
    password=os.getenv('PASSWORD'),
    host='db.obkjeuaammnhmifnnyyh.supabase.co',
)

print(db.connect())
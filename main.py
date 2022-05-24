from model import (Admin,CampSite,Review,AdminReview)
from faker import Faker
import uuid0
from playhouse.shortcuts import model_to_dict
fake = Faker()
# Admin.create_table()
# CampSite.create_table()
# Review.create_table()
# AdminReview.create_table()
# admin = Admin.create(
#     first_name = fake.first_name(),
#     last_name = fake.last_name(),
#     email = fake.email(),
#     contact_number = fake.phone_number(),
#     password = uuid0.generate().base62
# )

# camp_site = CampSite.create(
#     name = fake.name(),
#     address = fake.address(),
#     location = fake.city(),
#     contact_number = fake.phone_number(),
#     email = fake.email(),
#     admin = admin
# )

# review = Review.create(
#     content = fake.text()
# )

# AdminReview.create(
#     admin = admin,
#     review = review
# )

# camp_site =  CampSite.get(CampSite.campsite_id == 1)
# print(model_to_dict(camp_site))




from faker import Faker
from faker.providers import profile


fake = Faker()
def make_profiles():
    profiles = []
    for i in range(10):
        profiles.append(fake.profile())
    return profiles
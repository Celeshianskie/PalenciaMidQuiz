import requests
import json
from faker import Faker
from webexteamssdk import WebexTeamsAPI

fake = Faker()    

for _ in range(10):
    print(f"Name: {fake.name{}}")
    
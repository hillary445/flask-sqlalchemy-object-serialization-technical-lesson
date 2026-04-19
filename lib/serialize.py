# lib/serialize.py
from pprint import pprint
from marshmallow import Schema, fields

# model

class Dog:
    def __init__(self, name, breed, tail_wagging = False):
        self.name = name
        self.breed = breed
        self.tail_wagging = tail_wagging

# create model instance
class DogSchema(Schema):
    name = fields.String()
    breed = fields.String()
    tail_wagging = fields.Boolean()

dogs = [Dog(name="Snuggles", breed="Beagle", tail_wagging=True),
       Dog(name="Wags", breed="Collie", tail_wagging=False)]

dictionary_list = DogSchema(many=True).dumps(dogs)
print(dictionary_list)
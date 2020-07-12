# @time     : 2020/7/12 17:45
# @author  : HerbLee
# @file    : user.py.py

from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    text = fields.TextField()
    created = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.name
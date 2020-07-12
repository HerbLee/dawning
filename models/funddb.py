# @time     : 2020/7/12 17:22
# @author  : HerbLee
# @file    : funddb.py

from tortoise.models import Model
from tortoise import fields

class FundDb(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField() # 基金名称
    code = fields.TextField() # 基金代码

    text = fields.TextField()
    created = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.name

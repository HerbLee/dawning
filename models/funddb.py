# @time     : 2020/7/12 17:22
# @author  : HerbLee
# @file    : funddb.py

from tortoise.models import Model
from tortoise import fields


class FundDb(Model):
    """
    基金数据库
    """
    id = fields.IntField(pk=True)
    name = fields.TextField()  # 基金名称
    code = fields.CharField(unique=True, max_length=20)  # 基金代码
    created = fields.DatetimeField(auto_now_add=True)

    cf: fields.ReverseRelation["CurrentFund"]

    def __str__(self):
        return self.name


class CurrentFund(Model):
    id = fields.IntField(pk=True)
    code: fields.ForeignKeyRelation[FundDb] = fields.ForeignKeyField('models.FundDb', related_name='cf', to_field="code")
    # code = fields.TextField()  # 基金代码
    price = fields.FloatField()  # 净值
    cost = fields.FloatField()  # 单位成本
    nums = fields.FloatField()  # 可用份额

    created = fields.DatetimeField(auto_now_add=True)
    modify = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.name

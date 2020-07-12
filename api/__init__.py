# @time     : 2020/7/12 23:30
# @author  : HerbLee
# @file    : __init__.py
from sanic import Blueprint

from .finance import finance

api = Blueprint.group(finance, url_prefix="/api")


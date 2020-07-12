# @time     : 2020/7/12 23:31
# @author  : HerbLee
# @file    : __init__.py

from sanic import Blueprint

from .fund import fund

finance = Blueprint.group(fund, url_prefix="/finance")

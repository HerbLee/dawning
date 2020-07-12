# @time     : 2020/7/12 16:35
# @author  : HerbLee
# @file    : finance.py

from sanic import Blueprint
from sanic.response import text

fund = Blueprint("fund", url_prefix="/fund")

@fund.route("/get_data")
async def get_v2_data(request):
    return text("it is finance")


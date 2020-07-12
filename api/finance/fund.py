# @time     : 2020/7/12 16:35
# @author  : HerbLee
# @file    : finance.py

from sanic import Blueprint
from sanic.response import text
from models.funddb import FundDb, CurrentFund

fund = Blueprint("fund", url_prefix="/fund")


@fund.route("/get_data")
async def get_v2_data(request):
    return text("it is finance")


@fund.route("/add", methods=["POST",])
async def add_fund(request):
    datas = request.form
    # await FundDb.create(name=datas['name'][0], code=datas['code'][0],
    #                     price=float(datas['price'][0]), cost=float(datas['cost'][0]), nums=float(datas['nums'][0]))
    res = await FundDb.filter(code=datas['code'][0])
    if not res:
        fdb = await FundDb.create(name=datas['name'][0], code=datas['code'][0])

    await CurrentFund.create(code=res[0] if res else fdb, price=float(datas['price'][0]), cost=float(datas['cost'][0]), nums=float(datas['nums'][0]))
    return text("success")
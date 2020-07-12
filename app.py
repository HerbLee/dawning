# @time     : 2020/7/12 16:12
# @author  : HerbLee
# @file    : app.py


from sanic import Sanic
from jinja2 import Environment, PackageLoader, select_autoescape
from tortoise.contrib.sanic import register_tortoise
from util.config_utils import get_mysql_data, init
from sanic import response
from api import api


from util.log import log

import os


app = Sanic(__name__)
app.static('/favicon.ico', './static/favicon.ico')

"""
init utils
"""
init(os.path.abspath("."))


"""
init router
"""
app.blueprint(api)


"""
inti mysql
"""
register_tortoise(
    app,
    db_url="mysql://{}:{}@{}:{}/{}?maxsize={}&minsize={}".format(get_mysql_data()['user'],
                                                                 get_mysql_data()['password'],
                                                                 get_mysql_data()['host'],
                                                                 get_mysql_data()['port'],
                                                                 get_mysql_data()['dbname'],
                                                                 get_mysql_data()['maxsize'],
                                                                 get_mysql_data()['minsize']),
    modules={"models": ["models.{}".format(item.replace('.py', '')) for item in os.listdir("./models") if item.endswith(".py")]},
    generate_schemas=False
)

env = Environment(
    loader=PackageLoader(__name__, 'templates')
)


@app.middleware("request")
async def print_on_request(request):
    log.info("user {} request {} ".format(request.ip, request.path))




@app.route("/")
async def index(request):
    return response.html(env.get_template("index.html").render())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001)

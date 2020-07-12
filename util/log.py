# @time     : 2020/7/12 18:30
# @author  : HerbLee
# @file    : log.py
import logging
import os
apath = os.path.abspath(".")




log = logging.getLogger(__name__)
log.setLevel(level=logging.INFO)
handler = logging.FileHandler("{}/log/log.txt".format(apath))
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

log.addHandler(handler)
log.addHandler(console)






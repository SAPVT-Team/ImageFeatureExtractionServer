# -*- coding:utf-8 -*-
from flask import Blueprint

app = Blueprint('main', __name__)

from . import views
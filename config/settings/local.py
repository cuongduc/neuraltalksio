# -*- coding: utf-8 -*-
"""
Local settings
"""
import os
from .base import *

DEBUG = config('DEBUG', default=True, cast=bool)
SECRET_KEY = config('SECRET_KEY')

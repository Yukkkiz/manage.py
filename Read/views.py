import os
import logger
import sql as sql
import xlrd
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from xlrd import xldate_as_datetime
import  pandas as pd
import numpy as np
from django import forms
from django.core.exceptions import ValidationError
from Read import models
from Yongqi import settings

# Create your views here.

def Read(request):
    return render(request, 'Read.html')


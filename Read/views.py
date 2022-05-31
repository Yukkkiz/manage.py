import os
import logger
import sql as sql
import xlrd
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from xlrd import xldate_as_datetime
import pandas as pd
import numpy as np
from django import forms
from django.core.exceptions import ValidationError
from Read import models
from Yongqi import settings


# Create your views here.

def Read(request):
    return render(request, 'Read.html')


def upload_file(request):
    # 请求方法为POST时，进行处理
    if request.method == "POST":
        # 获取上传的文件，如果没有文件，则默认为None
        File = request.FILES.get("uploadfile", None)
        if File is None:
            return HttpResponse("没有需要上传的文件")
        else:
            # 打开特定的文件进行二进制的写操作
            # print(os.path.exists('/temp_file/'))
            with open("./temp_file/%s" % File.name, 'wb+') as f:
                # 分块写入文件
                for chunk in File.chunks():
                    f.write(chunk)
            return HttpResponse("Upload over!")
    else:
        return render(request, "Read.html")

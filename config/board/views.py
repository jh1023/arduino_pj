from django.shortcuts import render
from board.models import Board
from board.models import BSensor
from board.models import SensorData

from django.shortcuts import redirect
from django.db import connection
import pymysql

from django.db.models import Count, Q

##그래프 
from django.shortcuts import render
import json
from time import mktime, strptime
from datetime import datetime, timedelta, date

#api
from .ecubelab_test2 import *
from .weather_add import *


# # SQL Alchemy part
# from sqlalchemy import create_engine, select
# DB_URL = 'mysql+mysqldb://root:intra165@ㅣlocalhost:3306/edudb?charset=utf8'
# engine = create_engine(DB_URL)
# from sqlalchemy.orm import sessionmaker
#
# Session = sessionmaker()
# sess = Session()

def home(request):
    return render(request, "home.html")

def board(request): #게시판
    rsBoard = Board.objects.all()
    # print(rsBoard)

    return render(request, "board_list.html", {
        'rsBoard': rsBoard
    })

def board_write(request): #글쓰기
    return render(request, "board_write.html", )

def board_insert(request): 
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    if btitle != "":
        rows = Board.objects.create(b_title=btitle, b_note=bnote, b_writer=bwriter)
        return redirect('/board')
    else:
        return redirect('/board_write')

def board_view(request): #자세히보기
    bno = request.GET['b_no']
    rsDetail = Board.objects.filter(b_no=bno)

    return render(request, "board_view.html", {
        'rsDetail': rsDetail
    })

def board_edit(request):
    bno = request.GET['b_no']
    rsDetail = Board.objects.filter(b_no=bno)

    return render(request, "board_edit.html", {
        'rsDetail': rsDetail
    })


def board_update(request): #수정
    bno = request.GET['b_no']
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    try:
        board = Board.objects.get(b_no=bno)
        if btitle != "":
            board.b_title = btitle
        if bnote != "":
            board.b_note = bnote
        if bwriter != "":
            board.b_writer = bwriter

        try:
            board.save()
            return redirect('/board')
        except ValueError:
            return Response({"success": False, "msg": "에러입니다."})

    except ObjectDoesNotExist:
        return Response({"success": False, "msg": "게시글 없음"})

def board_delete(request): #삭제
    bno = request.GET['b_no']
    rows = Board.objects.get(b_no=bno).delete()

    return redirect('/board')


##
def sensor_view(request): #센서데이터 보기
    bsensor = BSensor.objects.last()
    context = {'bsensor':bsensor}

    return render(request, "sensor_view.html",context)  


###################################### 그래프
def charts_test(request):
    h_var = 's_no'
    v_var = 's_data'

    data = [[h_var,v_var]]
    #data =[]
    #data.append(BSensor.objects.all().order_by('s_no')[0:20])
    candidates = BSensor.objects.all().order_by('s_no')  #마지막부터 
    #candidates = BSensor.objects.values('s_no').order_by('s_no')[0:20]  #s_no 데이터만!!
    ###candidates = data.append(BSensor.objects.values('s_no').order_by('s_no')[0:20])  #s_no 데이터만!!
    for i in candidates:         
        data.append([i.s_no, i.s_data])#

    h_var_JSON = json.dumps(h_var)
    v_var_JSON = json.dumps(v_var)

    modified_data = json.dumps(data)

    return render(request,"charts.html",{'values':modified_data,\
        'h_title':h_var_JSON,'v_title':v_var_JSON,'candidates':candidates})       

#########################################
# 

def sensor_data(request):
    h_var = 'X'
    v_var = 'Y'
    data = [[h_var,v_var]]

    today = date.today()
    first_day = today.replace(day=1) #지금달 첫번째 날 ex) 1월1일
    last_day_month_ago = first_day - timedelta(days=1) #전달의 마지막날 구하기
    first_day_month_ago = last_day_month_ago.replace(day=1) #전달의 첫번째날구하기

    #enddate = startdate + timedelta(days=90)
    #candidates= SensorData.objects.filter(s_date__range=[first_day_month_ago, first_day])
    
    
    candidates = SensorData.objects.all().order_by('-s_no')
    #candidates = SensorData.objects.all().order_by('-s_no')[0:144]
    #최근 하루 데이터
    
    for i in candidates:         
        data.append([i.x, i.y])  #

    h_var_JSON = json.dumps(h_var)
    v_var_JSON = json.dumps(v_var)

    modified_data = json.dumps(data)

    return render(request,"sensor_chart.html",{'values':modified_data,\
        'h_title':h_var_JSON,'v_title':v_var_JSON}) 

def dust_checker(request):
    # api 프린트
    postList = print_wether
    postList2 = print_ecube_test

    #context = {'postList': postList}
    #context2={'postList2': print_ecube_test}
    #print(postList)
    return render(request, 'dust_main.html',{'postList': postList,'postList2': postList2})    

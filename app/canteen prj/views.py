# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app1.models import *
from django.http import HttpResponse,JsonResponse
from random import random
from django.core.files.storage import FileSystemStorage
import random
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.core.mail import EmailMessage

from django.core.files.storage import FileSystemStorage

from datetime import datetime
from .models import*
import pyqrcode
import png
from pyqrcode import QRCode
import random
import requests
import cv2



@csrf_exempt
def Student_reg(request):
    name=request.POST.get("name")
    phone=request.POST.get("phone")
    addr=request.POST.get("addr")
    batch=request.POST.get("batch")
 
    
    uname=request.POST.get("usnm")
    pswrd=request.POST.get("psw")


    print(name,phone,addr,batch,uname,pswrd)
    response_data={}
    try:
        ob=Student_table(Name=name,Phone=phone,Address=addr,Batch=batch,Username=uname,Pswrd=pswrd)
        ob.save()

        response_data['msg'] = "yes"
    except:
        response_data['msg'] = "no"
    return JsonResponse(response_data)


@csrf_exempt
def Canteen_reg(request):
    name=request.POST.get("name")
    phone=request.POST.get("phone")
    addr=request.POST.get("addr")
    cname=request.POST.get("cname")
 
    
    uname=request.POST.get("usnm")
    pswrd=request.POST.get("psw")


    print(name,phone,addr,cname,uname,pswrd)
    response_data={}
    try:
        ob=Canteen_table(Cname=cname,Owname=name,Phone=phone,Address=addr,Username=uname,Pswrd=pswrd)
        ob.save()

        response_data['msg'] = "yes"
    except:
        response_data['msg'] = "no"
    return JsonResponse(response_data)




@csrf_exempt
def Update_canteen(request):
    cid=request.POST.get("cid")
    name=request.POST.get("name")
    phone=request.POST.get("phone")
    addr=request.POST.get("addr")
    cname=request.POST.get("cname")
 
    
    uname=request.POST.get("usnm")
    pswrd=request.POST.get("psw")


    print(name,phone,addr,cname,uname,pswrd)
    response_data={}
    try:
        ob=Canteen_table.objects.get(id=int(cid))
        ob.Cname=cname
        ob.Owname=name
        ob.Phone=phone
        ob.Address=addr
        ob.Username=uname
        
        ob.Pswrd=pswrd
        ob.save()

        response_data['msg'] = "yes"
    except:
        response_data['msg'] = "no"
    return JsonResponse(response_data)




@csrf_exempt
def Delete_canteen(request):
    cid=request.POST.get("cid")
    
    response_data={}
    try:
        ob=Canteen_table.objects.get(id=int(cid))
        
        ob.delete()

        response_data['msg'] = "yes"
    except:
        response_data['msg'] = "no"
    return JsonResponse(response_data)






@csrf_exempt
def Update_student(request):
    cid=request.POST.get("cid")
    name=request.POST.get("name")
    phone=request.POST.get("phone")
    addr=request.POST.get("addr")
    batch=request.POST.get("batch")
 
    
    uname=request.POST.get("usnm")
    pswrd=request.POST.get("psw")


    print(name,phone,addr,batch,uname,pswrd)
    response_data={}
    try:
        ob=Student_table.objects.get(id=int(cid))
        ob.Name=name
        ob.Batch=batch
        ob.Phone=phone
        ob.Address=addr
        ob.Username=uname
        
        ob.Pswrd=pswrd
        ob.save()

        response_data['msg'] = "yes"
    except:
        response_data['msg'] = "no"
    return JsonResponse(response_data)



@csrf_exempt
def Delete_student(request):
    cid=request.POST.get("cid")
    
    response_data={}
    try:
        ob=Student_table.objects.get(id=int(cid))
        
        ob.delete()

        response_data['msg'] = "yes"
    except:
        response_data['msg'] = "no"
    return JsonResponse(response_data)


@csrf_exempt
def CheckLogin(request):
    uname=request.POST.get("uname")
    pswrd=request.POST.get("pswrd")
    utype=request.POST.get("utype")

    
    print(uname,pswrd)
    
    if(utype=="Canteen"):
        try:
            ob=Canteen_table.objects.get(Username=uname,Pswrd=pswrd)
         
            
            data={"msg":"Canteen"}
            return JsonResponse(data,safe=False)
        except:
            data={"msg":"no"}
            return JsonResponse(data,safe=False)
    else:
        try:
            ob=Student_table.objects.get(Username=uname,Pswrd=pswrd)
         
            
            data={"msg":"Student"}
            return JsonResponse(data,safe=False)
        except:
            data={"msg":"no"}
            return JsonResponse(data,safe=False)    



@csrf_exempt
def getallcanteen(request):
    
    resplist=[]
    respdata={}
    ob=Canteen_table.objects.all()
    
    resplist=[]
    respdata={}
    for i in ob:
        data={}
      

        data["cid"]=i.id
        data["cname"]=i.Cname
        data["oname"]=i.Owname
        data["phno"]=i.Phone
        data["addr"]=i.Address
        data["usernm"]=i.Username

        data["pswrd"]=i.Pswrd
       
        
        resplist.append(data)
    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)



@csrf_exempt
def getallstudents(request):
    
    resplist=[]
    respdata={}
    ob=Student_table.objects.all()
    
    resplist=[]
    respdata={}
    for i in ob:
        data={}
        data["cid"]=i.id
        data["cname"]=i.Name
        data["oname"]=i.Batch
        data["phno"]=i.Phone
        data["addr"]=i.Address
        data["usernm"]=i.Username

        data["pswrd"]=i.Pswrd
  
        resplist.append(data)
    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)

@csrf_exempt
def Add_food(request):
    uname=request.POST.get("uname")
    fname=request.POST.get("fname")
    fdes=request.POST.get("fdes")
    ftype=request.POST.get("ftype")
    fprc=request.POST.get("fprc")
 
    
    ftme=request.POST.get("ftme")
    fdate=request.POST.get("fdate")


    response_data={}
    try:
        ob=Food_table.objects.get(Cusername=uname,Date=fdate,Fname=fname)


        response_data['msg'] = "no"


    except:
        ob=Food_table(Cusername=uname,Date=fdate,Fname=fname,Finfo=fdes,Price=fprc,Time=ftme,Ftype=ftype,Status="1")
        ob.save()
        response_data['msg'] = "yes"
    return JsonResponse(response_data)


@csrf_exempt
def Canteen_view_food(request):
    uname=request.POST.get("uname")
    fdate=request.POST.get("fdate")
    resplist=[]
    respdata={}
    ob=Food_table.objects.filter(Cusername=uname,Date=fdate)
    
    resplist=[]
    respdata={}
    for i in ob:
        data={}
        data["fid"]=i.id
        data["fname"]=i.Fname
        data["fdes"]=i.Finfo
        data["fprc"]=i.Price
        data["ftme"]=i.Time
        data["ftyp"]=i.Ftype
        if(i.Status=="0"):
            fsts="Not available"
        else:
            fsts="Available"
        data["fsts"]=fsts

  
        resplist.append(data)

    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)



@csrf_exempt
def Update_food_details(request):
    fid=request.POST.get("fid")
    fname=request.POST.get("fname")
    fdes=request.POST.get("fdes")
    ftype=request.POST.get("ftype")
    fprc=request.POST.get("fprc")
 
    
    ftme=request.POST.get("ftme")
    


    response_data={}
    try:
        ob=Food_table.objects.get(id=int(fid))
        ob.Fname=fname
        ob.Finfo=fdes
        ob.Price=fprc
        ob.Time=ftme
        ob.Ftype=ftype
        ob.save()
        response_data['msg'] = "yes"


    except:
 
        response_data['msg'] = "no"
    return JsonResponse(response_data)


@csrf_exempt
def Disable_food(request):
    fid=request.POST.get("fid")
    
    response_data={}
    try:
        ob=Food_table.objects.get(id=int(fid))
        fsts=ob.Status
        if(fsts=="0"):
            ob.Status="1"
            ob.save()
        else:
            ob.Status="0"
            ob.save()
        response_data['msg'] = "yes"


    except:
 
        response_data['msg'] = "no"
    return JsonResponse(response_data)

@csrf_exempt
def Delete_food(request):
    fid=request.POST.get("fid")
    
    response_data={}
    try:
        ob=Food_table.objects.get(id=int(fid))
        ob.delete()
        
        response_data['msg'] = "yes"


    except:
 
        response_data['msg'] = "no"
    return JsonResponse(response_data)



@csrf_exempt
def Get_canteendetails(request):
 
    resplist=[]
    respdata={}
    ob=Canteen_table.objects.all()
    
    resplist=[]
    respdata={}
    for i in ob:
        data={}
        data["cname"]=i.Cname
        data["username"]=i.Username
  
        resplist.append(data)

    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)



@csrf_exempt
def Student_view_food(request):
    uname=request.POST.get("cname")
    fdate=request.POST.get("fdate")
    # ftyp=request.POST.get("ftyp")
    print(uname)
    print(fdate)
    
    resplist=[]
    respdata={}
    ob=Food_table.objects.filter(Cusername=uname,Date=fdate)
    
    resplist=[]
    respdata={}
    for i in ob:
        data={}
        data["fid"]=i.id
        data["fname"]=i.Fname
        data["fdes"]=i.Finfo
        data["fprc"]=i.Price
        data["ftme"]=i.Time
        data["ftyp"]=i.Ftype
        
        if(i.Status=="0"):
            fsts="Not available"
        else:
            fsts="Available"
        data["fsts"]=fsts

  
        resplist.append(data)

    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)

from datetime import date


@csrf_exempt
def Food2cart(request):

    fid=request.POST.get("fid")
    sname=request.POST.get("sname")
    fqty=request.POST.get("fqty")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    print("d1 =", d1)

    response_data={}
    try:
        ob=Bucket_table.objects.get(Foodid=fid,Sname=sname,Date=d1)
        
        response_data['msg'] = "exist"


    except:
        ob=Food_table.objects.get(id=int(fid))
        fname=ob.Fname
        fprc=ob.Price
        cname=ob.Cusername
        total=int(fqty)*int(fprc)
        ob1=Bucket_table(Foodid=fid,Fname=fname,Quantity=fqty,Price=total,Date=d1,Sname=sname,Cusernm=cname)
        ob1.save()
        response_data['msg'] = "yes"
    return JsonResponse(response_data)


@csrf_exempt
def Remove_food(request):

    fid=request.POST.get("fid")
    sname=request.POST.get("sname")

    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    print("d1 =", d1)

    response_data={}
    print(fid)
    print(sname)
    print(d1)
    try:
        ob=Bucket_table.objects.filter(Foodid=fid,Sname=sname,Date=d1)
        for i in ob:

            i.delete()
        response_data['msg'] = "yes"


    except:
    
        response_data['msg'] = "no"
    return JsonResponse(response_data)



@csrf_exempt
def Getmybucket(request):
  
    sname=request.POST.get("sname")
  
    print(sname)
    resplist=[]
    respdata={}
    ob=Bucket_table.objects.filter(Sname=sname)
    cantlist=[]
    for i in ob:
        cname=i.Cusernm
        if(cname not in cantlist):
            cantlist.append(cname)
    print("canteen list==>",cantlist)
    if(len(cantlist)!=0):
        for k in cantlist:
            obx=Bucket_table.objects.filter(Cusernm=k,Sname=sname)
            obc=Canteen_table.objects.get(Username=k)
            Canteen=obc.Cname
            items=""
            prices=""
            total=0
            qty=""
            for j in obx:
                items+=j.Fname+","
                prices+=j.Price+","
                total+=int(j.Price)
                qty+=j.Quantity+","
            data={}
            data["foods"]=items[:-1]
            data["prices"]=prices[:-1]
            data["qts"]=qty[:-1]
            data["total"]=total
            data["Canteen"]=Canteen
            data["cname"]=k
            resplist.append(data)
    print(resplist)
    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)

from datetime import datetime
@csrf_exempt
def Confirm_order(request):

    cname=request.POST.get("cname")
    sname=request.POST.get("uname")

    today = date.today()
    now=datetime.now()
    d1 = today.strftime("%d/%m/%Y")
    d2 = now.strftime("%d-%m-%Y-%H-%M-%S")
    print("d1 =", d1)

    response_data={}
  

    print(sname)
    print(cname)
    try:
        obc=Canteen_table.objects.get(Username=cname)
        canteen=obc.Cname
        obx=Bucket_table.objects.filter(Cusernm=cname,Sname=sname)
        resptxt="======================"+canteen+"======================\n\n"
        resptxt+="Date : "+d1+"\n\n"
        resptxt+="     Item          Quantity          price\n"
        
        items=""
        prices=""
        total=0
        qty=""
        for j in obx:
            tval="     "
            items+=j.Fname+","
            tval+=j.Fname+"     "
            prices+=j.Price+","
            total+=int(j.Price)
            qty+=j.Quantity+","
            tval+=j.Quantity+"     "
            tval+=j.Price+"\n"
            resptxt+=tval
            j.delete()

        resptxt+="     Grand Total: "+str(total)
        print(resptxt)
        number = random.randint(111111,999999)
        print(number)
        
        # String which represents the QR code
        scode = str(number)
        
        # Generate QR code
        url = pyqrcode.create(scode)
        
        qrpath="qrimages/"+sname+d2+".png"
        # Create and save the png file naming "myqr.png"
        url.png(qrpath, scale = 6)

        obs=Purchase_table(Cusernm=cname,Fooditems=items[:-1],Quantity=qty[:-1],Price=prices[:-1],Total=str(total),
        Date=d1,Sname=sname,Secretid=scode,Qrpath=qrpath)
        obs.save()
        print("saved")
        response_data['msg'] = "yes"
        response_data["fname"]="Bill"+d2+".txt"
        response_data["bill"]=resptxt


    except Exception as e:
        print(e)
    
        response_data['msg'] = "no"
    return JsonResponse(response_data)

@csrf_exempt
def Cancel_order(request):

    cname=request.POST.get("cname")
    sname=request.POST.get("uname")

    

    
    response_data={}

    print(sname)
    print(cname)
    try:
        obx=Bucket_table.objects.filter(Cusernm=cname,Sname=sname)
      
        items=""
        prices=""
        total=0
        qty=""
        for j in obx:

            j.delete()


        response_data['msg'] = "yes"


    except Exception as e:
        print(e)
    
        response_data['msg'] = "no"
    return JsonResponse(response_data)

import base64


@csrf_exempt
def Student_my_orders(request):
  
    sname=request.POST.get("sname")
  
    print(sname)
    resplist=[]
    respdata={}
    ob=Purchase_table.objects.filter(Sname=sname,Status="Orderd")
    for j in ob:
        fname=j.Fooditems
        fqty=j.Quantity
        ftotal=j.Total
        date=j.Date
        impath=j.Qrpath
        cname=j.Cusernm
        obc=Canteen_table.objects.get(Username=cname)
        cantname=obc.Cname
        status=j.Status
        data={}
        data["fname"]=fname
        data["fqty"]=fqty
        data["ftotal"]=ftotal
        data["fdate"]=date
        data["cname"]=cantname
        data["status"]=status
        with open(impath, "rb") as img_file:
            b64_string = base64.b64encode(img_file.read())
        data["imgstr"]=b64_string.decode("utf-8")
        resplist.append(data)
    print(resplist)
    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)




@csrf_exempt
def Student_my_history(request):
  
    sname=request.POST.get("sname")
  
    print(sname)
    resplist=[]
    respdata={}
    ob=Purchase_table.objects.filter(Sname=sname)
    for j in ob:
        fname=j.Fooditems
        fqty=j.Quantity
        ftotal=j.Total
        date=j.Date
        impath=j.Qrpath
        cname=j.Cusernm
        obc=Canteen_table.objects.get(Username=cname)
        cantname=obc.Cname
        status=j.Status
        data={}
        data["fname"]=fname
        data["fqty"]=fqty
        data["ftotal"]=ftotal
        data["fdate"]=date
        data["cname"]=cantname
        data["status"]=status
        
        resplist.append(data)
    print(resplist)
    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)



@csrf_exempt
def Get_order(request):

    qrno=request.POST.get("qrno")
    uname=request.POST.get("uname")
    print(qrno)
    print(uname)
    response_data={}

    try:
        obx=Purchase_table.objects.get(Secretid=qrno,Cusernm=uname)
        fname=obx.Fooditems
        fqty=obx.Quantity
        ftotal=obx.Total
        date=obx.Date

        response_data['msg'] = "yes"
        response_data['fname'] = fname
        response_data['fqty'] = fqty
        response_data['ftotal'] = ftotal
        response_data['osts'] = obx.Status
        response_data['date'] = date


    except Exception as e:
        print(e)
    
        response_data['msg'] = "no"
    return JsonResponse(response_data)


@csrf_exempt
def Approve_order(request):

    qrno=request.POST.get("qrno")
    print(qrno)
    response_data={}

    try:
        obx=Purchase_table.objects.get(Secretid=qrno)
        obx.Status="Deliverd"
        obx.save()
        print("updated")
        response_data['msg'] = "yes"

    except Exception as e:
        print(e)
    
        response_data['msg'] = "no"
    return JsonResponse(response_data)



@csrf_exempt
def Canteen_my_orders(request):
  
    sname=request.POST.get("sname")
  
    print(sname)
    resplist=[]
    respdata={}
    ob=Purchase_table.objects.filter(Cusernm=sname).order_by('-Status')
    for j in ob:
        fname=j.Fooditems
        fqty=j.Quantity
        ftotal=j.Total
        date=j.Date
        impath=j.Qrpath
        cname=j.Sname
        obc=Student_table.objects.get(Username=cname)
        stname=obc.Name
        status=j.Status
        data={}
        data["fname"]=fname
        data["fqty"]=fqty
        data["ftotal"]=ftotal
        data["fdate"]=date
        data["cname"]=stname
        data["status"]=status
    
        resplist.append(data)
    print(resplist)
    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)



@csrf_exempt
def Canteen_my_orders_by_date(request):
  
    sname=request.POST.get("sname")
    date=request.POST.get("date")
  
    print(sname)
    print(date)
    resplist=[]
    respdata={}
    ob=Purchase_table.objects.filter(Cusernm=sname,Date=date)
    for j in ob:
        fname=j.Fooditems
        fqty=j.Quantity
        ftotal=j.Total
        date=j.Date
        impath=j.Qrpath
        cname=j.Sname
        obc=Student_table.objects.get(Username=cname)
        stname=obc.Name
        status=j.Status
        data={}
        data["fname"]=fname
        data["fqty"]=fqty
        data["ftotal"]=ftotal
        data["fdate"]=date
        data["cname"]=stname
        data["status"]=status
    
        resplist.append(data)
    print(resplist)
    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)

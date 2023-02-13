from django.shortcuts import render
from django.contrib import messages

# Create your views here.

import json , pickle , numpy as np 


def home(req):
    return render (req,"home.html")


def search(req):
    file_obj=open('columns.json','r')
    location_list=json.loads(file_obj.read())

    return render (req,"predict.html",location_list)

area=''

def predict(req):
    area = req.POST.get('area') 
    location = req.POST.get('location')
    sqft = req.POST.get('sqft')
    bath = req.POST.get('bath')
    bed = req.POST.get('bed')

    file_obj=open('columns.json','r')
    location_list=json.loads(file_obj.read())

    for i in location_list.values():
        li=i


    file_mod=open('model.pkl','rb')
    li_R=pickle.load(file_mod)

    def predict_price(area,location,sqft,bed,bath):
        location_ind=li.index(location)+4
        x=np.zeros(len(i)+4)
        x[0]=area
        x[1]=sqft
        x[2]=bath
        x[3]=bed
        if location_ind>=4:
            x[location_ind]=1
        return li_R.predict([x])[0]

    mes=round(predict_price(area,location,sqft,bed,bath))

    print(area,location,sqft,bath,bed)
    messages.success(req, mes)
    return render (req,"predict.html",location_list)

    


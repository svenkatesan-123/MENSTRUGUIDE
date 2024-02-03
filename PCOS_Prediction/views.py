from django.shortcuts import render
from joblib import load
model=load('PCOS_Prediction\savedmodels\model4.joblib')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def home(request):
    return render(request, 'pcosHome.html')

def predict(request):
    return render(request, 'pcosPredict.html')

def result(request):
    # data=pd.read_excel("D:\FIYA\Skills\PROJECT\ML\PCOS_data.xlsx", sheet_name=1)

    # X = data.drop("PCOS (Y/N)", axis=1)
    # Y = data["PCOS (Y/N)"]

    # X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)

    # model = LogisticRegression()
    # model.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = (request.GET['n4'])
    temp1=val4.lower()
    if(temp1=="a+"):
        val4=11
    elif(temp1=="a-"):
        val4=12
    elif(temp1=="b+"):
        val4=13
    elif(temp1=="b-"):
        val4=14
    elif(temp1=="o+"):
        val4=15
    elif(temp1=="o-"):
        val4=16
    elif(temp1=="ab+"):
        val4=17
    elif(temp1=="ab-"):
        val4=18
    else:
        return render(request, 'pcosPredict.html', {"result2":"Incorrect inputs"})
   
    
    
    val5 = (request.GET['n5'])
    temp2=val5.lower()
    if(temp2=="regular"):
        val5=2
    elif(temp2=="irregular"):
        val5=4
    else:
        return render(request, 'pcosPredict.html', {"result2":"Incorrect inputs"})

    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = (request.GET['n8'])
    temp3=val8.lower()
    if(temp3=="yes"):
        val8=1
    elif(temp3=="no"):
        val8=0
    else:
        return render(request, 'pcosPredict.html', {"result2":"Incorrect inputs"})
    val9 = float(request.GET['n9'])
    val10 = float(request.GET['n10'])
    val11 = float(request.GET['n11'])
    val12 = (request.GET['n12'])
    temp2=val12.lower()
    if(temp2=="yes"):
        val12=1
    elif(temp2=="no"):
        val12=0
    else:
        return render(request, 'pcosPredict.html', {"result2":"Incorrect inputs"})
    val13 = (request.GET['n13'])
    temp2=val13.lower()
    if(temp2=="yes"):
        val13=1
    elif(temp2=="no"):
        val13=0
    else:
        return render(request, 'pcosPredict.html', {"result2":"Incorrect inputs"})
    val14 = (request.GET['n14'])
    temp2=val14.lower()
    if(temp2=="yes"):
        val14=1
    elif(temp2=="no"):
        val14=0
    else:
        return render(request, 'pcosPredict.html', {"result2":"Incorrect inputs"})
    val15 = (request.GET['n15'])
    temp2=val15.lower()
    if(temp2=="yes"):
        val15=1
    elif(temp2=="no"):
        val15=0
    else:
        return render(request, 'pcosPredict.html', {"result2":"Incorrect inputs"})
    val16 = (request.GET['n16'])
    temp2=val16.lower()
    if(temp2=="yes"):
        val16=1
    elif(temp2=="no"):
        val16=0
    else:
        return render(request, 'pcosPredict.html', {"result2":"Incorrect inputs"})
    val17 = (request.GET['n17'])
    temp2=val17.lower()
    if(temp2=="yes"):
        val17=1
    elif(temp2=="no"):
        val17=0
    else:
        return render(request, 'pcosPredict.html', {"result2":"Incorrect inputs"})
    val18 = (request.GET['n18'])
    temp2=val18.lower()
    if(temp2=="yes"):
        val18=1
    elif(temp2=="no"):
        val18=0
    else:
        return render(request, 'pcosPredict.html', {"result2":"Incorrect inputs"})

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13, val14, val15, val16, val17, val18]])

    result1=""

    if pred==[1]:
        result1 = "You might have PCOS, Kindly consult your doctor!"
    else:
        result1 = "You do not have PCOS!"

    return render(request, 'pcosPredict.html', {"result2":result1})
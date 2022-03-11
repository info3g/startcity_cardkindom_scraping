from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

from .models import *
from APIS.serializers import StarcitygamesSerializer,cardkingdomSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import warnings,time

import mysql.connector
warnings.filterwarnings('ignore')
connection = mysql.connector.connect(host="localhost",user="root",password="",database='test')
mycursor = connection.cursor(buffered=True)
print(connection)
class SnippetList(APIView):
    def post(self, request, format=None):
        serializer = StarcitygamesSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.data['Title']
            Editions = serializer.data['Editions']
            kwargs = {'Name': str(title),'Edition':str(Editions)}
            where_clause = 'WHERE ' + ' AND '.join([' ' + k + ' = %s' for k in kwargs.keys()])
            values = tuple(kwargs.values())
            sql = "SELECT *  FROM startcity " + where_clause
            mycursor.execute(sql, values)
            myresult = mycursor.fetchall()
            print("myresultmyresultmyresult",len(myresult),myresult)
            kwargs = {'ID': str(myresult[0][0])}
            where_clause = 'WHERE ' + ' AND '.join([' ' + k + ' = %s' for k in kwargs.keys()])
            values = tuple(kwargs.values())
            sql = "SELECT *  FROM starcity " + where_clause
            mycursor.execute(sql, values)
            myresults = mycursor.fetchall()
            import json
            all_datas={}
            Append=[]
            for item in myresults:
                print(item[3].split('QTY:'))
                test =  {"Language":item[1],"Price":item[2],"QTY":item[3].split('QTY:')[1],"Database ID":item[4]}
                Append.append(test)
            print(title)
            Search = {"Database ID":myresult[0][0],"Name":title,"Edition":Editions}
            all_datas.update({"Search":Search,"Data":Append})
            return Response(all_datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SnippetList2(APIView):
    def post(self, request, format=None):
        serializer = cardkingdomSerializer(data=request.data)
        if serializer.is_valid():
            uuid = serializer.data['uuid']


            kwargs = {'uuid': str(uuid)}
            where_clause = 'WHERE ' + ' AND '.join([' ' + k + ' = %s' for k in kwargs.keys()])
            values = tuple(kwargs.values())
            sql = "SELECT *  FROM cardkingdom " + where_clause
            mycursor.execute(sql, values)
            myresult = mycursor.fetchall()
            print(myresult,"o0ooooooooooooo")
            all_datas={}
            all_datas.update({"data":myresult})

            return Response(all_datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
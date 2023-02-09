from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb as sql

#adding data from html page to database
def form(request):
    if request.method == "POST":
        try:
            conn = sql.connect(user='Dibya',passwd='dibya',db='mydb',host='192.168.30.92') 
            #here i connected remote db with above credentials
            cur = conn.cursor()
            data = request.POST
            q = "insert into employeeform_emp values{}".format(tuple(data.values())[1:]) #extracting from dict format and convert into tuple
            cur.execute(q)
            conn.commit() #saving changes to db
        except Exception as e:
            #HttpResponse(e)
            return HttpResponse('something went wrong check:'+str(e)) #errors from db
    return render(request,'empform.html')



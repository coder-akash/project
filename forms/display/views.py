from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb as sql

#by using django orm
'''
from employeeform.models import emp
def show(request):
    emps = emp.objects.all()
    print(type(emps))
    #emps = {'id':1,'name':'akash'}
    return render(request,"show.html",{'employees':emps})
'''

# extracting data from database and passing to the html page(show.html)
def show(request):
    try:
        conn = sql.connect(user='Dibya',passwd='dibya',db='mydb',host='192.168.30.92')
        cur = conn.cursor()
        cur.execute('select * from employeeform_emp')
        empslist = list(cur.fetchall())       
        return render(request,"show.html",{'employees':empslist})
    except Exception as e:
        #HttpResponse(e)
        return HttpResponse('something went wrong check:'+str(e))
 
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello world! This is home page")

def page(request):
    return HttpResponse("This is the first page!")

def subpage(request):
    return HttpResponse("This is another page!")

def httptemplate(request):
    html_ = """<!doctype html>
       <html>
       <head>
       <meta charset="utf-8">
       <title>Hello Django</title>
       </head>

       <body>
       <h1>Hello world!</h1>
       <p>This is html coming through</p>
       </body>
       </html>
    """
    return HttpResponse(html_)  # response

def renderexample(request):
    return render(request, 'simplerender.html',{})

def rendervariable(request):
    return render(request, 'vary.html',{'name':'Tuan Le', 'company':'Jogo','display':True})
def renderbase(request):
    return render(request, 'base.html',{})
def renderindex(request):
    return render(request, 'index.html',{})
def include_ex(request):
    return render(request, 'mypage.html',{'title':'The title name','current_section':'22'})
def filter_ex(request):
    return render(request, 'filter.html',{'text':"Welcome in Django",'number':2,'count':'two'})

def vonglap_ex(request):
    array_city = ['Paris', 'London', 'Washington']
    return render(request, 'loop.html',{'array_data':array_city})

def vonglap_ex2(request):

    city = ['Paris', 'London', 'Washington']
    return render(request, 'loop2.html',{'city_list':city})

class country:
    city_list=[]
def vonglap_ex3(request):
    vietnam = country()
    vietnam.city_list = ['saigoin', 'hanoi', 'danang']
    usa = country()
    usa.city_list = ['Los Angles', 'New York']
    country_list = [vietnam, usa]
    return render(request, 'loop3.html',{'countries':country_list})
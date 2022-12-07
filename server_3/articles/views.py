from django.shortcuts import render
import random

# Create your views here.
def index(request):
    names = ['복길', '복실', '복돌']
    name = random.choice(names)
    context = {
        'name' : name,
        'img' : 'https://fimg5.pann.com/new/download.jsp?FileID=64499032'
    }
    return render(request, 'index.html', context)

def welcome(request, name):
    #사람들이 /welcome/본인이름 입력시 환영인사 + 이름을 보여주는것
    context = {
        'name' : name,
        'greetings' : ['안녕', '하이', '하이영', 'ㅎㅇ'],
    }
    return render(request, 'welcome.html', context)
from django.shortcuts import render
from .models import Article
guestbook = []

# guestbook = ['안녕하세요', '반갑습니다'] .... 늘어날것.. ? 

# Create your views here.
def index(request):
    guestbook = Article.objects.all()
    #위의 뜻 : SELET * FROM Articles;
    return render(request, 'index.html', {'guestbook': guestbook})

def create(request):
    content = request.GET.get('content')
    # guestbook.append(content) 이건 그냥 리스트에 넣기. 영구저장을 하자. 
    Article.objects.create(content=content)
    return render(request, 'create.html', {'content' : content})
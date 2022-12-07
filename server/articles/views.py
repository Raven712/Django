from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # 환영하는 메인 페이지 보여줌.
    names = ['아이유', '설윤', '김채현', '송하영', '민지'] 
    name = random.choice(names)
    context = {
        'name': name,
        'img': 'https://w.namu.la/s/0f0f182dcbb699f9b1d7d2e026b8654dbc881bfacf21427fe20dca1c0557bd38ffeb0c108c070906773b0e3f16eaf85ca44ab8481804761662c5eaa6b4594653c32fe5a9ca91c1eed3540b22fca357691cbf313b65ebc4fb68d0e5a9838175209337e997ef8b09fffbb3b257a5b634ce',
    }
    # context 는 딕셔너리로.
    return render(request, 'index.html', context) # 무언가를 만들면서 끝난다는 의미 ? . 너무많이써서 위에 보듯 render가 임포트 되어있음. 여기있는 index(request) /  return render(request, ~) 이건 일종의 국룰
    # return render(request, template_name, context).
    # 이제 앱 폴더 안에 templates 폴더를 만든다. 여기선 articles 폴더 내부에. 이것도 약속임
    # 그리고 그 폴더안에 index.html을 만들어서 할거 만들면 됨

def welcome(request, name):         # name은 urls.py에서 랜덤하게 입력되는 그것.. views의 welcome 함수에서 쓰겠다는것
    # 사람들이 /welcome/본인이름 을 입력하면, 인사와 동시에 이름을 보여줌.
    
    context = {
        'name': name,
        'images': [
            'https://pbs.twimg.com/media/FWiyirnVUAEGwTx?format=jpg&name=medium',
            'https://pbs.twimg.com/profile_images/1553406441838456832/Qt18nVK8_400x400.jpg',
            'https://i.ytimg.com/vi/LTyc7mwLNys/maxresdefault.jpg',
        ],
        'greeting': [
            'hi',
            'hello',
            '구텐탁',
            'ㅎㅇ'
        ]
    }
    return render(request, 'welcome.html', context)
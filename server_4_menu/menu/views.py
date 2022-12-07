from django.shortcuts import render
import random

# Create your views here.
def dinner(request):
    menu_ = ['삼겹살', '김치볶음밥', '라면', '햄버거', '도리토스']
    menu = random.choice(menu_)

    imgs = {
        '삼겹살' : 'https://mblogthumb-phinf.pstatic.net/MjAxODAxMTFfMjQz/MDAxNTE1NjY0NTUwMTQ2.WIRsiJ0-fogoxvHZpgnnR3jWZqnTO9BfgnjIkd5iAPIg.toj9m8hOTjZfenFhxc0KlgQyzbcTOhccR3y5ft9YwVUg.PNG.sungjin972/1.png?type=w800',
        '김치볶음밥' : 'https://t1.daumcdn.net/cfile/tistory/991B203B5D6DE2E32B',
        '라면' : 'https://w.namu.la/s/9f15f198aab1b14c8aa47e96a91a9d03331ecb7b5b892c803159d39b0d77ab4be30e2f15f66191284d7dad8371989329cc1c80810745e980a6949ae5e3589df648d3e9c31177108b8ce13f860cf0d8ab3961fea6fb94407b38cdfccdcacb9866',
        '햄버거' : 'https://w.namu.la/s/126ed0de470ffd19954dde2dcdf4684286c506b774a2c1cf713c04309cf94ce26946aa03ec30a4a8a93e8e645c7bf361347807b0654a312c6e58c34e8f6bbf987bc3f8fa1e84826de00ab1c5c33dedd2e71e141441b2bd6d45208eac9e4ee785',
        '도리토스' : 'https://sitem.ssgcdn.com/73/25/65/item/1000033652573_i1_1200.jpg',
    }
    img = imgs[menu]
        
    context = {
        'menu' : menu,
        'img' : img,
    }
    return render(request, 'dinner.html', context)

def lotto(request):

    lottery_ = []
    for i in range(1, 47):
        lottery_.append(i)
    
    count = 0
    lottery = []
    while count != 6:
        if len(lottery) == 0:
            lottery.append(random.choice(lottery_))
            count += 1
        else:
            i = random.choice(lottery_)
            if i in lottery:
                continue
            else:
                lottery.append(i)
                count += 1
    
    context = {
        'lottery' : lottery,
        
    }
    return render(request, 'lottery.html', context)
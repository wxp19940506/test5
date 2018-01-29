#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import *
# Create your views here.
def index(request):
    hero = HeroInfo.objects.get(pk=1)
    context = {'hero':hero}
    print hero.hname
    return render(request,'booktest/index.html',context)


#验证码
text_temp=''

def verifyCode(request):
    global text_temp

    from PIL import Image,ImageDraw,ImageFont
    import random
    #创建背景色
    bgColor = (random.randrange(50,100),random.randrange(50,100),random.randrange(50,100))
    #规定图片宽高
    width = 100
    height = 25
    #创建画布
    image = Image.new('RGB',(width,height),bgColor)
    #构造字体对象
    font= ImageFont.truetype('FreeMono.ttf',23)
    #创建画笔
    draw = ImageDraw.Draw(image)
    #创建文本内容
    text = 'ABCD0123abcd'
    # text_temp=''
    #逐个绘制
    for i in range(4):
        text_temp1 = text[random.randrange(0,len(text))]
        text_temp+=text_temp1
        draw.text((i*25,0),text_temp1,(255,255,255),font)
    # draw.text((0,0),text,(255,255,255),font)

    request.session['code'] = text_temp
    #保存到内存流中
    import cStringIO
    buf = cStringIO.StringIO()
    image.save(buf,'png')
    #渲染
    return HttpResponse(buf.getvalue(),'image/png')

def verifyTest1(request):
    return render(request,'booktest/verifyTest1.html')
def verifyTest2(request):
    code1 = request.POST['code1']
    # code2 = request.session['code']
    if code1 == text_temp:
        return HttpResponse('OK')
    else:
        return HttpResponse('FAIL')
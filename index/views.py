#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django import forms
from index.models import Image

class UserForm(forms.Form):
	headImg = forms.ImageField()

def index(request):
    return render(request,'index.html')

def upload(request):
	return render(request,'upload_database.html')

def upload_pic(request):
	if request.method == 'POST':
		#form = UserForm(request.POST,request.FILES)
		#if form.is_valid():
		#	img = form.cleaned_data['pic']
		#	m = Image(pic=img)
		#	m.save()
		img = request.FILES.get('img')
		new_img = Image(pic=img)
		new_img.save()
	return render(request,'index.html')

		#return HttpResponse("allowed only via POST")

def listImg(request):
    imgs = Image.objects.all()
    content = {
        'imgs':imgs,
    }
    return render(request, 'listImg.html', content)

def chosedImg(request):
	urls = request.GET['url']
	return render(request,'index.html',{'urls':urls})
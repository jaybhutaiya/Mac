from django.shortcuts import render
from django.http import HttpResponse
from.import forms
from django.views import View
from .models import course
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
def index(request):
    context={
        'title':'bio',
        'name':'Jay Bhutaiya',
        'Ph_no':'9879974232',
        'digit':[67,76,78,77],
    }
    return render(request,'index.html',context)

class home(View):
    def get(self,request,*args,**kwargs):
        data=course.objects.all()
        context={
            'data':data
        }
        return render(request,'mac.html',context)
# class courses(View):
#     def get(self,request,*args,**kwargs):
#         data=course.objects.all()
        # return render(request,'course.html',{'data':data})
def detail(request,id):
    data=course.objects.get(id=id)
    return render(request,'detail.html',{'data':data})
class courses(ListView):
    model=course
    template_name='course_list.html'
    context_object_name='data'
class college(View):
    def get(self,request,*args,**kwargs):
        return render(request,'college.html')
class activity(View):
    def get(self,request,*args,**kwargs):
        return render(request,'activity.html')
class about(View):
    def get(self,request,*args,**kwargs):
        return render(request,'about.html')
class blog(View):
    def get(self,request,*args,**kwargs):
        return render(request,'blog.html')
class contact(View):
    def get(self,request,*args,**kwargs):
        form=forms.leaveform()
        return render(request,'contact.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=forms.leaveform(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'contact.html',{'form':form})  
class blockchain(View):
    def get(self,request,*args,**kwargs):
        data=course.objects.all()
        context={
            'data':data
        }
        return render(request,'blockchain.html',context)

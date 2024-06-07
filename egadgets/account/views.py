from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from .form import RegisterForm,LogForm
from django.views.generic import CreateView,TemplateView,FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

# class LandingView(View):
#     def get(self,request):
#         return render(request,"index.html")
class LandingView(TemplateView):
    template_name="index.html"

# class loginView(View):
#     def get(self,request):
#         return render(request,"log.html")
#


class LoginView(FormView):
    template_name='log.html'
    form_class=LogForm
    def post(self,request):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                print(user)
                login(request,user)
                messages.success(request,"login successfully!...")
                return redirect('home')
            else:
                print(user,"loging failed")
                messages.error(request,"Invalid username/Password")
                return redirect('log')
        return render(request,"log.html",{"form":form_data})

      





    
# class regView(View):
#     form_class=RegisterForm()
#     template_name="reg.html"
#     success_url="log"
#     def get(self,request):
       
#         form=self.form_class
#         return render(request,self.template_name,{"form":form})
#     def post(self,request):
#         form_data=self.form_class(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             return redirect(self.success_url)
#         return render(request,self.template_name,{"form":form_data})



class regView(CreateView):
    form_class=RegisterForm
    template_name="reg.html"
    success_url=reverse_lazy('log')
    def form_valid(self, form: BaseModelForm):
        messages.success(self.request,"registration completed")
        return super().form_valid(form)
    def form_invalid(self, form: BaseModelForm):
        messages.error(self.request,"registration failed")
        return super().form_invalid(form)
    

class LogOut(View):
    def get(self,request):
        logout(request)
        return redirect('landing')    

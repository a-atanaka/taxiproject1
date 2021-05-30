from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models  import TaxiModel
from django.views.generic import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy 
from  . import forms
from django.contrib.auth import get_user_model
#from django.views.generic import DetailView,CreateView,DeleteView,UpdateView
#from .models import TodoModel




# Create your views here.

def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username,'',password)
        except IntegrityError:
            return render(request,'signup.html',{'error':'このユーザーはすでに登録されています'})
    return render(request,'signup.html')

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password) 
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request,'login.html',{'not':'ログインできませんでした'})
    return render(request,'login.html',{}) 

@login_required
def listfunc(request):
    object_list = TaxiModel.objects.all()
    return render(request, 'list.html',{'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request,pk):
    object = get_object_or_404(TaxiModel,pk=pk)
    return render(request,'detail.html',{'object':object})

class TaxiCreate(CreateView):
    template_name = 'create.html'
    model = TaxiModel 
    fields = ('priority','myinteger','regist_date','author')
    success_url = reverse_lazy('list')


class TaxiDelete(DeleteView):
    template_name = 'delete.html'
    model = TaxiModel
    success_url = reverse_lazy('list') 

class TaxiUpdate(UpdateView):
    template_name = 'update.html'
    model = TaxiModel
    fields = ('priority','myinteger','regist_date','author')
    success_url = reverse_lazy('list') 

def form_view(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('create')
    else:
       form = forms.PostForm()
    return render(request, 'create/create.html', {'form': form})
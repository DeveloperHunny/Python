from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from accountapp.models import HelloWorld
from django.urls import reverse , reverse_lazy
from django.views import generic
from django.contrib.auth import models, forms, decorators
from django.utils.decorators import method_decorator
from .forms import AccountUpdateForm
from .decorators import account_ownership_required

# Create your views here.

has_ownership = [decorators.login_required , account_ownership_required]

@decorators.login_required
def hello_world(request): #인자로 request가 들어가는 이유는 client에게 요청을 받아 처리하기 때문!
    
    if request.method == "POST":

        temp = request.POST.get('hello_world_input');
        
        new_hello_world = HelloWorld();
        new_hello_world.text = temp;
        new_hello_world.save();

        hello_world_list = HelloWorld.objects.all();
        
        #F5 새로고침 후 계속 POST 방식의 홈페이지가 생성되지 않도록 redirect로 GET 방식의 홈페이지로 돌아감.
        return HttpResponseRedirect(reverse('accountapp:hello_world')); 
    
    else :
        hello_world_list = HelloWorld.objects.all();
        return render(request, 'accountapp/hello_world.html' , context ={ 'hello_world_list' : hello_world_list });

class AccountCreateView(generic.CreateView):
    model = models.User
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'
    
class AccountDetailView(generic.DetailView):
    model = models.User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(generic.UpdateView):
    model = models.User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(generic.DeleteView):
    model = models.User
    context_object_name = 'target_user'
    template_name = 'accountapp/delete.html'
    success_url = reverse_lazy('accountapp:login') 

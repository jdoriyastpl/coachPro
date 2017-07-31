from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,View
from django.core.urlresolvers import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from adminPro.forms import UserForm
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.


class UserFormView(View):
    form_class = UserForm
    template_name = 'adminPro/signup.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('login'))
        return render(request,self.template_name,{'form':form})

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

    
# 처음페이지 함수
class SansuTemplateView(TemplateView):
    template_name = 'main_layout.html'

# 회원가입 함수
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

# 회원가입 완료 함수
class UserCreateDoneTemplateView(TemplateView):
    template_name = 'registration/register_done.html'

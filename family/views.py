from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

from datetime import datetime, date
    
# 처음페이지 함수
class SansuTemplateView(TemplateView):
    template_name = 'main_layout.html'

    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
       # 병원 진료 예약일
       # 안과
        op_1 = datetime(2018,5,11)
        op_2 = datetime.now()        
        context['op_3'] = op_1 - op_2   

        
        # 요양병원 입원일수
        convalescentHospital_1 = datetime(2017,8,29)
        convalescentHospital_2 = datetime.now()
        context['convalescentHospital_3'] = convalescentHospital_2 - convalescentHospital_1


        return context

    

# 회원가입 함수
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

# 회원가입 완료 함수
class UserCreateDoneTemplateView(TemplateView):
    template_name = 'registration/register_done.html'

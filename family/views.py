from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

from datetime import datetime, date, timedelta
import re
    
# 처음페이지 함수
class SansuTemplateView(TemplateView):
    template_name = 'main_layout.html'

    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # 전대병원 입원기간
        cnuh_1 = date(2017,6,26)
        cnuh_2 = date(2017,8,28)
        cnuh_3 = cnuh_2 - cnuh_1
        # 입원기간
        context['cnuh_3'] = cnuh_2 - cnuh_1
        
       # 요양병원 입원일수 아래것이 단순함.
        #convalescentHospital_1 = datetime(2017,8,29)
        #convalescentHospital_2 = datetime.now()
        #context['convalescentHospital_3'] = convalescentHospital_2 - convalescentHospital_1

        convalescentHospital_1 = date(2017,8,29)
        convalescentHospital_2 = date.today()
        convalescentHospital_3 = convalescentHospital_2 - convalescentHospital_1
        context['convalescentHospital_3'] = convalescentHospital_2 - convalescentHospital_1

        # 총 입원일
        context['hospitalization'] = (cnuh_3 + convalescentHospital_3) + timedelta(days=1)
       
       # 병원 진료 예약일
       # 안과
        op_1 = date(2018,5,11)
        op_2 = date.today()   

        
        
        op_3 = op_1 - op_2
        op_4 = op_2 - op_1
       
        context['op_3'] = op_3  # 남았습니다.
        context['op_4'] = op_4   # 지났습니다.

        # test
        t1 = datetime(2018,2,27)
        t2 = datetime.now()
        context['t3'] = t1 -t2 #남았습니다.
        context['t4'] = t2 - t1 # 지났습니다.       
        
       
        return context

    

# 회원가입 함수
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

# 회원가입 완료 함수
class UserCreateDoneTemplateView(TemplateView):
    template_name = 'registration/register_done.html'

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
        context['cnuh_1'] = cnuh_1
        
       # 요양병원 입원일수 아래것이 단순함.
        #convalescentHospital_1 = datetime(2017,8,29)
        #convalescentHospital_2 = datetime.now()
        #context['convalescentHospital_3'] = convalescentHospital_2 - convalescentHospital_1

        convalescentHospital_1 = date(2017,8,29)
        convalescentHospital_2 = date.today()
        convalescentHospital_3 = convalescentHospital_2 - convalescentHospital_1
        # 입원기간
        context['convalescentHospital_3'] = convalescentHospital_2 - convalescentHospital_1
        # 몇개월 전
        context['convalescentHospital_1'] = convalescentHospital_1

        # 총 입원일
        context['hospitalization'] = (cnuh_3 + convalescentHospital_3).days + 1     # timedelt(days=1) 를 사용할때 .days + 1 를 대신해서 사용
       
       # 병원 진료 예약일

       # 신경외과
        neurosurgery_1 = date(2018,4,26)
        neurosurgery_2 = date.today()
        neurosurgery_3 = neurosurgery_1 - neurosurgery_2 # 남았다
        neurosurgery_4 = neurosurgery_2 - neurosurgery_1 # 지났다
        context['neurosurgery_1'] = neurosurgery_1
        context['neurosurgery_2'] = neurosurgery_2
        context['neurosurgery_3'] = neurosurgery_3
        context['neurosurgery_4'] = neurosurgery_4

        # 안과(2019, 5, 10)
        op_111 = date(2019, 5, 10)
        op_222 = date.today()

        op_333 = op_111 - op_222
        op_444 = op_222 - op_111

        context['op_111'] = op_111
        context['op_222'] = op_222
        context['op_333'] = op_333  # 남았습니다.
        context['op_444'] = op_444  # 지났습니다.



       # 안과
        op_1 = date(2018,5,11)
        op_2 = date.today()           
        
        op_3 = op_1 - op_2
        op_4 = op_2 - op_1

        context['op_1'] = op_1
        context['op_2'] = op_2
        context['op_3'] = op_3  # 남았습니다.
        context['op_4'] = op_4   # 지났습니다.

        # 안과 2018-11-09
        op_11 = date(2018,11,9)
        op_22 = date.today()           
        
        op_33 = op_11 - op_22
        op_44 = op_22 - op_11

        context['op_11'] = op_11
        context['op_22'] = op_22
        context['op_33'] = op_33  # 남았습니다.
        context['op_44'] = op_44   # 지났습니다.

        # test
        t1 = datetime(2018,2,27)
        t2 = datetime.now()
        context['t3'] = t1 -t2 #남았습니다.
        context['t4'] = t2 - t1 # 지났습니다.    

        a=date(2015,3,11)  
        
        context['a'] = a

        # 기념일 
        anni = date(2018,1,10)
        ann = date(2018,1,10)
        context['anni'] = anni
        context['ann'] = ann
        return context

    

# 회원가입 함수
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

# 회원가입 완료 함수
class UserCreateDoneTemplateView(TemplateView):
    template_name = 'registration/register_done.html'

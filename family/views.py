from dateutil import parser

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
#from django.core.urlresolvers import reverse_lazy 아래로 대체
from django.urls import reverse

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http.response import StreamingHttpResponse
import os, sys, pandas, cgi
from openpyxl import load_workbook


from IPython.display import HTML
from PIL import Image
import numpy as np


from datetime import datetime, date, timedelta, time
from time import time, localtime, gmtime
import pickle
from . import views



# 처음페이지 함수
class SansuTemplateView(TemplateView):
    template_name = 'main_layout.html'

    # 예약 날자 계산하는 함수
    def ophthalmology(self, annivarsary):
        today = date.today()
        self.annivarsary = annivarsary

        if self.annivarsary > today:
            self.kkk = self.annivarsary - today
            self.kkk = "{day.days}일 남았습니다".format(day  = self.kkk)
        elif self.annivarsary == today:
            self.kkk = '{}일 오늘은 안과 진료일입니다'.format(today)
        else:
            self.kkk = today - self.annivarsary
            self.kkk = '{.days}일 지났습니다'.format(self.kkk)
        return self.kkk

    # 가족 웨딩 기념일
    def wedding(self, annivarsary, name = None):
        today = date.today()
        self.name = name
        self.annivarsary = annivarsary

        if self.annivarsary > today:
            self.kkk = self.annivarsary - today
            self.kkk = "{name} 결혼식({annivarsary})이  {day.days}일 남았습니다.".format(name=self.name, annivarsary=self.annivarsary, day=self.kkk)
        elif self.annivarsary == today:
            self.kkk = '{today}일 오늘은 {name} 결혼일입니다.'.format(today = today, name = self.name)
        return self.kkk

    # 기념일 계산 제너레이터
    def birthday(self):
        with open('2020_aniversary_note.bin', 'wb') as ff:
            uuu = datetime.fromtimestamp(time(), tz=None)

                                                            # datetime.date 으로 형변환 하기 위해서, 년도 자동화
                                                            ########### datetime.strptime('2022-07-27', '%Y-%m-%d).date()  ---> 마지막 date( ) 함수를
                                                            ########   사용하지 않으면 00:00:00 시 분 초 까지 나온다 !+++++++++++++++++++++++++++

            names = {
                # date(shift.year,2,2) 이 형태는 datetime date 형이다.
                date(uuu.year,3,5): "오늘으이 생일이다",
                date(uuu.year, 8,22): "첫번재 입니다",
                date(uuu.year, 8,22): "두번째 입니다",
            }
            pickle.dump(names, ff)

 # 데이터 형에 신경 써야 한다. datetime.date 형을 일치시켜야 한다. 꼭 print(type(a)) 형 확인을 하자
        with open('2020_aniversary_note.bin', 'rb') as f:
            a = pickle.load(f)

            for i in a:
                if i == date.today():
                    print(type(i))
                    if i == date.today():
                        return print(a[i])
                    return print(a[i])






            #for i in a.keys():

                #if i == date.today():
                    #yield a[i]

    #for iii in birthday(self):

        #print(type(iii))



            #c = datetime.strptime(b, "%Y-%m-%d").date()






    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # 생일
        context['birthday'] = self.birthday()

        # 안과 예약 날자 함수 호출
        context['ophthalmology_1'] = self.ophthalmology(annivarsary=date(2020, 6, 26))
        context['ophthalmology_0'] = self.ophthalmology(annivarsary=date(2020, 1, 10))

        # 산하, 수아 결혼식 날자 계산
        #context['sua'] = self.wedding(annivarsary=date(2019, 11, 9), name='이수아')


        # 기념일
        anni = date(2018, 1, 10)
        ann = date(2018, 1, 10)
        context['anni'] = anni
        context['ann'] = ann

        # 전대병원 입원기간
        cnuh_1 = date(2017,6,26)
        cnuh_2 = date(2017,8,28)
        cnuh_3 = cnuh_2 - cnuh_1

        # 입원기간
        context['cnuh_3'] = cnuh_2 - cnuh_1
        context['cnuh_1'] = cnuh_1


        
       # 광주시립제2요양병원 입원일수 아래것이 단순함.
        convalescentHospital_1 = date(2017,8,29)
        #convalescentHospital_2 = date.today() 화순군립요양원으로 옮기심.
        convalescentHospital_2 = date(2020,2,25)
        convalescentHospital_3 = convalescentHospital_2 - convalescentHospital_1
        # 입원기간
        context['convalescentHospital_3'] = convalescentHospital_2 - convalescentHospital_1
        # 몇개월 전
        context['convalescentHospital_1'] = convalescentHospital_1

        # 화순군립요양병원 입원일수
        hoasun_nursing_home_1 = date(2020,2,24)  ######## 25일이 아니라 24일 날자에 -1을 해줘야 정확한 날자 가 나온다
                                                 ######## 단 오늘은 진료일입니다는 해당사항이 없다. 그날 날자로 25일로
        hoasun_nursing_home_2 = date(2020,5,26)
        hoasun_nursing_home_sum = hoasun_nursing_home_2 - hoasun_nursing_home_1
        context['hoasun_nursing_home_sum'] = hoasun_nursing_home_sum

        # 코로나19로 인해 화순군립요양병원에서 광주제2시립요양병원으로 옮기심.
        gw2_nursing_home_1 = date(2020, 5, 25)  ######## 26일이 아니라 25일 날자에 -1을 해줘야 정확한 날자 가 나온다
                                                    ######## 단 오늘은 진료일입니다는 해당사항이 없다. 그날 날자로 26일로
        gw2_nursing_home_2 = date.today()
        gw2_nursing_home_sum = gw2_nursing_home_2 - gw2_nursing_home_1
        context['gw2_nursing_home_sum'] = gw2_nursing_home_sum

        # 총 입원일
        context['hospitalization'] = (date.today() - date(2017,6,26)).days + 1     # timedelt(days=1) 를 사용할때 .days + 1 를 대신해서 사용
                                                                                       # days+1 일은 에스웰 요양병원 1일치 더한기 한것
        # 총 입원일 년으로 계산하기 timesince
        context['hospitalization_timesince'] = date(2017,6,26) # timesince 사용할때는 반드시 date(2017,2,22) 이런 형식으로 상용. 다르게 사용하면 에러난다.
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



        # 안과(2019, 06, 21)
        op_1111 = date(2019, 6, 21)
        op_2222 = date.today()

        op_3333 = op_1111 - op_2222
        op_4444 = op_2222 - op_1111

        context['op_1111'] = op_1111
        context['op_2222'] = op_2222
        context['op_3333'] = op_3333 # 남았습니다.
        context['op_4444'] = op_4444  # 지났습니다.

        # 안과(2019, 5, 10)
        op_111 = date(2019, 5, 10)
        op_222 = date.today()

        op_333 = op_111 - op_222
        op_444 = op_222 - op_111

        context['op_111'] = op_111
        context['op_222'] = op_222
        context['op_333'] = op_333  # 남았습니다.
        context['op_444'] = op_444  # 지났습니다.


        return context



# 회원가입 함수
# class UserCreateView(CreateView):
#     template_name = 'registration/register.html'
#     form_class = UserCreationForm
#     success_url = reverse('register_done')

# 회원가입 완료 함수
# class UserCreateDoneTemplateView(TemplateView):
#     template_name = 'registration/register_done.html'



# 테스트 지을것 카카오 로그인
class kakaologin(TemplateView):
    def get(self, request):
        code = request.GET.get('code')
        return HttpResponse({code})


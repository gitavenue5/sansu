

from django.shortcuts import render, get_object_or_404, resolve_url, reverse, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

# 로그인 페이지로 가기
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from datetime import date, datetime, timedelta


from django.db.models import Q, F, Sum, Count, Case, When

#from django.contrib.auth.models import User
from rest_framework import viewsets

from . serializers import AnniversarySerializer, GwBankSerializer, WrBankSerializer

from . models import Daily, Anniversary, GwBank, WrBank, Note, NoteComment 
from . forms import DailyForm, AnniversaryForm, GwBankForm, WrBankForm, NoteForm, NoteCommentForm, NoteCommentUpdateForm 

# Create your views here.


# 로그인 리다이렉트
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

# 날마다
class DailyCreateView(LoginRequiredMixin, CreateView):
    model = Daily 
    form_class = DailyForm
    template_name = 'family_site/daily/daily_create.html'
    success_url = reverse_lazy('family_site:daily_list')

    def get_queryset(self):
        return Daily.objects.all()

class DailyListView(ListView):
    model = Daily
    template_name = 'family_site/daily/daily_list.html'

class DailyDetailView(DetailView):
    model = Daily
    template_name = 'family_site/daily/daily_detail.html'    

# 기념일
class AnniversaryViewSet(viewsets.ModelViewSet):
    queryset = Anniversary.objects.all()
    serializer_class = AnniversarySerializer

class AnniversaryCreateView(LoginRequiredMixin, CreateView):
    model = Anniversary
    form_class = AnniversaryForm
    template_name = 'family_site/anniversary/anniversary_create.html'
    success_url = reverse_lazy('family_site:anniversary_list')

class AnniversaryListView(ListView):
    model = Anniversary
    template_name = 'family_site/anniversary/anniversary_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        anni = date(2018,3,31)
       
        #anniver = anni.strftime('%Y-%m-%d') 이렇게 문자열화 하면 에러난다
        context['a'] = anni
        b = date.today()
        
        context['c'] = repr(b)        
        f = datetime.strptime('2018-04-17', '%Y-%m-%d')
        context['ff'] = str(f)[:-1]

       
        return context

# 광주은행
class GwBankViewSet(viewsets.ModelViewSet):
    queryset = GwBank.objects.all()
    serializer_class = GwBankSerializer

class GwBankCreateView(LoginRequiredMixin, CreateView):
    model = GwBank
    template_name = 'family_site/gwbank/gwbank_create.html'    
    form_class = GwBankForm
    #fields = ('id', 'gwbank_name_choices', 'gwbank_date', 'gwbank_income', 'gwbank_money', 'gwbank_name', 'gwbank_execution', 'gwbank_note',)
    #success_url = reverse_lazy('family_site:gwbank_list')
    # CreateView는 fields 를 적어주지 않으면 에러나고, form.html 에서 필드가 표시되지 않는다

    def form_valid(self, form):
        form = form.save(commit=False)
        form.gwbank_execution = self.default=0
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('family_site:gwbank_list')


class GwBankListView(ListView):
    model = GwBank
    template_name = 'family_site/gwbank/gwbank_list.html'
    paginate_by = 30

    def get_queryset(self):
        return GwBank.objects.all()

    def get_context_data(self, **kwarges):
        context = super(GwBankListView, self).get_context_data(**kwarges)
        context['chaesun'] = GwBank.objects.filter(gwbank_name='이채순').aggregate(이채순=Sum(F('gwbank_money')))['이채순'] or 0
        context['gichang'] = GwBank.objects.filter(gwbank_name='이기창').aggregate(이기창=Sum(F('gwbank_money')))['이기창'] or 0
        context['hwasun'] = GwBank.objects.filter(gwbank_name='이화순').aggregate(이화순=Sum(F('gwbank_money')))['이화순'] or 0
        #context['k'] = GwBank.objects.filter(gwbank_name='이채순')
        context['k'] = GwBank.objects.all()

        context['total'] = context['chaesun'] + context['gichang'] + context['hwasun']

        return context


# 우리은행

class WrBankViewSet(viewsets.ModelViewSet):
    queryset = WrBank.objects.all()
    serializer_class = WrBankSerializer

class WrBankCreateView(LoginRequiredMixin, CreateView):
    model = WrBank
    template_name = 'family_site/wrbank/wrbank_create.html'
    #success_url = reverse_lazy('family_site:wrbank_list')
    form_class = WrBankForm

    def form_valid(self, form):
        form = form.save(commit=False)
        form.wrbank_money1 = self.default=0
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('family_site:wrbank_list')

    

class WrBankListView(ListView):
    model = WrBank
    template_name = 'family_site/wrbank/wrbank_list.html'
    paginate_by = 30

    def get_queryset(self):        
        return WrBank.objects.all()

    def get_context_data(self, **kwarges):
        context = super(WrBankListView, self).get_context_data(**kwarges)
        context['interest'] = WrBank.objects.all().aggregate(대출이자총액=Sum(F('wrbank_money2')))['대출이자총액'] or 0
        context['principal'] = WrBank.objects.all().aggregate(원금총액=Sum(F('wrbank_money3')))['원금총액'] or 0
        context['deposit_withdrawal'] = WrBank.objects.all().aggregate(대출이자원금총액=Sum(F('wrbank_money2')+F('wrbank_money3')))['대출이자원금총액'] or 0

        context['kk'] = WrBank.objects.filter(wrbank_money2__gt=0).count
        context['kkk'] = WrBank.objects.filter(wrbank_money3__gt=0).count

        context['lee_sang_soon'] = WrBank.objects.filter(wrbank_note__startswith='이상순(가족)').aggregate(금액=Sum(F('wrbank_money1')))['금액'] or 0

        context['lee_sang_soon_count'] = WrBank.objects.filter(wrbank_note__startswith='이상순(가족)').count

        
        return context


# 게시판
class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'family_site/note/note_create.html'
    form_class = NoteForm    

    def form_valid(self, form):
        form = form.save(commit=False)
        form.note_author = self.request.user
        form.save()
        return super(NoteCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('family_site:note_list')
        

class NoteListView(ListView):
    model = Note
    template_name = 'family_site/note/note_list.html'
    paginate_by = 4

    def get_queryset(self, *args, **kwargs):
        return Note.objects.select_related('note_author').all()       

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        return context


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'family_site/note/note_detail.html'

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm     
    template_name = 'family_site/note/note_create.html'
    success_url = reverse_lazy('family_site:note_list')

   
class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note 
    success_url = reverse_lazy('family_site:note_list') 
    template_name = 'family_site/note/note_confirm_delete.html'
   


# 게시판 댓글
class NoteCommentCreateView(LoginRequiredMixin, CreateView):
    model = NoteComment
    template_name = 'family_site/notecomment/notecomment_create.html'
    form_class = NoteCommentForm  

    def form_valid(self, form):
        kkk = form.save(commit=False)
        kkk.note = get_object_or_404(Note, pk=self.kwargs['pk'])        
        kkk.notecomment_author= self.request.user  
        kkk.save()      
        return super().form_valid(form)
      
    def get_success_url(self):        
        return resolve_url(self.object.note)        

 
class NoteCommentUpdateView(LoginRequiredMixin, UpdateView):
    model = NoteComment
    template_name = 'family_site/notecomment/notecomment_create.html'
    form_class = NoteCommentForm

    def get_success_url(self):    
        return resolve_url(self.object.note)
 
class NoteCommentDeleteView(LoginRequiredMixin, DeleteView):
    model = NoteComment
    template_name = 'family_site/notecomment/notecomment_confirm_delete.html'
    form_class = NoteCommentForm
    
    def get_success_url(self):
        return resolve_url(self.object.note)

    
   








import datetime
#from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import Select, MultiWidget, DateInput, TextInput, Widget

from django import forms
#from django.forms import extras   extras 대신 forms 를 사용

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from . models import Daily, Anniversary, GwBank, WrBank, Note, NoteComment
#BIRTH_YEAR_CHOICES = ('2012', '2013', '2014', '2015','2016','2017','2018','2019','2020')
THIS_YEAR = datetime.date.today().year
# 날마다 폼
class DailyForm(forms.ModelForm):
    #daily_date = forms.DateField(widget=extras.SelectDateWidget(),label='날자',help_text="  ")
    daily_date = forms.DateField(widget=forms.SelectDateWidget(), label='날자', help_text="  ")
    class Meta:
        model = Daily
        fields = ('daily_date', 'daily_day', 'daily_content', )
        widgets = {
            'daily_content' : SummernoteWidget(),
        }

# 자동 완성 끄기
#  'autocomplete'='off' 를 attrs에 추가하면됩니다.    

# 기념일 폼
class AnniversaryForm(forms.ModelForm):
    #anniversary_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=10)),label=('연락처'))
    #anniversary_date = forms.DateField(widget=SelectDateWidget,initial=datetime.date.today,label=_("날짜"))
    anniversary_date = forms.DateField(widget=forms.SelectDateWidget(),label='날자',help_text="  ")
   
    class Meta:
        model = Anniversary
        fields = ('anniversary_date', 'anniversary_day', 'anniversary_name', 'anniversary_lunar_date', )
        


# 광주은행 폼
class GwBankForm(forms.ModelForm):
    #gwbank_date = forms.DateField(required=False, widget=extras.SelectDateWidget(years=BIRTH_YEAR_CHOICES),label='날자',help_text="  ")
    gwbank_date = forms.DateField(initial=datetime.date.today(), widget=forms.SelectDateWidget(None, range(2014, THIS_YEAR+10)))
    class Meta:
        model = GwBank
        fields = ('gwbank_name_choices', 'gwbank_date', 'gwbank_income', 'gwbank_money', 'gwbank_name', 'gwbank_execution', 'gwbank_note', )


# 우리은행
class WrBankForm(forms.ModelForm):
    #wrbank_date = forms.DateField(widget=extras.SelectDateWidget(),label='날자',help_text="  ")
    wrbank_date = forms.DateField(initial=datetime.date.today(), widget=forms.SelectDateWidget(None, range(2014, THIS_YEAR+10)))
    class Meta:
        model = WrBank
        fields = ('wrbank_date', 'wrbank_deposit_withdrawal', 'wrbank_money1', 'wrbank_note', 'wrbank_money2',  'wrbank_money3', 'wrbank_aggregate', 'wrbank_loan_balance', 'wrbank_bankbook_balance', )


# 게시판
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('note_title', 'note_content', )
        widgets = {
            'note_content': SummernoteWidget(),
        }


# 게시판 댓글
class NoteCommentForm(forms.ModelForm):
    class Meta:
        model = NoteComment
        fields = ('notecomment_content', )

# 게시판 수정
class NoteCommentUpdateForm(forms.ModelForm):
    class Meta:
        model = NoteComment
        fields = ('notecomment_content', )
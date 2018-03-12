from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

# 날마다
class Daily(models.Model):
    daily_date = models.DateField('날자', help_text='날자입력')
    daily_day = models.CharField('요일', max_length=4, help_text='토요일 입력')
    daily_content = models.TextField('글내용', help_text='summernote 글 내용')
    daily_created_date = models.DateTimeField('생성일', default=timezone.now, help_text='생성날자')
    daily_published_date = models.DateTimeField('수정일', auto_now=True, help_text='수정날자')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.daily_content

    def get_absolute_url(self):
        return reverse('family_site:daily_detail', args=[str(self.pk)])

# 기념일
class Anniversary(models.Model):
    anniversary_date = models.CharField('생일날자', max_length=20, help_text='생일날자')
    anniversary_day = models.CharField('요일', max_length=10,default='',  help_text='요일')
    anniversary_name = models.CharField('이름', max_length=20, default='', help_text='생일 당사자 이름')
    anniversary_lunar_date = models.CharField('생일 음력 날자', max_length=20, blank=True, help_text='생일 음력 날자')
    daily_created_date = models.DateTimeField('생성일', default=timezone.now, help_text='생성날자')
    daily_published_date = models.DateTimeField('수정일', auto_now=True, help_text='수정날자')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.anniversary_name

# 광주은행
class GwBank(models.Model):

    GWBANK_NAME_CHOICES = (
        ('이채순', '이채순'),
        ('이기창', '이기창'),
        ('이화순', '이화순'),
    )

    gwbank_name_choices = models.CharField('이름으로 구분', blank=True, max_length=4, choices=GWBANK_NAME_CHOICES, help_text='이름으로 특정 데이터 가져오기')
    gwbank_date = models.DateField('날자', help_text='입출금 날자')
    gwbank_income = models.CharField('입금출금', max_length=5, help_text='입금 출륵 중 선택')
    gwbank_money = models.PositiveIntegerField('금액', help_text='입출금 금액')
    gwbank_name = models.CharField('이름 및 설명글', blank=True, max_length=20, help_text='이름 및 설명글 작성')
    gwbank_execution = models.PositiveIntegerField('특정 값 합계 금액 정수', null=True, blank=True, help_text='특정 값 합계 금액 적는 필드')
    gwbank_note = models.CharField('메모', max_length=200, blank=True, default=0, help_text='메모 필드')
    daily_created_date = models.DateTimeField('생성일', default=timezone.now, help_text='생성날자')
    daily_published_date = models.DateTimeField('수정일', auto_now=True, help_text='수정날자')

    # CharField 에서 null=True 하면 템플릿에서 NONE  이라는 문자열을 출력한다.
    # CharField 필드는 null=True, blank=True 중 하나만 해야한다.
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.gwbank_income

    
# 우리은행
class WrBank(models.Model):
    wrbank_date = models.DateField('날자', help_text='날자를 표기')
    wrbank_deposit_withdrawal = models.CharField('입출금', max_length=10, help_text='입금 출금 표기')
    wrbank_money1 = models.PositiveIntegerField('금액', blank=True, default=0, help_text='금액, 이자를 표기')
    wrbank_note = models.CharField('비고 및 설명글', max_length=200, default='', help_text='비고 및 설명글 표기')
    wrbank_money2 = models.PositiveIntegerField('대출이자', blank=True, default=0,  help_text='대출 이자를 표기')    
    wrbank_money3 = models.PositiveIntegerField('원금', blank=True, default=0, help_text='원금을 표기')
    wrbank_aggregate = models.PositiveIntegerField('합계', blank=True, default=0, help_text='이자와 원금 합계')
    wrbank_loan_balance = models.PositiveIntegerField('대출잔액', blank=True, default=75000000, help_text='대출잔액')
    wrbank_bankbook_balance = models.PositiveIntegerField('통장잔액', default=0, help_text='통장 잔액')
    daily_created_date = models.DateTimeField('생성일', default=timezone.now, help_text='생성날자')
    daily_published_date = models.DateTimeField('수정일', auto_now=True, help_text='수정날자')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.wrbank_note


# 게시판 
class Note(models.Model):
    note_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='note')
    note_title = models.CharField('제목', max_length=200,  help_text='  ')
    note_content = models.TextField('내용 (사진 사이즈가 크면 등록되지 않습니다!)')
    note_created_date = models.DateTimeField('생성일', default=timezone.now, help_text='생성 날자')
    note_published_date = models.DateTimeField('수정일', blank=True, auto_now=True, null=True, help_text='글 수정 일시')

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.note_content    

    def get_absolute_url(self):
        #return reverse('family_site:note_detail', args=[str(self.pk)])
        return reverse('family_site:note_detail', args=(self.pk,))
    # note_created_date 기준으로 이전 포스트 반환
    def get_previous_note_created_date(self):
        return self.get_previous_by_note_created_date()

    # note_create_date 기준으로 다음 포스트 반환
    def get_next_note_created_date(self):
        return self.get_next_by_note_created_date()


# 게시판 댓글
class NoteComment(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments')
    notecomment_author = models.ForeignKey(settings.AUTH_USER_MODEL)
    notecomment_content = models.TextField('글내용')
    notecomment_created_date = models.DateTimeField('생성날자', auto_now_add=True, help_text='생성날자')
    notecomment_publish_date = models.DateTimeField('수정날자', auto_now=True, help_text='수정날자')

    class Meta:
        ordering = ('-notecomment_created_date', )

    def __str__(self):
        return self.notecomment_content

    def get_queryset(self):
        return super().get_queryset().select_related('notecomment_author').all()


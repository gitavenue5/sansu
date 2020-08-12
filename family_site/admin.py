from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from . models import Daily, Anniversary, GwBank, WrBank, Note, NoteComment

# Register your models here.

# 날마다
class DailyAdmin(SummernoteModelAdmin):
    summer_note_fields = ('content', )
    list_display = ('id', 'daily_date', 'daily_content')
    list_display_links = ('id', 'daily_date', 'daily_content')
admin.site.register(Daily, DailyAdmin)

# 기념일
@admin.register(Anniversary)
class AnniversaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'anniversary_date', 'anniversary_name', 'anniversary_lunar_date',  )
    list_display_links = ('id', 'anniversary_date', 'anniversary_name', )

# 광주은행
@admin.register(GwBank)
class GwBankAdmin(admin.ModelAdmin):
    list_display = ('id', 'gwbank_date', 'gwbank_income', 'gwbank_money', 'gwbank_name', 'gwbank_execution', 'gwbank_note', )
    list_display_links = ('id', 'gwbank_date', 'gwbank_name', )


# 우리은행
@admin.register(WrBank)
class WrBankAdmin(admin.ModelAdmin):
    list_display = ('id', 'wrbank_date', 'wrbank_deposit_withdrawal', 'wrbank_money1', 'wrbank_note', 'wrbank_money2',  'wrbank_money3', 'wrbank_aggregate', 'wrbank_loan_balance', 'wrbank_bankbook_balance', )
    list_display_links = ('wrbank_date', 'wrbank_deposit_withdrawal', 'wrbank_money1', 'wrbank_note', 'wrbank_money2',  'wrbank_money3', )


    # 게시판
class NoteAdmin(SummernoteModelAdmin):
    summer_note_fields = ('note_content', )
admin.site.register(Note, NoteAdmin)

#게시판 댓글
@admin.register(NoteComment)
class NoteCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'notecomment_author', 'notecomment_content', )

from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from . models import Daily, Anniversary, GwBank, Note, NoteComment

# Register your models here.

# 날마다
class DailyAdmin(SummernoteModelAdmin):
    summer_note_fields = ('content', )
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


    # 게시판
class NoteAdmin(SummernoteModelAdmin):
    summer_note_fields = ('note_content', )
admin.site.register(Note, NoteAdmin)

# 게시판 댓글
@admin.register(NoteComment)
class NoteCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'notecomment_author', 'notecomment_content', )
    
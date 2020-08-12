
from django.urls import path, include


from . import views

app_name = 'family_site'
urlpatterns = [

    # daily urls
    path('daily_create/', views.DailyCreateView.as_view(), name='daily_create'),
    path('daily_list/', views.DailyListView.as_view(), name='daily_list'),
    path('daily_detail/<int:daily_id>/', views.DailyDetailView.as_view(), name='daily_detail'),

    # anniversary urls
    path('anniversary_create/', views.AnniversaryCreateView.as_view(), name='anniversary_create'),
    path('anniversary_list/', views.AnniversaryListView.as_view(), name='anniversary_list'),

    # 광주은행
    path('gwbank_create/', views.GwBankCreateView.as_view(), name='gwbank_create'),
    path('gwbank_list/', views.GwBankListView.as_view(), name='gwbank_list'),

    # 우리은행
    path('wrbank_create/', views.WrBankCreateView.as_view(), name='wrbank_create'),
    path('wrbank_list/', views.WrBankListView.as_view(), name='wrbank_list'),
    
    # 게시판
    path('note_create/', views.NoteCreateView.as_view(), name='note_create'),
    path('note_list/', views.NoteListView.as_view(), name='note_list'),
    path('note_detail/<int:note_id>/', views.NoteDetailView.as_view(), name='note_detail'),
    path('note_update/<int:note_id>/', views.NoteUpdateView.as_view(), name='note_update'),
    path('note_delete/<int:note_id>/', views.NoteDeleteView.as_view(), name='note_delete'),

    # # 게시판 댓글
    path('notecomment_create/<int:pk>/', views.NoteCommentCreateView.as_view(), name='notecomment_create'),
    path('notecomment_update/<int:note_pk>)/<int:pk>/', views.NoteCommentUpdateView.as_view(), name='notecomment_update'),
    path('notecomment_delete/<int:note_pk>)/<int:pk>/', views.NoteCommentDeleteView.as_view(), name='notecomment_delete'),
    #
    #
    # 카카오 로그인
    path('kakao_login/', views.kakaoLoginTemplateView.as_view(), name='kakao_login'),

]


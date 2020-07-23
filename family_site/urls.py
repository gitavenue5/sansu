
from django.conf.urls import url

from . import views


urlpatterns = [

    # daily urls
    url(r'^daily_create/$', views.DailyCreateView.as_view(), name='daily_create'),
    url(r'^daily_list/$', views.DailyListView.as_view(), name='daily_list'),
    url(r'^daily_detail/(?P<pk>\d+)/$', views.DailyDetailView.as_view(), name='daily_detail'),

    # anniversary urls
    url(r'^anniversary_create/$', views.AnniversaryCreateView.as_view(), name='anniversary_create'),
    url(r'^anniversary_list/$', views.AnniversaryListView.as_view(), name='anniversary_list'),

    # 광주은행
    url(r'^gwbank_create/$', views.GwBankCreateView.as_view(), name='gwbank_create'),
    url(r'^gwbank_list/$', views.GwBankListView.as_view(), name='gwbank_list'),

    # 우리은행
    url(r'^wrbank_create/$', views.WrBankCreateView.as_view(), name='wrbank_create'),
    url(r'^wrbank_list/$', views.WrBankListView.as_view(), name='wrbank_list'),
    
    # 게시판
    url(r'^note_create/$', views.NoteCreateView.as_view(), name='note_create'),
    url(r'^note_list/$', views.NoteListView.as_view(), name='note_list'),
    url(r'^note_detail/(?P<pk>\d+)/$', views.NoteDetailView.as_view(), name='note_detail'),
    url(r'^note_update/(?P<pk>[0-9]+)/$', views.NoteUpdateView.as_view(), name='note_update'),
    url(r'^note_delete/(?P<pk>\d+)/$', views.NoteDeleteView.as_view(), name='note_delete'),

    # 게시판 댓글
    url(r'^notecomment_create/(?P<pk>\d+)/$', views.NoteCommentCreateView.as_view(), name='notecomment_create'),    
    url(r'^notecomment_update/(?P<note_pk>\d+)/(?P<pk>\d+)/$', views.NoteCommentUpdateView.as_view(), name='notecomment_update'),
    url(r'^notecomment_delete/(?P<note_pk>\d+)/(?P<pk>\d+)/$', views.NoteCommentDeleteView.as_view(), name='notecomment_delete'),
    
   
    # 카카오

    url(r'kakao/$', views.KakaoView.as_view(), name='kakao_aniversary'),

    url(r'p/$', views.p, name='kakao'),
    
]



from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from family_site.views import AnniversaryViewSet, GwBankViewSet, WrBankViewSet

from family.views import  SansuTemplateView #UserCreateView, UserCreateDoneTemplateView

router = routers.DefaultRouter()
router.register(r'anniversary_api', AnniversaryViewSet)
router.register(r'gwbank_api', GwBankViewSet)
router.register(r'wrbank_api', WrBankViewSet)


urlpatterns = [

    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),

    # serializer
    path('api/', include(router.urls)),  # api 홈 디렉토리
    path('api-auth/', include('rest_framework.urls')),
    
 
    path('', SansuTemplateView.as_view(), name='sansu'),
    path('', include('family_site.urls')),

    # 회원, 로그인
    path('accounts/', include('django.contrib.auth.urls')),
    #url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    #url(r'^accounts/register/done/$', UserCreateDoneTemplateView.as_view(), name='register_done'),

    #django summernote
    path('summernote/', include('django_summernote.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


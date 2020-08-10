

from django.conf.urls import url, include

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from family_site.views import AnniversaryViewSet, GwBankViewSet, WrBankViewSet

from family.views import  SansuTemplateView, UserCreateView, UserCreateDoneTemplateView

router = routers.DefaultRouter()
router.register(r'anniversary_api', AnniversaryViewSet)
router.register(r'gwbank_api', GwBankViewSet)
router.register(r'wrbank_api', WrBankViewSet)


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),


    # serializer
    url(r'^api/', include(router.urls)),  # api 홈 디렉토리
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
 
    url(r'^$', SansuTemplateView.as_view(), name='sansu'),
    url(r'^', include('family_site.urls', namespace='family_site')),

    # 회원, 로그인
    #url(r'^accounts/', include('django.contrib.auth.urls')),
    #url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    #url(r'^accounts/register/done/$', UserCreateDoneTemplateView.as_view(), name='register_done'),

    #django summernote
    url(r'^summernote/', include('django_summernote.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


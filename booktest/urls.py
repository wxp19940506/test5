from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^verifyCode$',views.verifyCode),
    url(r'^verifyTest1',views.verifyTest1),
    url(r'^verifyTest2',views.verifyTest2),
]
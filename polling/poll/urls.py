from django.conf.urls import url
from . import views
app_name='poll'
urlpatterns = [
    url('^$', views.IndexView.as_view(), name='index'),
    url('polling', views.form_data, name='form-data'),
    url('thankyou', views.Bye.as_view(), name='bye'),
    url('poll',views.polling_result, name='poll'),
    url('count', views.Counts.as_view(), name='count'),
    url('result', views.Result.as_view(), name='result')
]
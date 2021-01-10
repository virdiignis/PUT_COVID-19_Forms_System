from django.urls import path
from front import views

urlpatterns = [
    path('', views.home, name='home'),
    path('email', views.email, name='email'),
    path('confirm/<str:token>', views.confirm, name='confirm'),
    path('forms/test/order', views.FormTestOrderModalView.as_view(), name='form_test_order'),
    path('forms/test/result', views.FormTestResultModalView.as_view(), name='form_test_result'),
    path('forms/isolation', views.FormIsolationModalView.as_view(), name='form_isolation'),
]

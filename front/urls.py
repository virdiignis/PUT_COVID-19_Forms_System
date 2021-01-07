from django.urls import path
from front import views

urlpatterns = [
    path('test/order', views.FormTestOrderModalView.as_view(), name='form_test_order'),
    path('test/result', views.FormTestResultModalView.as_view(), name='form_test_result'),
    path('isolation', views.FormIsolationModalView.as_view(), name='form_isolation'),
]

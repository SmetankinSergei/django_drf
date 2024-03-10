from django.urls import path

from users.views import PaymentsListAPIView

urlpatterns = [
    path('payments/', PaymentsListAPIView.as_view()),
]

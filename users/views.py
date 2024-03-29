from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from users.models import Payment
from users.serializers import PaymentSerializer


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['target_course', 'target_lesson', 'payment_option']
    ordering_fields = ['date']

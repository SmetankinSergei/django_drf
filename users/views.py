from rest_framework import generics

from users.models import Payment
from users.serializers import PaymentSerializer


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()

        # по курсу
        course_id = self.request.query_params.get('course_id')
        if course_id:
            return queryset.filter(target_course_id=course_id)

        # по уроку
        lesson_id = self.request.query_params.get('lesson_id')
        if lesson_id:
            return queryset.filter(target_lesson_id=lesson_id)

        # по способу оплаты
        payment_option = self.request.query_params.get('payment_option')
        if payment_option:
            return queryset.filter(payment_option=payment_option)

        # по дате оплаты
        sort_by_date = self.request.query_params.get('sort_by_date')
        if sort_by_date:
            return queryset.order_by('-date') if sort_by_date.lower() == 'desc' else queryset.order_by('date')

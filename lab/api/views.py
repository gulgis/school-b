from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)

from rest_framework import status, permissions, authentication

from rest_framework.views import APIView

from rest_framework.response import Response

from .serializers import StudentSerializer, LabSerializer
from lab.models import Student, Lab


class StudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()


class StudentCreateAPIView(CreateAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()


class StudentDetailAPIView(RetrieveAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()


class StudentDeleteAPIView(DestroyAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()


class LabNumberAPIView(APIView):

    serializer_class = LabSerializer
    model = Lab
    queryset = Student.objects.all()

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, *args, **kwargs):

        url_number = self.kwargs.get("lab_seats")
        print(url_number, "lab_seats")

        lab_qs = Lab.objects.filter(lab_seats__gte=url_number)
        print(lab_qs, "lab_qs")

        number_of_classes = lab_qs.count()

        serialized_data = ClassroomSerializer(lab_qs, many=True)
        # print(serialized_data.data, "serialized_data")

        if serialized_data.is_valid:
            return Response(
                {
                    "lab_data": serialized_data.data,
                    "number_of_classes": number_of_classes,
                },
                status=status.HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                {"Error": "Could not serialize data"},
                status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
            )
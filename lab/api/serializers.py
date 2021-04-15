from rest_framework.serializers import ModelSerializer
from lab.models import Student, Lab


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'username',
            'cod_student',
            'aprooved',
            'average_score',

        )

class LabSerializer(ModelSerializer):
    class Meta:
        model = Lab
        fields = (
            'lab_name',
            'lab_seats',
            'students',

        )



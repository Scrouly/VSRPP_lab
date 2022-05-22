from rest_framework.serializers import ModelSerializer

from lab3_5.models import User, Students, Groups, Faculty


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_active = True
        Students.objects.create(user=user)
        user.save()

        return user


class StudentsSerializer(ModelSerializer):
    class Meta:
        model = Students
        fields = ('id', 'name', 'surname', 'phone_number', 'group',)


class GroupsSerializer(ModelSerializer):
    class Meta:
        model = Groups
        fields = ('group_id', 'gr_name', 'faculty',)


class FacultySerializer(ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id', 'faculty_name', 'phone_number',)

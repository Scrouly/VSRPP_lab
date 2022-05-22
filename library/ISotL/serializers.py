from rest_framework.serializers import ModelSerializer

from ISotL.models import User, Books


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.groups = 1
        user.is_active = True
        user.save()
        return user


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def create(self, validated_data):
        book = Books.objects.create(**validated_data)
        book.in_stock = True
        print(book.renter)
        book.save()
        return book

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.renter = validated_data.get('renter', instance.renter)
        if instance.renter == None:
            instance.in_stock = True
        else:
            instance.in_stock = False
        instance.save()
        return instance

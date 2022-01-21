from rest_framework import serializers
from .models import Courses

class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Courses
        #fileds = ('id','name','languages','price')
        fields = '__all__'

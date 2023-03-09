from django.contrib.auth.models import User
from rest_framework import serializers

# in dem serializer wird festgelegt welche felder man aus dem entsprechenden model in seiner api haben möchte.
# mit der zeile model = User wird das entsprechende Model was man serialisieren möchte festgelegt. zum bsp könnte man auch schreiben model = todo


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name',]


# class TaskSerializer

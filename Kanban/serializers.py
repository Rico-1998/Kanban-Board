class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        # model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name']

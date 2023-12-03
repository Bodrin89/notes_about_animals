
from rest_framework import serializers

from apps.blogs.models import Blog
from apps.blogs.services import BlogServices
from apps.images.models import Images


class GetBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('id', 'title', 'text', 'image')


class CreateBlogSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    image = serializers.PrimaryKeyRelatedField(queryset=Images.objects.all(),
                                               required=False,
                                               allow_null=True)

    class Meta:
        model = Blog
        fields = ('title', 'text', 'image', 'user')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        images_for_user = Images.objects.filter(user=user)
        self.fields['image'].queryset = images_for_user

    def create(self, validated_data):
        return BlogServices.create_blog(validated_data)


class UpdateBlogSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    text = serializers.CharField(required=False)
    title = serializers.CharField(required=False)

    class Meta:
        model = Blog
        fields = ('title', 'text', 'image', 'is_active', 'user')

    def update(self, instance, validated_data):
        return BlogServices.update_blog(instance, validated_data)

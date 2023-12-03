from apps.blogs.models import Blog


class BlogServices:

    @staticmethod
    def create_blog(validated_data: dict):
        """Создать новый блог"""
        image = validated_data.pop('image')
        if image:
            return Blog.objects.create(**validated_data, image_id=image.id)
        return Blog.objects.create(**validated_data)

    @staticmethod
    def update_blog(instance: Blog, validated_data: dict):
        """Обновить блог"""
        title = validated_data.get('title', instance.title)
        text = validated_data.get('text', instance.text)
        image = validated_data.get('image', instance.image)
        is_active = validated_data.get('is_active')
        if is_active == instance.is_active:
            is_active = instance.is_active
        Blog.objects.filter(pk=instance.pk).update(
            title=title,
            text=text,
            image=image,
            is_active=is_active
        )
        updated_instance = Blog.objects.get(pk=instance.pk)
        updated_instance.save()
        return updated_instance

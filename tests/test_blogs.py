import pytest
from django.urls import reverse
from tests.factories import BlogFactory


@pytest.mark.django_db
class TestBlog:
    url_blog_creat = reverse('apps.blogs:create-blog')
    url_blog_list = reverse('apps.blogs:list-blog')

    def test_blog_create_unregister_user(self, client, blog, clear_cache):
        """Создание блога не зарегистрированным пользователем"""

        data = {
            "title": blog.title,
            "text": blog.text,
            "image": blog.image_id
        }

        response = client.post(self.url_blog_creat, data=data)
        assert response.status_code == 403

    def test_blog_create_register_user(self, get_auth_client, blog, clear_cache):
        """Создание блога зарегистрированным пользователем"""

        data = {
            "title": blog.title,
            "text": blog.text,
            "image": blog.image_id
        }

        response = get_auth_client.post(self.url_blog_creat, data=data)
        assert response.data == {'title': data['title'], 'text': data['text'], 'image': data['image']}
        assert response.status_code == 201

    def test_get_blog_id(self, client, blog, clear_cache):
        """Тест получения блога по id"""
        url_blog_get_id = reverse('apps.blogs:get-blog', kwargs={'pk': blog.pk})

        expected_response = {
            "id": blog.id,
            "title": blog.title,
            "text": blog.text,
            "image": blog.image_id
        }

        response = client.get(url_blog_get_id)
        assert response.status_code == 200
        assert response.data == expected_response

    def test_get_list_blog(self, client, clear_cache):
        """Тест на получение всех активных блогов"""
        active_blogs = BlogFactory.create_batch(2, is_active=True)
        inactive_blog = BlogFactory.create_batch(2, is_active=False)

        blogs = active_blogs + inactive_blog

        response = client.get(self.url_blog_list)

        assert response.status_code == 200
        assert len(response.data) == 2
        assert len([blog for blog in response.data if blog['is_active']]) == 2
        assert len(blogs) == 4

    def test_update_blog_owner(self, get_auth_client, blog, clear_cache):
        """Тест изменения блога зарегистрированным пользователем и являющегося хозяином блога"""
        url_blog_get_update = reverse('apps.blogs:update-blog', kwargs={'pk': blog.pk})
        data = {
            'text': 'Текст измененный',
            'title': 'Измененный заголовок',
            'is_active': False
        }
        response = get_auth_client.put(url_blog_get_update, data=data)
        assert response.status_code == 200
        assert response.data == {'title': data['title'],
                                 'text': data['text'],
                                 'image': blog.image_id,
                                 'is_active': data['is_active']}

    def test_update_blog_not_owner(self, not_owner_auth_client, blog, clear_cache):
        """Тест изменения блога зарегистрированным пользователем и не являющегося хозяином блога"""
        url_blog_get_update = reverse('apps.blogs:update-blog', kwargs={'pk': blog.pk})
        data = {
            'text': 'Текст измененный',
            'title': 'Измененный заголовок',
            'is_active': False
        }
        response = not_owner_auth_client.put(url_blog_get_update, data=data)
        assert response.status_code == 403

    def test_update_blog_not_auth_user(self, client, blog, clear_cache):
        """Тест на изменение блога не аутентифицированным пользователем"""
        url_blog_get_update = reverse('apps.blogs:update-blog', kwargs={'pk': blog.pk})
        data = {
            'text': 'Текст измененный',
            'title': 'Измененный заголовок',
            'is_active': False
        }
        response = client.put(url_blog_get_update, data=data)
        assert response.status_code == 403

    def test_deleted_blog(self, get_auth_client, blog, clear_cache):
        """Тест на удаление блога хозяином"""
        url_delete_blog = reverse('apps.blogs:destroy-blog', kwargs={'pk': blog.pk})
        response = get_auth_client.delete(url_delete_blog)
        assert response.status_code == 204

    def test_deleted_blog_not_owner(self, not_owner_auth_client, blog, clear_cache):
        """Тест на удаление блога не хозяином"""
        url_delete_blog = reverse('apps.blogs:destroy-blog', kwargs={'pk': blog.pk})
        response = not_owner_auth_client.delete(url_delete_blog)
        assert response.status_code == 403

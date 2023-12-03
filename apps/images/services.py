import os
import aiofiles

import httpx
from django.http import JsonResponse
from dotenv import load_dotenv
import asyncio

from apps.images.models import Images
from config.settings import LOGGER

load_dotenv()

ACCESS_KEY = os.getenv('ACCESS_KEY')


async def get_url_image(search_foto: str, page: int):
    """Получение ссылок для скачивания картинки"""
    headers = {'Accept-Version': 'v1', 'Authorization': f"Client-ID {ACCESS_KEY}"}
    params = {'query': search_foto, 'page': page}
    url = 'https://api.unsplash.com/search/photos'

    async with httpx.AsyncClient() as client:
        res = await client.get(url=url, params=params, headers=headers)
        if res.status_code == 200:
            response = res.json()
            if response.get('results'):
                return response.get('results')[0].get('urls').get('small')


async def download_images(user_id: int, url: str, query: str):
    """Скачивание картинки и загрузка в БД"""
    async with httpx.AsyncClient() as client:
        file_name = f"media/{user_id}/{url.split('/')[-1]}.jpeg"
        directory = os.path.dirname(file_name)
        if not os.path.exists(directory):
            os.makedirs(directory)
        res = await client.get(url=url)
        async with aiofiles.open(file_name, "wb+") as f:
            await f.write(res.read())
            await Images.objects.aget_or_create(user_id=user_id, title=query, url=file_name)


async def save_images(user_id: int, query: str, count: int):
    link_images = await search_image(query, count)
    await asyncio.gather(
        *(download_images(user_id=user_id, url=url, query=query) for url in link_images),
        return_exceptions=True
    )
    return link_images


async def search_image(query: str, count: int):
    page = 0
    images = await asyncio.gather(
        *(get_url_image(query, count) for count in range(page, count)),
        return_exceptions=True
    )
    return images



import json

from asgiref.sync import sync_to_async
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from apps.images.services import save_images


@method_decorator(csrf_exempt, name='dispatch')
class GetUrlImage(View):

    @sync_to_async
    def read_body_sync(self, request):
        return request.read()

    @sync_to_async
    def read_user_sync(self, request):
        user = request.user
        is_authenticated = request.user.is_authenticated
        return {'user': user, 'is_authenticated': is_authenticated}

    async def post(self, request, *args, **kwargs):
        request_body = await self.read_body_sync(request)
        user_is_authenticated = await self.read_user_sync(request)
        if not user_is_authenticated['is_authenticated']:
            return JsonResponse("Вы не авторизованы", safe=False)
        user = user_is_authenticated['user']
        body = request_body
        data = json.loads(body.decode('utf-8'))
        count = int(data.get('count'))
        search = data.get('search')
        response = await save_images(user_id=user.id, query=search, count=count)
        return JsonResponse(response, safe=False)




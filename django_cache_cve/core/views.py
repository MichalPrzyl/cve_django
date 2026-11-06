from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
from django.views.decorators.cache import cache_page

#@cache_page(6)
@api_view(["POST"])
def create_cache(request):
    cache.set("user_1", "Michał", timeout=4)
    return Response("Cache created")
    
@cache_page(20)
@api_view(["GET"])
def get_cache(request):
    user_id = request.headers['X-USER-ID']
    print(f"user_id: {user_id}")
    ret = cache.get("user_id")
    return Response({
        'user_id': ret,
        'secret': f'secret_for_user_{user_id}'
    })

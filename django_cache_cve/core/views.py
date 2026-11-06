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
    ret = cache.get("user_1")
    return Response(ret)

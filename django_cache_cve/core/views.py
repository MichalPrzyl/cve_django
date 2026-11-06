from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

@cache_page(20)
@vary_on_headers('X-USER-ID')
@api_view(["GET"])
def get_cache(request):
    print(f"get cache request, headers: {request.headers}")
    user_id = request.headers.get('X-USER-ID')
    if user_id is None:
        return Response({
            "role": "ADMIN",
            "token": "super-secret-token"
        })

    return Response({
        "role": "GUEST",
        "token": "NO DATA"
    })


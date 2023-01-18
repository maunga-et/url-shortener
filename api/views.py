from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from core.models import Url
from core.id_generator import generate_id
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def shorten_url(request):
    url = request.data.__getitem__('url')
    url_id = ''
    while True:
        unique_id = generate_id()
        try:
            is_used = Url.objects.get(unique_id=unique_id)
        except Url.DoesNotExist:
            url_id = unique_id
            break
    if request.user.id is not None:
        new_url = Url(user = User.objects.get(pk = request.user.id), url=url, unique_id=url_id)
        new_url.save()
    else:
        new_url = Url(url=url, unique_id=url_id)
        new_url.save()

    return Response({
        "data": url_id
    })
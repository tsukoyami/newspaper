
from django.http import JsonResponse
from .models import Subscriber
from .serializers import SubscriberSerialiser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def subscriber(request):
    if request.method == 'GET':
        sources = Subscriber.objects.all()
        serializer = SubscriberSerialiser(sources, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        serializer = SubscriberSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
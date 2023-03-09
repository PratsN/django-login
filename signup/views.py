from django.shortcuts import render
from .models import Registration
from .serializers import RegistrationSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


# Create your views here.


def index(request):
    return render(request, 'index.html')


@api_view(['GET', 'POST'])
@csrf_exempt
def register(request):
    if (request.method == 'POST'):
        signup_serializer = RegistrationSerializer(data=request.data)
        if signup_serializer.is_valid():
            signup_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    else:
        return render(request, 'register.html')


@ api_view(['GET'])
@ csrf_exempt
def data(request):
    if (request.method == 'GET'):
        userData = Registration.objects.all()
        userSerialize = RegistrationSerializer(userData, many=True)
    return render(request, 'data.html', {'result': userSerialize.data})

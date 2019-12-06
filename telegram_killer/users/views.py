from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.http import Http404

# Create your views here.
def profile(request, id):
    if request.method == "GET":
        try:
            profile = request.GET.get('profile')
        except profile.DoesNotExist:
            return Http404
        return JsonResponse({'Name':'Shavros', 'Status':'Student'})
    else:
        return HttpResponseNotAllowed(['GET'])

def contacts(request, id):
    if request.method == "GET":
        try:
            contacts = request.GET.get('contacts')
        except contacts.DoesNotExist:
            return Http404
        return JsonResponse({'name': 'Katya', 'phone number': '8 912 345 67 89'})
    else:
        return HttpResponseNotAllowed(['GET'])


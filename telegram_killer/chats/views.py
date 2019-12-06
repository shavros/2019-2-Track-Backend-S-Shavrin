from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.http import Http404

# Create your views here.
def chat_list(request, id):
    if request.method == "GET":
        try:
            chat_list = request.GET.get('chat_list')
        except chat_list.DoesNotExist:
            return Http404
        return JsonResponse({'first chat': 'Lena', 'second chat': 'Kolya'})
    else:
        return HttpResponseNotAllowed(['GET'])

def one_chat(request, id):
    if request.method == "GET":
        try:
            chat = request.GET.get('chat')
        except chat.DoesNotExist:
            return Http404
        return JsonResponse({'message': 'Hello!', 'time': '22:22'})
    else:
        return HttpResponseNotAllowed(['GET'])

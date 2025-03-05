from django.http import JsonResponse


def getUid(request):
    print(1234)
    return JsonResponse({
        'result': "success",
        'id': 123,
        'photo': 123,
    })

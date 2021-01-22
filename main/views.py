from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Do_list

# Create your views here.
def index(request):
    all_data = Do_list.objects.order_by('id')
    context = {"Do_list_data" : all_data}
    return render(request, 'main/index.html', context)
    # return HttpResponse("To_do_list 메인 화면입니다.")

def detail(request, do_list_id):
    try:
        id_data = Do_list.objects.get(pk=do_list_id)
    except Do_list.DoesNotExist:
        raise Http404("없는 정보입니다.")
    context = {"id_data" : id_data}
    return render(request, 'main/detail.html', context)
    # return HttpResponse(f"{do_list_id} detail 입니다.")

def add(request):
    if request.method == 'GET':
        return render(request, 'main/add.html')
    elif request.method == 'POST':
        
        return HttpResponse(f"{request.POST['information']}")
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Do_list
from django.urls import reverse
from django.utils import timezone

# Create your views here.
def index(request):
    all_data = Do_list.objects.filter(state=True).order_by("id")
    context = {"Do_list_data": all_data}
    return render(request, "main/index.html", context)
    # return HttpResponse("To_do_list 메인 화면입니다.")


def detail(request, do_list_id):
    if request.method == "GET":
        try:
            id_data = Do_list.objects.get(pk=do_list_id)
        except Do_list.DoesNotExist:
            raise Http404("없는 정보입니다.")
        context = {"id_data": id_data}
        return render(request, "main/detail.html", context)
        # return HttpResponse(f"{do_list_id} detail 입니다.")
    elif request.method == "POST":
        id_data = Do_list.objects.get(pk=do_list_id)
        id_data.state = False
        id_data.save()
        return HttpResponseRedirect(reverse("main:index"))


def add(request):
    if request.method == "GET":
        return render(request, "main/add.html")
    elif request.method == "POST":
        content = request.POST["content"]
        information = request.POST["information"]
        add_list = Do_list(
            content=content, information=information, pub_date=timezone.now()
        )
        add_list.save()
        return HttpResponseRedirect(reverse("main:index"))


def change(request, do_list_id):
    if request.method == "GET":
        try:
            id_data = Do_list.objects.get(pk=do_list_id)
        except Do_list.DoesNotExist:
            raise Http404("없는 정보입니다.")
        context = {"id_data": id_data}
        return render(request, "main/change.html", context)
    elif request.method == "POST":
        content = request.POST["content"]
        information = request.POST["information"]
        id_data = Do_list.objects.get(pk=do_list_id)
        id_data.content = content
        id_data.information = information
        id_data.modify_date = timezone.now()
        id_data.save()
        return HttpResponseRedirect(reverse("main:index"))
    # return HttpResponse(f"{do_list_id} change 입니다.")

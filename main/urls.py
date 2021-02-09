from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:do_list_id>/", views.detail, name="detail"),
    path("add/", views.add, name="add"),
    path("change/<int:do_list_id>/", views.change, name="change"),
    # path('delete/<int:do_list_id>/', views.delete, name='delete'),
]

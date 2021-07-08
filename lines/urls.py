from django.urls import path
from .import views


urlpatterns = [
    path("", views.line_index, name="line_index"),
    path("<int:line_id>", views.line_detail, name="line_detail"),
    path("<int:line_id>/booking", views.booking, name="booking"),

]

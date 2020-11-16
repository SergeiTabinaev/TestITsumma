from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import manage_items, manage_item
from decouple import config


urlpatterns = {
    path('', manage_items, name="items"),
    path('<slug:key>', manage_item, name="single_item") #config('RECIEVER_URL'))
}
urlpatterns = format_suffix_patterns(urlpatterns)

# Первый путь http://127.0.0.1:8000/DataReciever
# а второй путь http://127.0.0.1:8000/DataReciever/mem cpu disk net

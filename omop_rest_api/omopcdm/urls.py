from django.urls import include, path
from .views import TextAPIView

urlpatterns = [

    path('', TextAPIView.as_view(), name ="omopcdm"),
    
   
]

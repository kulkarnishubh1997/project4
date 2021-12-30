from django.urls import path
from demo import views
app_name='demo'

urlpatterns=[
    path('',views.sample,name="sample"),
]


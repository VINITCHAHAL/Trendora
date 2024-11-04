from django.contrib import admin
from django.urls import path,include


from UserServices.Controller.DynamicFormController import DynamicFormController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('UserServices.urls')),
    path('api/getForm/<str:modelName>/',DynamicFormController.as_view(),name='dynamicForm'),
    path('api/getForm/<str:modelName>/<str:id>/',DynamicFormController.as_view(),name='dynamicForm'),
]

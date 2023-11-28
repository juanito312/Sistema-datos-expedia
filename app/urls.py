from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('principal/', views.principal, name='principal'),
    path('iniciar_sesion/',views.iniciar_sesion, name='iniciar_sesion'),
    path('subir_csv/',views.subir_csv, name='subir_csv'),
    path('cargar_csv/', views.cargar_csv, name='cargar_csv'),
    path('registros_expedia/', views.registros_expedia, name='registros_expedia'),
    path('list_expedia', views.list_expedia, name='list_expedia'),
    path('mineria/', views.mineria_datos, name='mineria'),
    path('estadistica/', views.estadistica, name='estadistica'),
    path('grafica_1/', views.grafica_1, name='grafica_1'),
    path('grafica_2/', views.grafica_2, name='grafica_2'),
    path('grafica_3/', views.grafica_3, name='grafica_3'),
    path('grafica_4/', views.grafica_4, name='grafica_4'),
    path('grafica_5/', views.grafica_5, name='grafica_5'),
    path('grafica_6/', views.grafica_6, name='grafica_6'),
    path('grafica_7/', views.grafica_7, name='grafica_7'),
    path('grafica_8/', views.grafica_8, name='grafica_8'),
    path('modelo_1/', views.modelo_1, name='modelo_1'),
    path('modelo_2/', views.modelo_2, name='modelo_2'),
    path('modelo_3/', views.modelo_3, name='modelo_3'),
    path('modelo_4/', views.modelo_4, name='modelo_4'),
    path('modelo_5/', views.modelo_5, name='modelo_5'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Expedia
from .models import Usuario
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.http.response import JsonResponse
from django.http import JsonResponse
import json
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from django.contrib.auth import views as auth_views

# <---- Seccion para Vistas en la aplicacion ------>

# Constantes para algunas vistas
pagina_inicio = 'index.html'
acceso = 'login.html'
dash_Estadistica = 'estadistica.html'
dash_Mineria = 'mineria.html'

# Vista de la pagina principal
def index(request):
    return render(request, pagina_inicio)

# Vista del formulario
def login(request):
    return render(request, acceso)

# Vista del formulario del registro
def registro(request):
    return render(request, 'registro.html')

# Vista de pagina principal
def principal(request):
    return render(request, 'principal.html')

# Vista para subir el archivo csv
def subir_csv(request):
    return render(request, 'subir_csv.html')

# Vista para mostrar los registros del tabla Expedia
def registros_expedia(request):
    return render(request, 'registros_expedia.html')

# Vista para mostrar el dashboar sobre  Mineria de Datos
def mineria_datos(request):
    return render(request, 'mineria.html')

# Vista para mostrar el dashboard sobre Datos Estadisticos
def estadistica(request):
    return render(request, dash_Estadistica)


#<---- Seccion para procesos en la aplicacion ------>
# Proceso para registrar el usuario en la base de datos
def registro_usuario(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        password = request.POST['password']

        # Insertamos el usuario en la base de datos
        Usuario.objects.create(nombre = usuario, contrasenia = password)

    return render(request, acceso)
# Proceso para acceder a la pagina principal
def iniciar_sesion(request):
    if request.method == 'POST':
            usuario = request.POST['usuario']
            password = request.POST['password']
            user = authenticate(request, username=usuario, password=password)
            print(user)
            if user is not None:
                login(request)
                return redirect('principal')
            else:
                return render(request, acceso, {'error': 'Usuario o Contraseña incorrecta'})

    return render(request, acceso)
# Proceso para cargar la tabla
def list_expedia(_request):
    expedia = list(Expedia.objects.values())
    data = {'expedia': expedia}
    return JsonResponse(data)
# Proceso para poder subir el archivo csv a la base de datos
def cargar_csv(request):
    if request.method == 'POST' and request.FILES['archivo_csv']:
        archivo_csv = request.FILES['archivo_csv']
        
        # Guardamos el archivo en el sistema de archivos
        fs = FileSystemStorage()
        nombre_archivo = fs.save(archivo_csv.name, archivo_csv)
        ruta_local_archivo = fs.path(nombre_archivo)
        
        # Leemos el archivo con pandas
        df = pd.read_csv(ruta_local_archivo)
    
        # Borrar la tabla antes de cargar nuevos datos
        Expedia.objects.all().delete()
        
        for index, row in df.iterrows():
            Expedia.objects.create(
                srch_id=row['srch_id'],
                site_id=row['site_id'],
                visitor_location_country_id=row['visitor_location_country_id'],
                visitor_hist_starrating=row['visitor_hist_starrating'],
                visitor_hist_adr_usd=row['visitor_hist_adr_usd'],
                prop_country_id=row['prop_country_id'],
                prop_id=row['prop_id'],
                prop_starrating=row['prop_starrating'],
                prop_review_score=row['prop_review_score'],
                prop_brand_bool=row['prop_brand_bool'],
                prop_location_score1=row['prop_location_score1'],
                prop_location_score2=row['prop_location_score2'],
                price_usd=row['price_usd'],
                promotion_flag=row['promotion_flag'],
                srch_destination_id=row['srch_destination_id'],
                srch_length_of_stay=row['srch_length_of_stay'],
                srch_booking_window=row['srch_booking_window'],
                srch_adults_count=row['srch_adults_count'],
                srch_children_count=row['srch_children_count'],
                srch_room_count=row['srch_room_count'],
                srch_saturday_night_bool=row['srch_saturday_night_bool'],
                srch_query_affinity_score=row['srch_query_affinity_score'],
                orig_destination_distance=row['orig_destination_distance'],
                comp1_rate=row['comp1_rate'],
                comp1_inv=row['comp1_inv'],
                comp1_rate_percent_diff=row['comp1_rate_percent_diff'],
                comp2_rate=row['comp2_rate'],
                comp2_inv=row['comp2_inv'],
                comp2_rate_percent_diff=row['comp2_rate_percent_diff'],
                comp3_rate=row['comp3_rate'],
                comp3_inv=row['comp3_inv'],
                comp3_rate_percent_diff=row['comp3_rate_percent_diff'],
                comp4_rate=row['comp4_rate'],
                comp4_inv=row['comp4_inv'],
                comp4_rate_percent_diff=row['comp4_rate_percent_diff'],
                comp5_rate=row['comp5_rate'],
                comp5_inv=row['comp5_inv'],
                comp5_rate_percent_diff=row['comp5_rate_percent_diff'],
                comp6_rate=row['comp6_rate'],
                comp6_inv=row['comp6_inv'],
                comp6_rate_percent_diff=row['comp6_rate_percent_diff'],
                comp7_rate=row['comp7_rate'],
                comp7_inv=row['comp7_inv'],
                comp7_rate_percent_diff=row['comp7_rate_percent_diff'],
                comp8_rate=row['comp8_rate'],
                comp8_inv=row['comp8_inv'],
                comp8_rate_percent_diff=row['comp8_rate_percent_diff'],
                day=row['day'],
                month=row['month'],
                year=row['year']
            )
        
    return render(request, 'principal.html')

# <----- Procesos para cargar las Graficas en el Dashboar Estadistico ----->
def grafica_1(request):
    # Obtener los daros de la tabla
    datos_expedia = Expedia.objects.values('month','price_usd')
    
    # Convierte los datos a una lista de diccionarios
    datos_expedia_list = list(datos_expedia)
    
    # Convertir la lista de diccionarios a una cadena JSON
    datos_expedia_json = json.dumps(datos_expedia_list)
    
    # Renderizamos la plantilla con el contexto
    return render(request, dash_Estadistica, {'datos_expedia_json': datos_expedia_json})

def grafica_2(request):
    
    datos_expedia = Expedia.objects.values('price_usd', 'prop_starrating')
    datos_expedia_list2 = list(datos_expedia)
    datos_expedia_json2 = json.dumps(datos_expedia_list2)
    
    return render(request, dash_Estadistica, {'datos_expedia_json2': datos_expedia_json2})

def grafica_3(request):
    # Obtener datos de Expedia y filtrar valores nulos en visitor_location_country_id
    datos_expedia = Expedia.objects.exclude(visitor_location_country_id__isnull=True).values('visitor_location_country_id')
    
    # Verificar si hay datos antes de convertir a JSON
    if datos_expedia.exists():
        # Convertir QuerySet a lista y luego a JSON
        datos_expedia_list3 = list(datos_expedia)
        datos_expedia_json3 = json.dumps(datos_expedia_list3, default=str)  # Usamos default=str para manejar objetos datetime
        return render(request, dash_Estadistica, {'datos_expedia_json3': datos_expedia_json3})
    else:
        return render(request, dash_Estadistica, {'datos_expedia_json3': '[]'})  # Envía un array vacío si no hay datos

def grafica_4(request):
    datos_expedia = Expedia.objects.exclude(prop_starrating__isnull=True).values('prop_starrating')
    # Verificar si hay datos antes de convertir a JSON
    if datos_expedia.exists():
        # Convertir QuerySet a lista y luego a JSON
        datos_expedia_list4 = list(datos_expedia)
        datos_expedia_json4 = json.dumps(datos_expedia_list4, default=str)  # Usamos default=str para manejar objetos datetime
        return render(request, dash_Estadistica, {'datos_expedia_json4': datos_expedia_json4})
    else:
        return render(request, dash_Estadistica, {'datos_expedia_json4': '[]'})  # Envía un array vacío si no hay datos

def grafica_5(request):
    datos_expedia = Expedia.objects.exclude(prop_review_score__isnull=True).values('prop_review_score')
    # Verificar si hay datos antes de convertir a JSON
    if datos_expedia.exists():
        # Convertir QuerySet a lista y luego a JSON
        datos_expedia_list5 = list(datos_expedia)
        datos_expedia_json5 = json.dumps(datos_expedia_list5, default=str)  # Usamos default=str para manejar objetos datetime
        return render(request, dash_Estadistica, {'datos_expedia_json5': datos_expedia_json5})
    else:
        return render(request, dash_Estadistica, {'datos_expedia_json5': '[]'})  # Envía un array vacío si no hay datos

def grafica_6(request):
    datos_expedia = Expedia.objects.exclude(srch_length_of_stay__isnull=True).values('srch_length_of_stay')
    # Verificar si hay datos antes de convertir a JSON
    if datos_expedia.exists():
        # Convertir QuerySet a lista y luego a JSON
        datos_expedia_list6 = list(datos_expedia)
        datos_expedia_json6 = json.dumps(datos_expedia_list6, default=str)  # Usamos default=str para manejar objetos datetime
        return render(request, dash_Estadistica, {'datos_expedia_json6': datos_expedia_json6})
    else:
        return render(request, dash_Estadistica, {'datos_expedia_json6': '[]'})  # Envía un array vacío si no hay datos

def grafica_7(request):
    datos_expedia = Expedia.objects.exclude(srch_room_count__isnull=True).values('srch_room_count')
    # Verificar si hay datos antes de convertir a JSON
    if datos_expedia.exists():
        # Convertir QuerySet a lista y luego a JSON
        datos_expedia_list7 = list(datos_expedia)
        datos_expedia_json7 = json.dumps(datos_expedia_list7, default=str)  # Usamos default=str para manejar objetos datetime
        return render(request, dash_Estadistica, {'datos_expedia_json7': datos_expedia_json7})
    else:
        return render(request, dash_Estadistica, {'datos_expedia_json7': '[]'})  # Envía un array vacío si no hay datos

def grafica_8(request):
    datos_expedia = Expedia.objects.exclude(srch_saturday_night_bool__isnull=True).values('srch_saturday_night_bool')
    # Verificar si hay datos antes de convertir a JSON
    if datos_expedia.exists():
        # Convertir QuerySet a lista y luego a JSON
        datos_expedia_list8 = list(datos_expedia)
        datos_expedia_json8 = json.dumps(datos_expedia_list8, default=str)  # Usamos default=str para manejar objetos datetime
        return render(request, dash_Estadistica, {'datos_expedia_json8': datos_expedia_json8})
    else:
        return render(request, dash_Estadistica, {'datos_expedia_json8': '[]'})  # Envía un array vacío si no hay datos

# <----- Procesos para cargar las Graficas en el Dashboar Mineria de Datos ----->
def modelo_1(request):
    # Obtener los datos
    datos_expedia = Expedia.objects.all()

    # Crear un DataFrame
    datos = pd.DataFrame(list(datos_expedia.values()))

    # Validar que los datos existan
    if 'visitor_hist_adr_usd' in datos.columns and 'visitor_hist_starrating' in datos.columns:
        X = datos['visitor_hist_adr_usd'].to_list()  # Variable predictora
        y = datos['visitor_hist_starrating'].to_list()  # Variable objetivo

        # Crear el modelo
        model = LinearRegression()

        # Entrenar el modelo
        X = pd.DataFrame(X)  # Asegurarse de que X sea un DataFrame
        model.fit(X, y)

        # Hacer predicciones
        y_pred = model.predict(X).tolist()

        # Calcular el coeficiente de determinación
        r2 = r2_score(y, y_pred)
        print(f'Coeficiente de Determinación: {r2:.2f}')

        # Pasar los datos al contexto
        context = {
            'datos_originales': json.dumps({'x': X.squeeze().tolist(), 'y': y}),  # Squeeze para convertir DataFrame a lista
            'datos_predichos': json.dumps({'x': X.squeeze().tolist(), 'y': y_pred}),
            'r2_score': r2,
        }

        # Renderizar el template
        return render(request, dash_Mineria, context)

def modelo_2(request):
    # Obtener los datos
    datos_expedia = Expedia.objects.all()

    # Crear un DataFrame
    datos = pd.DataFrame(list(datos_expedia.values()))

    # Validar que los datos existan
    if 'srch_adults_count' in datos.columns and 'srch_room_count' in datos.columns:
        X = datos['srch_adults_count'].to_list()  # Variable predictora
        y = datos['srch_room_count'].to_list()  # Variable objetivo

        # Crear el modelo
        model = LinearRegression()

        # Entrenar el modelo
        X = pd.DataFrame(X)  # Asegurarse de que X sea un DataFrame
        model.fit(X, y)

        # Hacer predicciones
        y_pred = model.predict(X).tolist()

        # Calcular el coeficiente de determinación
        r2 = r2_score(y, y_pred)
        print(f'Coeficiente de Determinación: {r2:.2f}')

        # Pasar los datos al contexto
        context = {
            'datos_originales2': json.dumps({'x': X.squeeze().tolist(), 'y': y}),  # Squeeze para convertir DataFrame a lista
            'datos_predichos2': json.dumps({'x': X.squeeze().tolist(), 'y': y_pred}),
            'r2_score': r2,
        }

        # Renderizar el template
        return render(request, dash_Mineria, context)

def modelo_3(request):
    # Obtener los datos
    datos_expedia = Expedia.objects.all()

    # Crear un DataFrame
    datos = pd.DataFrame(list(datos_expedia.values()))

    # Validar que los datos existan
    if 'visitor_location_country_id' in datos.columns and 'prop_country_id' in datos.columns:
        X = datos['visitor_location_country_id'].to_list()  # Variable predictora
        y = datos['prop_country_id'].to_list()  # Variable objetivo

        # Crear el modelo
        model = LinearRegression()

        # Entrenar el modelo
        X = pd.DataFrame(X)  # Asegurarse de que X sea un DataFrame
        model.fit(X, y)

        # Hacer predicciones
        y_pred = model.predict(X).tolist()

        # Calcular el coeficiente de determinación
        r2 = r2_score(y, y_pred)
        print(f'Coeficiente de Determinación: {r2:.2f}')

        # Pasar los datos al contexto
        context = {
            'datos_originales3': json.dumps({'x': X.squeeze().tolist(), 'y': y}),  # Squeeze para convertir DataFrame a lista
            'datos_predichos3': json.dumps({'x': X.squeeze().tolist(), 'y': y_pred}),
            'r2_score': r2,
        }

        # Renderizar el template
        return render(request, dash_Mineria, context)

def modelo_4(request):
    # Obtener los datos
    datos_expedia = Expedia.objects.all()

    # Crear un DataFrame
    datos = pd.DataFrame(list(datos_expedia.values()))

    # Validar que los datos existan
    if 'prop_location_score2' in datos.columns and 'prop_location_score1' in datos.columns:
        X = datos['prop_location_score2'].to_list()  # Variable predictora
        y = datos['prop_location_score1'].to_list()  # Variable objetivo

        # Crear el modelo
        model = LinearRegression()

        # Entrenar el modelo
        X = pd.DataFrame(X)  # Asegurarse de que X sea un DataFrame
        model.fit(X, y)

        # Hacer predicciones
        y_pred = model.predict(X).tolist()

        # Calcular el coeficiente de determinación
        r2 = r2_score(y, y_pred)
        print(f'Coeficiente de Determinación: {r2:.2f}')

        # Pasar los datos al contexto
        context = {
            'datos_originales4': json.dumps({'x': X.squeeze().tolist(), 'y': y}),  # Squeeze para convertir DataFrame a lista
            'datos_predichos4': json.dumps({'x': X.squeeze().tolist(), 'y': y_pred}),
            'r2_score': r2,
        }

        # Renderizar el template
        return render(request, dash_Mineria, context)

def modelo_5(request):
    # Obtener los datos
    datos_expedia = Expedia.objects.all()

    # Crear un DataFrame
    datos = pd.DataFrame(list(datos_expedia.values()))

    # Validar que los datos existan
    if 'srch_length_of_stay' in datos.columns and 'srch_booking_window' in datos.columns:
        X = datos['srch_length_of_stay'].to_list()  # Variable predictora
        y = datos['srch_booking_window'].to_list()  # Variable objetivo

        # Crear el modelo
        model = LinearRegression()

        # Entrenar el modelo
        X = pd.DataFrame(X)  # Asegurarse de que X sea un DataFrame
        model.fit(X, y)

        # Hacer predicciones
        y_pred = model.predict(X).tolist()

        # Calcular el coeficiente de determinación
        r2 = r2_score(y, y_pred)
        print(f'Coeficiente de Determinación: {r2:.2f}')

        # Pasar los datos al contexto
        context = {
            'datos_originales5': json.dumps({'x': X.squeeze().tolist(), 'y': y}),  # Squeeze para convertir DataFrame a lista
            'datos_predichos5': json.dumps({'x': X.squeeze().tolist(), 'y': y_pred}),
            'r2_score': r2,
        }

        # Renderizar el template
        return render(request, dash_Mineria, context)

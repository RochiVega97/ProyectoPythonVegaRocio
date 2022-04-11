from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Entregable, Estudiante, Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario
#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from AppCoder.forms import CursoFormulario, ProfesorFormulario, UserRegisterForm,UserEditForm, EstudiantesFormulario, EntregablesFormulario

from django.contrib.auth.decorators import login_required

# Create your views here.

def curso(request):
      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"

      return HttpResponse(documentoDeTexto)

def inicio(request):
      return render(request, "AppCoder/inicio.html")

def AcercaDeMi(request):
      return render(request, "AppCoder/AcercaDeMi.html")

def LeerMas(request):
      return render(request, "AppCoder/LeerMas.html")

def Contacto(request):
      return render(request, "AppCoder/Contacto.html")

def estudiantes(request):
      if request.method == 'POST':
            miFormulario = EstudiantesFormulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  estudiante = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'],
                  email=informacion['email']) 
                  estudiante.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= EstudiantesFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/estudiantes.html", {"miFormulario":miFormulario})


def entregables(request):
      if request.method == 'POST':
            miFormulario = EntregablesFormulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  entregable = Entregable (nombre=informacion['nombre'], fechaDeEntrega=informacion['fechaDeEntrega'],
                  entregado=informacion['entregado']) 
                  entregable.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= EntregablesFormulario #Formulario vacio para construir el html
      return render(request, "AppCoder/entregables.html", {"miFormulario":miFormulario})

def cursos(request):
      if request.method == 'POST':
            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  curso = Curso (nombre=informacion['curso'], camada=informacion['camada']) 
                  curso.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= CursoFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/cursos.html", {"miFormulario":miFormulario})

def profesores(request):
      if request.method == 'POST':
            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                  email=informacion['email'], profesion=informacion['profesion']) 
                  profesor.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})

def buscar(request):
      if  request.GET["camada"]:
            #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            camada = request.GET['camada'] 
            cursos = Curso.objects.filter(camada__icontains=camada)
            return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})
      else:
            respuesta = "No enviaste datos"
      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

def leerProfesores(request):
      profesores = Profesor.objects.all() #trae todos los profesores
      contexto= {"profesores":profesores} 
      return render(request, "AppCoder/leerProfesores.html",contexto)

def leerCursos(request):
      curso = Curso.objects.all() #trae todos los cursos
      contexto= {"Curso":curso} 
      return render(request, "AppCoder/leerCursos.html",contexto)

def eliminarProfesor(request, profesor_nombre):
      profesor = Profesor.objects.get(nombre=profesor_nombre)
      profesor.delete()
      # vuelvo al menú
      profesores = Profesor.objects.all()  # trae todos los profesores
      contexto = {"profesores": profesores}
      return render(request, "AppCoder/leerProfesores.html", contexto)

def eliminarCursos(request, curso_nombre):
      curso = Curso.objects.get(nombre=curso_nombre)
      curso.delete()
      # vuelvo al menú
      curso = Curso.objects.all()  # trae todos los cursos
      contexto = {"cursos": curso}
      return render(request, "AppCoder/leerCursos.html", contexto)

def editarCursos(request, curso_nombre):
    # Recibe el nombre del profesor que vamos a modificar
    curso = Curso.objects.get(nombre=curso_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            curso.nombre = informacion['nombre']
            curso.camada = informacion['camada']

            curso.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = CursoFormulario(initial={'nombre': curso.nombre, 'camada': curso.camada})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarCursos.html", {"miFormulario": miFormulario, "curso_nombre": curso_nombre})

def editarProfesor(request, profesor_nombre):
    # Recibe el nombre del profesor que vamos a modificar
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']

            profesor.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido,
                                                   'email': profesor.email, 'profesion': profesor.profesion})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarProfesor.html", {"miFormulario": miFormulario, "profesor_nombre": profesor_nombre})

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CursoList(ListView):

    model = Curso
    template_name = "AppCoder/cursos_list.html"

class EstudianteList(ListView):

    model = Estudiante
    template_name = "AppCoder/estudiante_list.html"

class EntregableList(ListView):

    model = Entregable
    template_name = "AppCoder/entregable_list.html"

class CursoDetalle(DetailView):

    model = Curso
    template_name = "AppCoder/curso_detalle.html"

class EntregableDetalle(DetailView):

    model = Entregable
    template_name = "AppCoder/entregable_detalle.html"


class EstudianteDetalle(DetailView):

    model = Estudiante
    template_name = "AppCoder/estudiante_detalle.html"

class CursoCreacion(CreateView):

    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'camada']

class EntregableCreacion(CreateView):

    model = Entregable
    success_url = "/AppCoder/entregable/list"
    fields = ['nombre', 'fechaDeEntrega', 'entregado']

class EstudianteCreacion(CreateView):

    model = Estudiante
    success_url = "/AppCoder/estudiante/list"
    fields = ['nombre', 'apellido']

class CursoUpdate(UpdateView):

    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'camada']

class EntregableUpdate(UpdateView):

    model = Entregable
    success_url = "/AppCoder/entregable/list"
    fields = ['nombre', 'fechaDeEntrega', 'entregado']


class EstudianteUpdate(UpdateView):

    model = Estudiante
    success_url = "/AppCoder/estudiante/list"
    fields = ['nombre', 'apellido']

class CursoDelete(DeleteView):

    model = Curso
    success_url = "/AppCoder/curso/list"

class EntregableDelete(DeleteView):

    model = Entregable
    success_url = "/AppCoder/entregable/list"


class EstudianteDelete(DeleteView):

    model = Estudiante
    success_url = "/AppCoder/estudiante/list"
    
# Vista de login
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})

def register(request):

      if request.method == 'POST':

            form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})

@login_required
def inicio(request):

    return render(request, "AppCoder/inicio.html")

@login_required
def AcercaDeMi(request):

    return render(request, "AppCoder/AcercaDeMi.html")


# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

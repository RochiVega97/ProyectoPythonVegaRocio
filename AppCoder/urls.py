from django.urls import path

from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('AcercaDeMi', views.AcercaDeMi, name="AcercaDeMi"),
    path('LeerMas', views.LeerMas, name="LeerMas"),
    path('Contacto', views.Contacto, name="Contacto"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
    path('leerProfesores', views.leerProfesores, name = "LeerProfesores"),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
    
    path('leerCursos', views.leerCursos, name = "LeerCursos"),
    path('eliminarCursos/<cursos_nombre>/', views.eliminarCursos, name="EliminarCursos"),
    path('editarCursos/<cursos_nombre>/', views.editarCursos, name="EditarCursos"),
    
    path('curso/list', views.CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),

    path('estudiante/list', views.EstudianteList.as_view(), name='ListEstudiantes'),
    path(r'^(?P<pk>\d+)$', views.EstudianteDetalle.as_view(), name='DetailEstudiantes'),
    path(r'^nuevo$', views.EstudianteCreacion.as_view(), name='NewEstudiantes'),
    path(r'^editar/(?P<pk>\d+)$', views.EstudianteUpdate.as_view(), name='EditEstudiantes'),
    path(r'^borrar/(?P<pk>\d+)$', views.EstudianteDelete.as_view(), name='DeleteEstudiantes'),


    path('entregable/list', views.EntregableList.as_view(), name='ListEntregables'),
    path(r'^(?P<pk>\d+)$', views.EntregableDetalle.as_view(), name='DetailEntregables'),
    path(r'^nuevo$', views.EntregableCreacion.as_view(), name='NewEntregable'),
    path(r'^editar/(?P<pk>\d+)$', views.EntregableUpdate.as_view(), name='EditEntregables'),
    path(r'^borrar/(?P<pk>\d+)$', views.EntregableDelete.as_view(), name='DeleteEntregables'),


    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),






]

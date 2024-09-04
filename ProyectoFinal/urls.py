from ProyectoFinal import views
from django.urls import path
from ProyectoFinal import views_clases

urlpatterns = [
    path('inicio/', views.inicio, name = 'inicio'),
    path('cursos', views.cursos, name = 'cursos'),   
    path('estudiantes', views.estudiantes, name = 'estudiantes'),
    path('busqueda', views.busqueda, name = 'busqueda'),
    path('buscar/', views.buscar),
    path('profesores', views.profesores, name = 'profesores'),

   
]

urls_vistas_clases = [
    path('profesor/lista/', views_clases.ProfesoresListView.as_view(), name='List'),
    path('profesor/detalle/<int:pk>/', views_clases.ProfesoresDetailView.as_view(), name='Detail'),
    path('profesor/nuevo/', views_clases.ProfesoresCreateView.as_view(), name='New'),
    path('profesor/editar/<int:pk>', views_clases.ProfesoresUpdateView.as_view(), name='Edit'),
    path('profesor/eliminar/<int:pk>', views_clases.ProfesoresDeleteView.as_view(), name='Delete'),

    path('curso/lista/', views_clases.CursoListView.as_view(), name='CursoList'),
    path('curso/detalle/<int:pk>/', views_clases.CursoDetailView.as_view(), name='CursoDetail'),
    path('curso/nuevo/', views_clases.CursoCreateView.as_view(), name='CursoNew'),
    path('curso/editar/<int:pk>', views_clases.CursoUpdateView.as_view(), name='CursoEdit'),
    path('curso/eliminar/<int:pk>', views_clases.CursoDeleteView.as_view(), name='CursoDelete'),

    
    path('estudiante/lista/', views_clases.EstudianteListView.as_view(), name='EstudianteList'),
    path('estudiante/detalle/<int:pk>/', views_clases.EstudianteDetailView.as_view(), name='EstudianteDetail'),
    path('estudiante/nuevo/', views_clases.EstudianteCreateView.as_view(), name='EstudianteNew'),
    path('estudiante/editar/<int:pk>', views_clases.EstudianteUpdateView.as_view(), name='EstudianteEdit'),
    path('estudiante/eliminar/<int:pk>', views_clases.EstudianteDeleteView.as_view(), name='EstudianteDelete')
]

urlpatterns += urls_vistas_clases
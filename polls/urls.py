from django.urls import path
from polls import views

urlpatterns = [
    path('students/',views.home,name="Home"),
    path('save/',views.Login,name="save"),
    path('students/Update/<int:id>/',views.update,name='update'),
    # path('students/Student-Dalete/<int:id>', views.Delete, name='Student-Dalete'),
    path('students/Student-Delete/<int:id>/', views.Delete, name='Student-Delete'),
    # path('students/Student-Delete/', views.Delete, name='Student-Delete'),
]

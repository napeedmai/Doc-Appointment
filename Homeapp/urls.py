from django.urls import path
from . import views

urlpatterns =[ 
    path("",views.index,name="home"),
    path("index",views.index,name="index"),
    path("about",views.about,name="about"),               
    path("appointment",views.appointment,name="appointment"),   
    path("bookAppointment",views.book_appointment,name="Appointment"),
    path("patientIndex",views.patient,name="Patient"),
    path("DocApp",views.doctor,name="doctor"),
    path("delete",views.delete,name="delete")   

 ]


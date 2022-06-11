from django.urls import path
from .import views

urlpatterns=[

    path("",views.index , name="anasayfa"),
    path("sayilarimiz",views.sayilarimiz , name="sayilarimiz"),
    path("yazarlarimiz",views.yazarlarimiz , name="yazarlarimiz"),
    path("yazigönder",views.yazigönder , name="yazigönder"),
    path("sayilarimiz/<int:id>" , views.icerik , name="icerik")
]
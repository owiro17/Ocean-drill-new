from . import views
from django.urls import path
urlpatterns = [
    path('',views.index,name="index"),
    path('about-us/',views.aboutUs,name="about-us"),
    path('what-we-do/',views.whatWeDo,name="what-we-do"),
    path('our-work/',views.ourWork,name="our-work"),
    path('faq/',views.faq,name="faq"),
    path('contact-us/',views.contactUs,name="contact-us"),
]

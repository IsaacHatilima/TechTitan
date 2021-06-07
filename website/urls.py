from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us/', views.about_us, name="about-us"),
    path('why_us/', views.why_us, name="why_us"),
    path('out_team/', views.out_team, name="out_team"),
    path('it_solutions/', views.it_solutions, name="it_solutions"),
    path('it_solutions/it_management_services', views.it_management_services, name="it_management_services"),
    path('it_solutions/cyber_security_services', views.cyber_security_services, name="cyber_security_services"),
    path('it_solutions/software_dev_services', views.software_dev_services, name="software_dev_services"),
    path('it_solutions/networking_and_cloud_services', views.networking_services, name="networking_and_cloud_services"),
    path('it_solutions/it_consultations', views.consulting_services, name="it_consultations"),
    path('it_solutions/data_backup_and_recovery', views.backup_services, name="data_backup_and_recovery"),
    path('it_solutions/email_hosting', views.email_hosting, name="email_hosting"),
    path('it_solutions/web_hosting', views.web_hosting, name="web_hosting"),
    path('stories', views.blogging, name="stories"),
    path('contact_us', views.contact, name="contact_us"),
    path('find_out', views.find_out, name="find_out"),
    path('request_quote', views.get_quote, name="request_quote"),
]


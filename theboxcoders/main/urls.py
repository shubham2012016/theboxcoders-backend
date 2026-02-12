from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('Web-Development-services', views.web_devlopment, name='web_devlopment'),
    path('python-services', views.python_service, name='python_services'),
    path('ai-integration-services', views.ai_intergration_services, name='ai_intergration_services'),
    path('instagram-automation-services', views.instagram_automation, name='instagram_automation'),
    path('facebook-automation-services', views.facebook_automation, name='facebook_automation'),
    path('whatsapp-automation-services', views.whatsapp_automation, name='whatsapp_automation'),
    path('tally-automation-services', views.tally_automation, name='tally_automation'),

    path('thank-you', views.thank_you, name='thank_you'),
    path('book-consultation', views.book_consultation, name='book_consultation'),
    # path('web-development-services', views.web_devlopment, name='web_dev_project_inquiry'),
    # path('python-services', views.python_service, name='python_project_inquiry'),
]
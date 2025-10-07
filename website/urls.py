from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('join/', views.join, name='join'),
    path('help/', views.help_center, name='help'),
    path('premium/', views.premium, name='premium'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('safety/', views.safety, name='safety'),
    path('trust/', views.trust, name='trust'),
    path('success-stories/', views.success_stories, name='success_stories'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('discover/', views.discover, name='discover'),
    path('events/', views.events, name='events'),
    path('faq/', views.faq, name='faq'),
]

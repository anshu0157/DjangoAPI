from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import include, path
from . import views



urlpatterns = [
    path('advisor/', views.profiles.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)


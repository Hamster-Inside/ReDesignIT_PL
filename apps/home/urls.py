from django.urls import path
from .views import HomeView, StatisticView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('statistic', StatisticView.as_view(), name='statistic')
]

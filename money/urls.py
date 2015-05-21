from django.conf.urls import url
from .views import LatestExpensesListView

urlpatterns = [
    url(r'^latest_expenses/$', LatestExpensesListView.as_view(), name='users_logout'),
]

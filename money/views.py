from django.views.generic.list import ListView
from .models import Expense


class LatestExpensesListView(ListView):
    model = Expense

    def get_context_data(self, **kwargs):
        latest_expenses = self.request.user.expenses.all()[:5]
        return {"latest_expenses": latest_expenses}

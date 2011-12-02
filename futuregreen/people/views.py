# people/views.py

from django.views.generic import ListView, DetailView

from futuregreen.people.models import *

class EmployeeDetailView(DetailView):
    model = Employee

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['employee_list'] = Employee._default_manager.filter(public=True)\
                                                            .order_by('employee_type__level')
        return context

class EmployeeListView(ListView):
    model = Employee
from django.views.generic import TemplateView
from api.models import Person
from django.contrib.auth.models import User

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['person_list'] = Person.objects.filter(is_home=True)
        return context
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from medicamento.models import Medicamento


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

def ver_home(request):
    print('entro aca')
    medicamentos = Medicamento.objects.all()
    query = request.GET.get('q')
    print(query)
    if query and query != '':
        medicamentos = Medicamento.objects.filter(Q(total__icontains=query) | Q(cliente__cliente_id__icontains=query))
    else:
        medicamentos = Medicamento.objects.all()
    data = {}
    print(medicamentos)
    data['medicamentos'] = medicamentos
    return render(request, "home.html", {"data": data})




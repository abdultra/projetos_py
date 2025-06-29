from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Paciente
from .forms import PacienteForm
from .utils import listar_objetos, detalhar_objeto, criar_objeto, editar_objeto, excluir_objeto

def index(request):
    return render(request, 'pacientes/index.html')

# Funções para o modelo Paciente

def paciente_list(request):
    return listar_objetos(request, Paciente, 'app_lab/paciente/paciente_list.html', 'pacientes')


def paciente_detail(request, pk):
    return detalhar_objeto(request, pk, Paciente, 'app_lab/paciente/paciente_detail.html', 'paciente')


def paciente_create(request):
    return criar_objeto(request, PacienteForm, Paciente, 'app_lab/paciente/paciente_form.html', 'paciente_list')

def paciente_edit(request, pk):
    return editar_objeto(request, pk, PacienteForm, Paciente, 'app_lab/paciente/paciente_form.html', 'paciente_list')

def paciente_delete(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente excluído com sucesso!')
        return redirect('paciente_list')
    return render(request, 'app_lab/paciente/paciente_confirm_delete.html', {'object': paciente, 'model_name': 'Paciente', 'cancel_url': 'paciente_list'})

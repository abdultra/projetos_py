from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

def listar_objetos(request, ModelClass, template_name, context_name='objetos'):
	objetos = ModelClass.objects.all()
	context = {context_name: objetos}
	return render(request, template_name, context)

def detalhar_objeto(request, ModelClass, pk, template_name, context_name='objeto'):
	objeto = get_object_or_404(ModelClass, pk=pk)
	context = {context_name: objeto}
	return render(request, template_name, context)

def criar_objeto(request, FormClass, template_name, redirect_url):
	if request.method == 'POST':
		form = FormClass(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, "Registro criado com sucesso.")
			return redirect(redirect_url)
	else:
		form = FormClass()
	return render(request, template_name, {'form': form})

def editar_objeto(request, ModelClass, FormClass, pk, template_name, redirect_url):
	objeto = get_object_or_404(ModelClass, pk=pk)
	if request.method == 'POST':
		form = FormClass(request.POST, request.FILES, instance=objeto)
		if form.is_valid():
			form.save()
			messages.success(request, "Registro atualizado com sucesso.")
			return redirect(redirect_url)
	else:
		form = FormClass(instance=objeto)
	return render(request, template_name, {'form': form})

def excluir_objeto(request, ModelClass, pk, redirect_url, confirm_template):
	objeto = get_object_or_404(ModelClass, pk=pk)
	if request.method == 'POST':
		objeto.delete()
		messages.success(request, "Registro excluído com sucesso.")
		return redirect(redirect_url)
	return render(request, confirm_template, {'objeto': objeto})

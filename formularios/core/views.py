from django.shortcuts import render
from django.forms import formset_factory
import json
import ast

from formularios.core.forms import UploadForm, OptionsForm
from formularios.core.models import xls_to_dict


def home(request):
    if request.method == 'POST' and 'btn_upload' in request.POST:
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            context = xls_to_dict(request.FILES['upload'])
            request.session['actions'] = str(context['acoes'])
            OptionsFormSet = formset_factory(OptionsForm, extra=len(context['acoes']))
            formset = OptionsFormSet()
            for acao, form in zip(context['acoes'], formset):
                acao['indicacao'] = form
            return render(request, 'edit.html', context=context)

    if request.method == 'POST' and 'btn_print' in request.POST:
        context = request.session.get('actions', '')
        acoes = ast.literal_eval(context)
        
        return render(request, 'print.html', {'acoes':acoes})
        
    else:
        form = UploadForm()
        return render(request, 'index.html', {'form': form})

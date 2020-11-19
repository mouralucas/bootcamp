from django.shortcuts import render

# Create your views here.
from django.views import View


class Dash(View):
    def get(self, *args, **kwargs):
        """
        Criar uma requisição que retorne as informações da tabela [x] via contexto....
        :param args:
        :param kwargs:
        :return:
        """
        context = {
            'valores_1': '',
            'valores_2': '',
            'valores_3': '',
            'valores_4': '',
            'valores_5': '',
            'valores_6': '',
            'valores_7': '',
            'valores_8': '',
            'valores_9': '',
            'valores_10': '',
            'valores_11': '',
        }
        return render(request=self.request, template_name='dash.html', context=context)


"""
Criar um class based views que retorna o template uma lista com as informações da tabela [x]
ao clicar no botão contida no template da view Dash e também criar sua URL
"""
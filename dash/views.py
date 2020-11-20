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
            'tabela_venda': None,
            'tabela_venda_maior_100': None,
            'tabela_venda_maior_100_qtd': None,
            'tabela_venda_maior_100_par_impar': None,
            'servicos_nome_maior_5': None,
            'dia': None,
        }
        return render(request=self.request, template_name='exercicio_um.html', context=context)


"""
Criar um class based views que retorna o template uma lista que cada posição seja uma letra do alfabeto e
uma segunda lista de 15 posições com numeros aleatórios, use a função for para gerar a lista aleatória
(dica: pesquise a função Random do python para isso) 
Cria a URL 'listas/' no arquivo dash/urls para que a função seja executado quando a URL for digitada no navegador

Use a função Dash acima como referência da montagem da view. O 'context' deve conter duas chaves: 'alfabeto' para 
envia a lista com o alfabeto e 'lista_aleatoria' para enviar a lista de numeros aleatórios

A view deve chamar o template 'exercicio_dois.html'.
"""
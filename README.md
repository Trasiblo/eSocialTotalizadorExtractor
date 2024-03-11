# eSocialTotalizadorExtractor

Extrair dados de arquivos XML baixados do ambiente web do eSocial para uma planilha organizada e de fácil consulta.

- ler e **extrair** dados dos **arquivos XML** dos eventos S-5001 (Informações das Contribuições Sociais por Trabalhador);
- ler e **extrair** dados dos **arquivos XML** dos eventos S-3000 (Exclusão de Eventos);
- **Gerar** um **arquivo de planilha (.xlsx)** com **um relatório detalhado** dos eventos válidos..


## Uso básico
### 1. Intalação do Python

Siga o passo a passo, [Instalando o Python 3 no Windows](https://python.org.br/instalacao-windows/) - *visitado em 11/03/2024 às 16:02*

### 2. Obter os arquivos xmls no eSocial

Siga o passo a passo, [eSocial Download: para facilitar a vida do empregador](https://www.gov.br/esocial/pt-br/noticias/esocial-download-para-facilitar-a-vida-do-empregador) - *visitado em 11/03/2024 às 15:20*

### 3. Crie uma pasta
![](https://github.com/Trasiblo/eSocialTotalizadorExtractor/raw/main/gifs/criar_pasta.gif)


### 4. Criando e Ativando um ambiente virtual com python

Cria o ambiente virtual
```
python -m venv venv
```

Ativa o ambiente virutal recem criado
```
venv\Scripts\activate
```

![](https://github.com/Trasiblo/eSocialTotalizadorExtractor/raw/main/gifs/criar_ambiente_virtual.gif)

### 5. Instalação da biblioteca eSocialTotalizadorExtractor

Diretamente do repositório:

```
pip install https://github.com/Trasiblo/eSocialTotalizadorExtractor/raw/main/distt/esocialtotalizadorextractor-0.1.0-py3-none-any.whl
```
ou
```
pip install https://github.com/Trasiblo/eSocialTotalizadorExtractor/raw/main/distt/esocialtotalizadorextractor-0.1.0.tar.gz
```

![](https://github.com/Trasiblo/eSocialTotalizadorExtractor/raw/main/gifs/instalar.gif)

### 6. Criando dois arquivos exemplos 

![](https://github.com/Trasiblo/eSocialTotalizadorExtractor/raw/main/gifs/criar_arquivos.gif)


### 7. Código para ler os arquivos baixados do eSocial (ler.py)

```python
from esocialtotalizadorextractor.lerTotalizador import *

diretorio = '202402' #pasta onde os arquivos xmls foram descompactados

ler = lerXml(diretorio)

ler.s5001() 
```

Cole o código no arquivo ler.py

![](https://github.com/Trasiblo/eSocialTotalizadorExtractor/raw/main/gifs/colar_ler.gif)


### 8. Código para gerar o arquivo Excel com os dados Lidos (relatorio.py)

```python
from esocialtotalizadorextractor.banco import *
import pandas as pd

valor = relatorio.get_valor()
df1 = pd.DataFrame(valor)

valor = relatorio.get_valor_analitico()
df2 = pd.DataFrame(valor)

arqExcel = pd.ExcelWriter('teste.xlsx') #nome do arquivo que sera gerado

df1.to_excel(arqExcel, index=False, float_format='%.2f', sheet_name='Resumo')
df2.to_excel(arqExcel, index=False, float_format='%.2f', sheet_name='Analitica')

arqExcel.close()
```

Cole o código no arquivo relatorio.py

![](https://github.com/Trasiblo/eSocialTotalizadorExtractor/raw/main/gifs/colar_relatorio.gif)

### 9. Descompactando zip dos xmls do eSocial

![](https://github.com/Trasiblo/eSocialTotalizadorExtractor/raw/main/gifs/xmls_esocial.gif)

### 10. Executando os códigos e abrindo o arquivo Excel gerado, "teste.xlsx".

![](https://github.com/Trasiblo/eSocialTotalizadorExtractor/raw/main/gifs/executar_codigos.gif)



## Erros 

Verifique se as Extensões de nomes de arquivos estão ativadas no seu sistema.

![](https://github.com/Trasiblo/eSocialTotalizadorExtractor/raw/main/gifs/criar_exibir_extensoes.gif)


## Apoie este projeto!
Este projeto é gratuito e de código aberto, mas seu desenvolvimento depende do apoio da comunidade. Se você acha este projeto útil, considere fazer uma doação para ajudar a manter o desenvolvimento e a melhorar a experiência para todos.

> chave pix (e-mail): trasiblo@hotmail.com
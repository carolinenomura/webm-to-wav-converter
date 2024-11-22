# Conversor de Áudios WebM para WAV

Este script em Python permite converter arquivos de áudio no formato .webm de uma pasta selecionada para o formato .wav, salvando os arquivos convertidos em uma pasta de saída especificada. Ele utiliza uma janela de diálogo para seleção de pastas com tkinter e a biblioteca ffmpeg para realizar a conversão dos áudios.

## Recursos

- Seleção de pastas de entrada e saída por meio de uma janela de diálogo.
- Conversão em lote de todos os arquivos .webm da pasta de entrada.
- Inclui uma cópia local do ffmpeg para simplificar o uso.

## Requisitos
- Python 3
- Adicionar Python à variável PATH

## Instalação
### 1. Baixe este Repositório

Baixe ou clone o repositório para sua máquina local.

```python
git clone <url-do-repositorio>
```
Navegue até a pasta webm-to-wav-converter criada e abra o terminal dentro dela.

### 2. Configure o Ambiente Python

Este projeto utiliza pipenv para gerenciar dependências.
Instale o pipenv (caso ainda não tenha).

```python
pip install pipenv
```

Instale as dependências.

```python
pipenv install
```

### 3. Executando o Script

Execute o script diretamente no ambiente do pipenv.

```python
pipenv run python converter.py
```

## Instruções de Uso

### Ao executar o script, você será solicitado a selecionar:
- Uma pasta de entrada contendo arquivos .webm.
- Uma pasta de saída onde os arquivos .wav serão salvos.

### O script irá:

1. Examinar a pasta de entrada em busca de arquivos .webm.
2. Converter cada arquivo para .wav.
3. Salvar os arquivos convertidos na pasta de saída com os nomes originais.

Quando a conversão for concluída, uma mensagem de sucesso será exibida no terminal.

# Transcrição de Áudio com Whisper e Ollama

## Descrição

Este projeto tem como objetivo realizar a transcrição de arquivos de áudio utilizando o Whisper e gerar resumos com os principais pontos-chave do conteúdo utilizando o Ollama.

## Tecnologias utilizadas

- Python
- Whisper
- Ollama
- FFmpeg

## Pré-requisitos

- Python 3.11 recomendado.
- FFmpeg instalado.
- Ollama instalado.

## Instalação

Instale as dependências do projeto:

```bash
python -m pip install -r requirements.txt
```

Baixe o modelo utilizado pelo Ollama:

```bash
ollama pull llama3.2:3b
```

## Execução

Com o Ollama em execução, utilize o comando:

```bash
python main.py
```

Informe o caminho do arquivo de áudio no formato MP3 ou WAV.

## Exemplo de uso

Ao executar o programa, informe o arquivo `teste-ia-pt-br.mp3`.

O programa realizará a transcrição do áudio e apresentará no terminal o texto transcrito, um resumo e os principais pontos-chave.

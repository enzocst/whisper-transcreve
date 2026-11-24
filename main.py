
import whisper
import ollama
import os

# Recebe o arquivo de áudio
audio = input("Informe o caminho do áudio: ").strip().strip('"')

# Verifica se o arquivo existe
if not os.path.isfile(audio):
    print("Arquivo não encontrado.")
    exit()

# Verifica o formato do áudio
if not audio.lower().endswith((".mp3", ".wav")):
    print("Formato inválido. Utilize MP3 ou WAV.")
    exit()

# Carrega o modelo Whisper
print("Carregando modelo Whisper...")
model = whisper.load_model("small")

# Transcreve o áudio
print("Transcrevendo áudio...")
result = model.transcribe(audio, language="pt", fp16=False)
texto = result["text"].strip()

# Exibe a transcrição
print("\n--- TRANSCRIÇÃO ---")
print(texto)

# Gera o resumo utilizando o Ollama
print("\nGerando resumo...")

resposta = ollama.chat(
    model="llama3.2:1b",
    messages=[
        {
            "role": "user",
            "content": f"Resuma o texto abaixo e liste os principais pontos-chave em português, sem inventar informações:\n\n{texto}"
        }
    ]
)

# Exibe o resumo e os pontos-chave
print("\n--- RESUMO E PONTOS-CHAVE ---")
print(resposta["message"]["content"])

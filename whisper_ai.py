import whisper

print(whisper._MODELS["small"])
model = whisper.load_model("small")

model = whisper.load_model(
    "small",
    download_root=r"C:\Users\Cassterss\Documents\Python\code\Agent_Tyler\models\whisper"
)
def speak_to_text(root):
    resul = model.transcribe(
        root,
        language="ru",
        initial_prompt='Команды голосового ассистента: открой браузер, закрой браузер, включи VPN, выключи VPN, открой Telegram, открой YouTube.'
        )
    return resul['text'].strip()
    

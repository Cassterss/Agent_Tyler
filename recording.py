import sounddevice as sd
import soundfile as sf
import os
SAMPLE_RATE = 16000
DURATION = 4 

def record_command():

    print("🎙 Говори команду...")

    audio = sd.rec(
        int(SAMPLE_RATE * DURATION),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    sf.write(
        r"C:\Users\Cassterss\Documents\Python\code\Agent_Tyler\files\command.wav",
        audio,
        SAMPLE_RATE
    )

    print("✅ command.wav записан")

    return r"C:\Users\Cassterss\Documents\Python\code\Agent_Tyler\files\command.wav"

def deleted(root):
    os.remove(root)
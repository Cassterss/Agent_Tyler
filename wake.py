import torch
import torch.nn as nn
import soundfile as sf
import torchaudio as ta 
import torch.nn.functional as F
import sounddevice as sd

class Tyler_Ai(nn.Module):
    def __init__(self):
        super(Tyler_Ai, self).__init__()
        self.l1 = nn.Conv2d(1, 64, kernel_size=3, padding=1)
        self.l2 = nn.Conv2d(64, 32, kernel_size=3, padding=1)
        self.l3 = nn.Conv2d(32, 16, kernel_size=3, padding=1)
        self.flatten = nn.Flatten()
        self.l4 = nn.Linear(16*8*18, 1)
        self.max = nn.MaxPool2d(2)
        self.relu = nn.ReLU()
        

    def forward(self, x):
        x = self.l1(x)
        x = self.relu(x)
        x = self.max(x) # 32 75
        x = self.l2(x)
        x = self.relu(x)
        x = self.max(x) # 16 37
        x = self.l3(x)
        x = self.relu(x)
        x = self.max(x) # 8 18
        x = self.flatten(x)
        x = self.l4(x)
        return x


mel = ta.transforms.MelSpectrogram(
    sample_rate=16000,
    n_fft=400,
    hop_length=160,
    n_mels=64
)
db = ta.transforms.AmplitudeToDB()
def normalize_volume(audio):

    rms = torch.sqrt(torch.mean(audio ** 2) + 1e-8)

    gain = 0.05 / rms

    gain = torch.clamp(gain, min=0.25, max=8.0)

    audio = audio * gain

    audio = torch.clamp(audio, -1.0, 1.0)

    return audio

sigmoid = nn.Sigmoid()
model = Tyler_Ai()
model.eval()
model.load_state_dict(torch.load(r'C:\Users\Cassterss\Documents\Python\code\Agent_Tyler\models\Tyler_AI.pth'))

SAMPLE_RATE = 16000
STEP = 4800         
WINDOW = 24000       
THRESHOLD = 0.76



def wake_up():
    print('+')
    buffer = torch.empty(0, dtype=torch.float32)
    with sd.InputStream(
    samplerate=SAMPLE_RATE,
    blocksize=STEP,
    dtype="float32",
    channels=1,
    ) as stream:

        while True:

            audio, rate = stream.read(STEP)

            audio = torch.from_numpy(audio[:, 0].copy())

            buffer = torch.cat((buffer, audio))


            if buffer.numel() < WINDOW:
                continue


            buffer = buffer[-WINDOW:]

            normalized_buffer = normalize_volume(buffer)


            x = mel(normalized_buffer)
            x = db(x)
            x = x.unsqueeze(0).unsqueeze(0)

            with torch.no_grad():
                logit = model(x)
                probability = torch.sigmoid(logit).item()

            if probability > THRESHOLD:
                return True
                
            











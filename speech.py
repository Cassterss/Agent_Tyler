import torch
import torch.nn as nn
from transformers import AutoTokenizer, PreTrainedTokenizerBase

transform: PreTrainedTokenizerBase = AutoTokenizer.from_pretrained(
    r"C:\Users\Cassterss\Documents\Python\code\Agent_Tyler\rubert_tokenizer",
    local_files_only=True
)

class Module(nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = nn.Embedding(
            num_embeddings=(len(transform)),
            embedding_dim=32
        )
        self.attention = nn.Linear(32,1)
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(32,64)
        self.l3 = nn.Linear(64,16)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.l1(x)
        score = self.attention(x)
        weight = self.softmax(score)
        x = (x*weight).sum(dim=1)
        x = self.l2(x)
        x = self.relu(x)
        x = self.l3(x)
        return x

model = Module()
model.load_state_dict(torch.load(r'C:\Users\Cassterss\Documents\Python\code\Agent_Tyler\models\Fast_Ai.pth'))
model.eval()
softmax = nn.Softmax()

def chose_things(text):
    with torch.no_grad():
        text_tensor_encode = transform(
            text,
            padding='max_length',
            max_length=32,
            return_tensors='pt'
        )
        text_tensor_encode = text_tensor_encode['input_ids']
        y = model(text_tensor_encode)
        y = softmax(y)
        y = torch.argmax(y)
        return y.item()
    


import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import os

base_dir = "model/"
model_path_local = base_dir + "ru_gpt2_large"
tokenizer_path_local = base_dir + "gpt2_tokenizer"
model_path_hub = "sberbank-ai/rugpt2large"

# model is huge, so use cuda if possible:
if torch.cuda.is_available():
    device = 'cuda'
else:
    device = 'cpu'

# make dir for model and tokenizer storing:
if not os.path.isdir(base_dir):
    os.mkdir(base_dir)

# load model and tokenizer:
if os.path.isdir(model_path_local):
    print("model is already saved, so load it locally from disk...")
    ru_gpt_model = GPT2LMHeadModel.from_pretrained(model_path_local)
else:
    print("load model from hub...")
    ru_gpt_model = GPT2LMHeadModel.from_pretrained(model_path_hub)
    ru_gpt_model.save_pretrained(model_path_local)
print("model is successfully loaded")

if os.path.isdir(tokenizer_path_local):
    print("tokenizer is already saved, so load it locally from disk...")
    ru_gpt_tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path_local)
else:
    print("load tokenizer from hub...")
    ru_gpt_tokenizer = GPT2Tokenizer.from_pretrained(model_path_hub)
    ru_gpt_tokenizer.save_pretrained(tokenizer_path_local)
print("tokenizer is successfully loaded")

ru_gpt_model.to(device)


class ModelWrapper(object):
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer

    def generate(self, text, do_sample=True, max_length=50,
                 repetition_penalty=5.0, top_k=5, top_p=0.95,
                 temperature=1, num_beams=5, no_repeat_ngram_size=3
                 ):
        input_ids = self.tokenizer.encode(text, return_tensors="pt").to(device)
        out = self.model.generate(
            input_ids,
            max_length=max_length,
            repetition_penalty=repetition_penalty,
            do_sample=do_sample,
            top_k=top_k, top_p=top_p, temperature=temperature,
            num_beams=num_beams, no_repeat_ngram_size=no_repeat_ngram_size
        )
        return list(map(self.tokenizer.decode, out))[0]  # decode tokens to strings


model_wrapper = ModelWrapper(ru_gpt_model, ru_gpt_tokenizer)

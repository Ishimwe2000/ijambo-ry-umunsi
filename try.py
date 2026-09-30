from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Kinyarwanda -> English translation model hosted on the Hugging Face Hub
MODEL_NAME = "Helsinki-NLP/opus-mt-rw-en"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

text = "Muraho! Amakuru yawe?"

# 1. Text -> token IDs (PyTorch tensors)
inputs = tokenizer(text, return_tensors="pt")

# 2. Model generates English token IDs
generated = model.generate(**inputs)

# 3. Token IDs -> text
output = tokenizer.batch_decode(generated, skip_special_tokens=True)
print(output)

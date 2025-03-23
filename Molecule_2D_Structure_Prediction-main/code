import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, AdamW
from rdkit import Chem

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

tokenizer.pad_token = tokenizer.eos_token 

smiles_data = [
    "CCO",  # Ethanol
    "CCN(CC)CC",  # Triethylamine
    "C1=CC=CC=C1",  # Benzene
    # Add more SMILES strings
]

inputs = tokenizer(smiles_data, return_tensors="pt", padding=True, truncation=True)

optimizer = AdamW(model.parameters(), lr=5e-5)
model.train()

for epoch in range(10):  
    outputs = model(**inputs, labels=inputs["input_ids"])
    loss = outputs.loss
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    print(f"Epoch {epoch + 1}, Loss: {loss.item()}")

model.save_pretrained("molgpt_finetuned")
tokenizer.save_pretrained("molgpt_finetuned")

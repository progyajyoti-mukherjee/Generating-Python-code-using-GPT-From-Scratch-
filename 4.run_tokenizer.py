from tokenizers import ByteLevelBPETokenizer
from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer

TRAIN_BASE = True

if TRAIN_BASE:
    paths = ["python_code_text_data.txt"]

    tokenizer = ByteLevelBPETokenizer()

    tokenizer.train(files=paths, vocab_size=52_000, min_frequency=2, special_tokens=[
        "<s>",
        "<pad>",
        "</s>",
        "<unk>",
        "<mask>"
    ])

    # Save files to disk
    tokenizer.save_model("tokenizer")

# Ensure that the tokenizer is saved and can be loaded correctly
tokenizer = GPT2Tokenizer.from_pretrained('./tokenizer')

tokenizer.add_special_tokens({
    "eos_token": "</s>",
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>"
})

inp = "print('Hello world!')"
t = tokenizer.encode(inp)
print(t)

print(tokenizer.decode(t))

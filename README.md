# Hindi GPT (In Progress)

This project is an implementation of a GPT-style language model for Hindi text using PyTorch. It includes a custom tokenizer [Varnika](https://github.com/angkul07/Varnika), a transformer model, and basic text generation.

---

## Features

- Custom BPE tokenizer for Hindi
- Dataset creation with context windows and strides
- Transformer model with multi-head attention
- Text generation using autoregressive decoding

---

## Model Configuration

The model uses these settings:

```python
GPT_CONFIG_124M = {
    "vocab_size": 150000,
    "context_length": 256,
    "emb_dim": 384,
    "n_heads": 6,
    "n_layers": 6,
    "drop_rate": 0.1,
    "qkv_bias": False
}
```

---

## Requirements

You need the following Python libraries:

- torch
- tokenizers

Install them using pip:

```
pip install torch tokenizers
```

---

## Example Output

```
Input text: ऑनलाइन क्लास में हमेशा अपने पोस्चर
Output text: ऑनलाइन क्लास में हमेशा अपने पोस्चर को सही रखें और
```

---

## To Do
- [ ] Create interface (CLI or Web)
- [ ] Add support for multi-lingal training.
- [ ] Support for Architectures like Flash Attention.

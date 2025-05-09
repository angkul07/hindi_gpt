from tokenizers import Tokenizer

class HindiTokenizer:
    def __init__(self, model_path="/home/angkul/my_data/coding/agi/hindi_GPT/hindi_tokenizer.json"):
        self.tokenizer = Tokenizer.from_file(model_path)

    def encode(self, text):
        return self.tokenizer.encode(text).ids

    def decode(self, token_ids):
        return self.tokenizer.decode(token_ids)
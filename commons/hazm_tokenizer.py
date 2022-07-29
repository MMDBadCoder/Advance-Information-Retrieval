from hazm import WordTokenizer, Normalizer


class HazmTokenizer:
    def __init__(self):
        self.tokenizer = WordTokenizer()
        self.normalizer = Normalizer()

    def tokenize(self, text):
        text = self.normalizer.normalize(text)
        return self.tokenizer.tokenize(text)

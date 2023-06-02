import random
import pandas as pd


class Words:
    def __init__(self):
        self.current_word = None
        try:
            data = pd.read_csv("words_to_learn.csv")
        except pd.errors.EmptyDataError or FileNotFoundError:
            data = pd.read_csv("french_words.csv")
        finally:
            self.list_of_words = data.to_dict(orient="records")

        self.total = len(self.list_of_words)
        self.next_word()

    def next_word(self):
        word = random.choice(self.list_of_words)
        self.current_word = word

    def remove_current_word(self):
        self.list_of_words.remove(self.current_word)
        self.total = self.total - 1
        print(self.total)

    def save_words_to_learn(self):
        self.remove_current_word()
        data = pd.DataFrame.from_dict(self.list_of_words)
        data.to_csv("words_to_learn.csv", index=False)

    def __str__(self):
        return f"French: {self.current_word['French']} - English: {self.current_word['English']}"

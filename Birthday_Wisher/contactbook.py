import pandas as pd


class ContactBook:
    def __init__(self):
        try:
            data = pd.read_csv("birthdays.csv")
            self.contact_list = data.to_dict(orient="records")
        except pd.errors.EmptyDataError or FileNotFoundError:
            self.contact_list = []
            print("Error")

        self.total = len(self.contact_list)

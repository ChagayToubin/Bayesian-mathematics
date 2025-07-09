import pandas as pd
class loader:
    @staticmethod
    def load_file():
        return pd.read_csv("buy_computer_data.csv")

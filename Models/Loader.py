import pandas as pd
class loader:
    @staticmethod
    def load_file(name):
        return pd.read_csv(name)

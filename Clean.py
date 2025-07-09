class clean:
    @staticmethod
    def clean_file(file):
        return file.drop(columns=['id'])

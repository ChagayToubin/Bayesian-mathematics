import requests
import json

from Models.Manger import manger


class Answer:
    @staticmethod
    def answer():
        a=manger()

        value = json.dumps([1, 2, 3, 4, 5])  # ממיר לרשימה כ־JSON
        url = f"http://127.0.0.1:8000/@@@/{value}"

        response = requests.get(url)

        print(type(response.text))

Answer.answer()

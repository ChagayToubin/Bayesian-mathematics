from typing import Union
import json
from fastapi import FastAPI
from fastapi import FastAPI, Query
from typing import List


app = FastAPI()


@app.get("/@@@/{list_condtion}")
def check_items(list_condtion):
    print(type(list_condtion))
    print(list_condtion)
    data = json.loads(list_condtion)
    print(type(data))  # עכשיו list
    print(data)



    return list_condtion


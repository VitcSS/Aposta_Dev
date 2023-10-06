import requests
from typing import List, Dict

def get_federal(competition : str = 'latest')-> Dict:
    tags : str = ['loteria', 'concurso', 'data','local','dezenas']
    BASE_REQUEST : str = f"https://loteriascaixa-api.herokuapp.com/api/federal/{competition}"
    raw = requests.get(BASE_REQUEST).json()
    resumed : Dict = {}
    for k in tags:
        resumed[k] = raw[k]
    return resumed

def result(federal_result : Dict)->int:
    numbers : List = [int(i) for i in federal_result['dezenas']]
    total : int = str(sum(numbers))
    return int(total[int(len(total)/2)])


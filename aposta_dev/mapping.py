import json
from typing import Dict
def get_mapping(path : str = 'aposta_dev/map.json')->Dict:
    with open(path) as file:
        mapping : Dict = json.load(file)
    return mapping

def raffle_result(result: int, options_map : Dict = get_mapping()):
    options : Dict = options_map
    for k,v in options.items():
        if result <= int(k):
            return v


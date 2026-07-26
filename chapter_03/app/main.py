import json
from pathlib import Path
from typing import List,Dict

Data_file=Path(__file__).parent.parent/'data'/'products.json'


def load_product()->List[Dict]:
    if not Data_file.exists():
        return []
    with open(Data_file,'r',encoding='utf-8') as file:
        return json.load(file)

def get_all_products()->List[Dict]:
    return load_product()
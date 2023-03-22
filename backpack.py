from python_input.from_api import get_data

data = get_data()

for row in data:
    print(row)



from dataclasses import dataclass

@dataclass
class Item:
    id: int
    weight: float
    value: float


@dataclass
class Solution:
    items: list[Item]
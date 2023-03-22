import csv
import itertools
from dataclasses import dataclass

@dataclass
class AdventurerItem:
    id: int
    name: str
    value: float
    weight: float
    valueWeightRatio: float

class Backpack:
    def __init__(self, max_weight = 5) -> None:
        self.max_weight: float = max_weight
        self.current_weight: float = 0
        self.content: list[AdventurerItem] = []

    def current_weight(self) -> float:
        return sum(map(lambda elt: elt.weight, self.content))

    def add_item(self, item) -> None:
        self.content.append(item)
        self.current_weight += item.weight

    def empty(self) -> None:
        self.content = []
        self.current_weight = 0

    def is_overcharged(self) -> bool:
        return self.current_weight > self.max_weight

    def is_well_charged(self, percentage) -> bool:
        return not self.is_overcharged() and self.current_weight > self.max_weight * percentage

class ItemSet:

    def __init__(self) -> None:
        self.items = self.import_csv_data('.\items.csv')

    def import_csv_data(self, csv_file_path: str):
        with open(csv_file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader) # skip header if necessary
            data = []
            for row in csv_reader:
                adventurer_item = AdventurerItem(int(row[0]), row[1].strip(), float(row[2]), float(row[3]), round(float(row[3]) / float(row[2]), 5))
                data.append(adventurer_item)

            data = sorted(data, key=lambda elt: elt.valueWeightRatio, reverse=False)
            return data

def bruteforce(item_set: ItemSet, max_weight: float, acceptedPercentage: float = 0.9) -> list[Backpack]:

    res = []
    combinations = []
    for i in range(4):
        i_combinations = itertools.combinations(item_set.items, i)

        for i in i_combinations:
            combinations = combinations + [list(i)]

    print(f"there are {len(combinations)} combinations")

    #print("combinations:",  combinations)
    for combination in combinations:
        backpack = Backpack(max_weight)
        #print("combi:", combination)
        for item in combination:
            backpack.add_item(item)
            if backpack.is_overcharged():
                continue
        if backpack.is_well_charged(acceptedPercentage):
            res.append(backpack)

    return res



possible_backpacks = bruteforce(ItemSet(), max_weight=1.5)

print(f"got {len(possible_backpacks)} possible bp there")
for bp in possible_backpacks:
    print("bp content", bp.content)

#def solve(item_set: ItemSet, backpack: Backpack, resolver_method: function) -> list[AdventurerItem]:
#    pass


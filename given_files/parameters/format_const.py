
import csv
import json


def read_file(filename: str) -> list[int]:
    res = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            res.append(int(row[0]))
    return res

def format_integer_list(filename: str, language: str) -> str:
    data: list[int] = read_file(filename)
    if language == "python" or language == "nodejs":
        return json.dumps(data)
    if language == "java":
        return "".join(list(map(lambda x: "add(" + str(x) + ");\n", data)))
    if language == "c++":
        return "".join(list(map(lambda x: str(x) + ",\n", data)))

res = format_integer_list("./parameters/values_easy.csv", "js")

print(res)
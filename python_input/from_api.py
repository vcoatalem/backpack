import csv
import urllib.request


def get_data() -> list[list[str]]:
    url = "https://exaltemps-challenge-algo.s3.eu-west-3.amazonaws.com/easy.csv"

    with urllib.request.urlopen(url) as response:
        csv_data = response.read().decode('utf-8').splitlines()

    data = []
    reader = csv.reader(csv_data)
    next(reader)
    for row in reader:
        data.append((row[0], row[1]))
    return data

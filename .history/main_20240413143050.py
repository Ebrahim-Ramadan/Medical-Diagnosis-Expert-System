import json

with open('disease_categories.json', 'r') as file:
    disease_categories = json.load(file)


if __name__ == "__main__":
    print(disease_categories)

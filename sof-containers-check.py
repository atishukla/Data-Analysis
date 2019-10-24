import csv
from collections import defaultdict, Counter

with open('data/survey_results_public.csv', encoding='utf8') as f:
    csv_reader = csv.DictReader(f)

    for line in csv_reader:
        print(line['Containers'])
        break
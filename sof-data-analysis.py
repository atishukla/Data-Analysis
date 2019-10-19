import csv
from collections import defaultdict

with open('data/survey_results_public.csv', encoding='utf8') as f:
    csv_reader = csv.DictReader(f)

    # count becomes default dictionary which knows to expect int as value to keys
    counts = defaultdict(int)

    for line in csv_reader:
        counts[line['Hobbyist']] += 1

# Now Yes and No are in default dict as keys
total = counts['Yes'] + counts['No']

yes_pct = (counts['Yes'] / total) * 100
yes_pct = round(yes_pct, 2)

no_pct = (counts['No'] / total) * 100
no_pct = round(no_pct, 2)

print(f'Yes is {yes_pct}%')
print(f'Yes is {no_pct}%')

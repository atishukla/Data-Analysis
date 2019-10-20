import csv
from collections import defaultdict, Counter

with open('data/survey_results_public.csv', encoding='utf8') as f:
    csv_reader = csv.DictReader(f)
    total = 0

    # counter comes to rescue for things like counting and is intelligent as well
    language_counter = Counter()

    for line in csv_reader:
        languages = line['LanguageWorkedWith'].split(';')
        # instead of adding language_counter[language] += 1 we can use update method
        language_counter.update(languages)
        total += 1

# To print 5 most common language
for language, value in language_counter.most_common(5):
    language_pct = (value / total) * 100
    language_pct = round(language_pct, 2)

    print(f'{language}: {language_pct}%')

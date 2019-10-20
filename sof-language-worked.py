import csv
from collections import defaultdict, Counter

with open('data/survey_results_public.csv', encoding='utf8') as f:
    csv_reader = csv.DictReader(f)

    # counter comes to rescue for things like counting and is intelligent as well
    language_counter = Counter()

    for line in csv_reader:
        languages = line['LanguageWorkedWith'].split(';')
        for language in languages:
            # Now we need to create counter for this
            language_counter[language] += 1
        print(language_counter)
        break

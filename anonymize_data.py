import csv
import hashlib
import os


def anonymize_data(input_file, output_file, chunk_size=100000):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='',encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        for chunk in iter(lambda: list(reader)[:chunk_size], []):
            for row in chunk:
                row['first_name'] = hashlib.sha256(row['first_name'].encode()).hexdigest()
                row['last_name'] = hashlib.sha256(row['last_name'].encode()).hexdigest()
                row['address'] = hashlib.sha256(row['address'].encode()).hexdigest()
            writer.writerows(chunk)


if __name__ == "__main__":
    anonymize_data('sample_data.csv', 'anonymized_data.csv')

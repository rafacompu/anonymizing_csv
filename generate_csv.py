import csv
from faker import Faker

fake = Faker()


def generate_csv(file_name, num_rows):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(num_rows):
            writer.writerow({
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'address': fake.address().replace('\n', ' '),
                'date_of_birth': fake.date_of_birth()
            })


if __name__ == "__main__":
    print("Generating CSV file... this process may take a while.")
    generate_csv('sample_data.csv', 1000000)  # Generates a CSV with 1,000,000 rows
    print("CSV file generated successfully.")

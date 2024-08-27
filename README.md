# CSV Anonymization Project

This project generates a large CSV file containing fake personal data and provides a solution to anonymize specific columns in the CSV file. The solution is designed to handle large datasets, including files up to 2GB, and can be scaled to process even larger datasets using distributed computing with PySpark.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Generating the CSV File](#generating-the-csv-file)
  - [Anonymizing the CSV File](#anonymizing-the-csv-file)
  - [Scaling with PySpark](#scaling-with-pyspark)
- [Docker](#docker)

## Requirements

- Python 3.6 or higher
- pip (Python package installer)
- Optional: Docker (for containerized execution)
- Optional: PySpark (for distributed processing of large datasets)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rafacompu/anonymizing_csv.git
   cd anonymizing_csv

2. Installl the required Python packages:

   ```bash
   pip install -r requirements.txt
   
## Usage

### Generating the CSV File

To generate a CSV file with fake personal data, run the following command:

```bash
python generate_csv.py --output data.csv
```

This will create a file named sample_data.csv in the current directory. You can adjust the number of rows by modifying the num_rows parameter in the generate_csv.py script.

### Anonymizing the CSV File

To anonymize specific columns in the CSV file, run the following command:

```bash
python anonymize_csv.py --input data.csv --output anonymized_data.csv --columns "name" "email"
```

This will create a new file named anonymized_data.csv with the specified columns anonymized. You can add or remove columns to be anonymized by modifying the columns parameter in the anonymize_csv.py script.

### Scaling with PySpark

To scale the anonymization process using PySpark, you can use the anonymize_csv_pyspark.py script. This script requires PySpark to be installed and configured on your system.

```bash
spark-submit anonymize_csv_pyspark.py --input data.csv --output anonymized_data.csv --columns "name" "email"
```

This script will use PySpark to process the CSV file in a distributed manner, making it suitable for large datasets that do not fit in memory.

## Docker

You can also run the anonymization process in a Docker container. To build the Docker image, run the following command:

```bash
docker build -t anonymizing_csv .
```

To run the anonymization process inside a Docker container, use the following command:

```bash
docker run -v $(pwd):/app anonymizing_csv python anonymize_csv.py --input data.csv --output anonymized_data.csv --columns "name" "email"
```

Have fun!
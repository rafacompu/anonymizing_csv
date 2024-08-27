from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, col

# Initialize Spark session
spark = SparkSession.builder \
    .appName("CSV Anonymization") \
    .getOrCreate()

# Load the CSV file into a DataFrame
df = spark.read.csv("sample_data.csv", header=True, inferSchema=True)

# Anonymize the columns
anonymized_df = df.withColumn("first_name", sha2(col("first_name"), 256)) \
                  .withColumn("last_name", sha2(col("last_name"), 256)) \
                  .withColumn("address", sha2(col("address"), 256))

# Save the anonymized data to a new CSV file
anonymized_df.write.csv("anonymized_data_spark.csv", header=True)

# Stop the Spark session
spark.stop()

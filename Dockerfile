# Use the official Spark base image
FROM bitnami/spark:latest
LABEL authors="rafaotamendi"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Run the Spark job
CMD ["spark-submit", "--master", "local[*]", "anonymize_spark.py"]

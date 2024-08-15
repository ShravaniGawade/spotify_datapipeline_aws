# Spotify Playlists ETL Project

Project Overview
This project involves extracting, transforming, and loading (ETL) Spotify playlist data using various AWS services. The primary goal was to process and analyze large datasets effectively using Amazon S3, Amazon Glue, and Amazon Athena.

## Project Workflow

Data Collection:

The Spotify playlist data was uploaded to an Amazon S3 bucket.

ETL Process:

Amazon Glue was utilized to perform ETL operations on the data. The steps included:
Joining Tables: Combined various data tables to create a unified dataset.
Dropping Unnecessary Fields: Removed fields that were not required for analysis to optimize the dataset.
The transformed data was then reloaded into an Amazon S3 bucket.
Schema Detection:

A Glue Crawler was created to detect the schema of the transformed data and make it queryable.

Data Analysis:

The transformed data was imported into Amazon Athena where SQL queries were performed to analyze the data.

Technologies Used:
Amazon S3: For storing raw and transformed data.
Amazon Glue: For ETL operations, including data transformation and schema detection.
Amazon Athena: For querying and analyzing the transformed data.

Conclusion:
This project demonstrates the effective use of AWS services for managing and analyzing large-scale data. By leveraging Amazon Glue for ETL and Amazon Athena for querying, the project showcases the ability to process and analyze data efficiently.

Credit: This project was inspired by Date with Data on Youtube

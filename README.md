# Chesta_Associate_Data_and_Technology_Assignment

Introduction

This assignment focuses on building a simple assessment generation system for an educational question bank. The tasks involved SQL, Python, data cleaning, and basic system design. My approach was to create practical and easy-to-understand solutions while following the requirements provided.

Part 1: SQL Task

For the SQL task, I wrote a query to generate a Grade 6 Mathematics question paper. The query filters the question bank based on the required grade and subject and then randomly selects questions according to the given difficulty distribution:

4 Easy
4 Medium
2 Hard

The query ensures that duplicate questions are not selected and checks that the final paper contains questions from at least three different competencies. The output is arranged according to the difficulty level for better readability.

Assumptions
The question bank contains enough questions for each difficulty level.
Competency values are already cleaned and standardized.
Part 2: Python Task

The Python program reads the question bank dataset and generates a question paper based on a user-defined blueprint. The user can specify the grade, total number of questions, and the required difficulty distribution.

The program filters the data, randomly selects the required number of questions, and returns the final question paper. An option to export the generated paper was also included.

Assumptions
The cleaned dataset is used as input.
The dataset has enough questions to satisfy the requested blueprint.
Part 3: Data Cleaning

The messy dataset contained inconsistent values, missing data, and formatting issues. The cleaning process included:

Standardizing difficulty labels.
Standardizing subject names.
Cleaning question type values.
Standardizing grade values.
Removing duplicate records.
Handling missing values.
Converting marks and dates into appropriate formats.
Cleaning competency names and removing extra spaces.

Missing numerical values were filled using suitable methods, while categorical fields were standardized and completed where appropriate. A cleaned version of the dataset was generated for further use.

Assumptions
Missing question text records were removed as they could not be used for assessment generation.
Missing categorical values were filled using the most suitable available values.
Missing dates were handled during the cleaning process.
Part 4: System Design

A simple automated reporting system was proposed to send weekly dashboard summaries to program teams.

The system would:

Collect data from the database.
Process and summarize the data.
Generate dashboard reports.
Send the reports automatically through Email or Teams/Slack.

A scheduler would run the process every week. Basic logging and error handling would help identify failures, and notifications could be sent if any part of the process failed.

Tools Used
Python
Pandas
PostgreSQL
SQL
pgAdmin
Overall Approach

The main objective of this assignment was to build simple, practical, and maintainable solutions. The focus was on data quality, clear logic, and meeting the given requirements while making reasonable assumptions where necessary.

Thank you for reviewing my assignment.

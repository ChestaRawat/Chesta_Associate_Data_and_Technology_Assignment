# Chesta - Associate Data & Technology Assignment

## Introduction

This assignment focuses on building a simple assessment generation system for an educational question bank. The tasks involved SQL, Python, data cleaning, and basic system design. The objective was to create practical, maintainable, and easy-to-understand solutions while adhering to the given requirements.



# Part 1: SQL Task

## Objective

Generate a Grade 6 Mathematics question paper from the question bank based on a predefined blueprint.

## Solution Overview

The SQL query performs the following operations:

* Filters questions for:

  * Grade 6
  * Mathematics subject
* Randomly selects questions according to the required difficulty distribution:

  * 4 Easy questions
  * 4 Medium questions
  * 2 Hard questions
* Prevents duplicate question selection.
* Ensures that questions cover at least three different competencies.
* Orders the final output by difficulty level for better readability.

## Assumptions

* The question bank contains sufficient questions for each difficulty level.
* Competency values are already cleaned and standardized.
* Question IDs are unique.



# Part 2: Python Task

## Objective

Develop a Python-based assessment generator that creates question papers dynamically using a user-defined blueprint.

## Solution Overview

The Python application:

* Reads the question bank dataset.
* Accepts user inputs such as:

  * Grade
  * Subject
  * Total number of questions
  * Difficulty distribution
* Filters the dataset based on the selected criteria.
* Randomly selects questions according to the blueprint.
* Generates the final question paper.
* Supports exporting the generated assessment.

## Key Features

* Dynamic blueprint configuration.
* Randomized question selection.
* Duplicate question prevention.
* Easy-to-maintain modular structure.

## Assumptions

* The cleaned dataset is used as the input source.
* The dataset contains enough questions to satisfy the requested blueprint.
* Difficulty labels are standardized.



# Part 3: Data Cleaning

## Objective

Prepare a clean and consistent dataset suitable for assessment generation.

## Data Quality Issues Identified

The raw dataset contained:

* Inconsistent difficulty labels
* Inconsistent subject names
* Mixed question type formats
* Duplicate records
* Missing values
* Formatting inconsistencies
* Invalid or inconsistent date formats

## Cleaning Steps Performed

### Standardization

* Standardized difficulty labels.
* Standardized subject names.
* Standardized question type values.
* Standardized grade values.
* Cleaned competency names and removed extra spaces.

### Duplicate Handling

* Removed duplicate records based on relevant columns.

### Missing Value Treatment

* Removed records with missing question text.
* Filled missing categorical values where appropriate.
* Handled missing dates using suitable approaches.
* Filled missing numerical values using appropriate methods.

### Data Type Corrections

* Converted marks into numeric format.
* Converted date fields into proper datetime format.

## Output

A cleaned dataset was generated and used for both SQL and Python assessment generation tasks.

## Assumptions

* Records without question text are unusable and were removed.
* Missing categorical values were completed using the most appropriate available values.
* Date-related issues were resolved during the cleaning process.



# Part 4: System Design

## Objective

Design a simple automated reporting system that sends weekly dashboard summaries to program teams.

## Proposed Workflow

### Step 1: Data Collection

* Extract data from the source database.

### Step 2: Data Processing

* Perform aggregations and calculations.
* Generate summary metrics and KPIs.

### Step 3: Report Generation

* Create dashboard summaries.
* Prepare visual reports and insights.

### Step 4: Automated Distribution

* Send reports automatically through:

  * Email
  * Microsoft Teams
  * Slack

### Step 5: Monitoring & Logging

* Maintain execution logs.
* Track failures and processing status.
* Send alerts when failures occur.

## System Components

* Database
* Data Processing Layer
* Reporting Engine
* Scheduler (Weekly Execution)
* Notification Service
* Logging & Monitoring Module

## Benefits

* Reduces manual reporting effort.
* Improves reporting consistency.
* Enables timely communication of key insights.
* Supports scalable report distribution.



# Tools & Technologies Used

* Python
* Pandas
* SQL
* PostgreSQL
* pgAdmin



# Overall Approach

The primary goal of this assignment was to develop simple, practical, and maintainable solutions that satisfy the business requirements.

Key focus areas included:

* Data quality and consistency
* Clear and scalable logic
* Requirement-driven implementation
* Reasonable assumptions where necessary
* Maintainability and ease of understanding

The solutions were designed to be straightforward while ensuring reliability, flexibility, and usability for future enhancements.



# Thank You

Thank you for reviewing my assignment. I appreciate your time and consideration.

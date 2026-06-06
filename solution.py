import pandas as pd
import random

# Load Question Bank

file_path = r"C:\Users\isha1\OneDrive\Pictures\Documents\GitHub\ASSIGNMENT PEEPUL\Part_1_2_question_bank - question_bank_clean 1.xlsx"

df = pd.read_excel(file_path)

# Blueprint Configuration

grade = int(input("Enter grade: "))
total_questions = int(input("Enter total questions: "))

easy = int(input("Enter number of easy questions: "))
medium = int(input("Enter number of medium questions: "))
hard = int(input("Enter number of hard questions: "))

if easy + medium + hard != total_questions:
    print("Error: Difficulty distribution does not match total questions.")
    exit()


# Competency Selection

competency_distribution = {}

choice = input(
    "Do you want competency-wise selection? (yes/no): "
).lower()

if choice == "yes":

    competencies = list(df["competency"].unique())

    print("\nAvailable Competencies:")

    for i, j in enumerate(competencies, 1):
        print(f"{i}. {j}")

    remaining = total_questions

    for j in competencies:

        if remaining == 0:
            break

        print(f"\nRemaining questions: {remaining}")

        num = int(
            input(
                f"How many questions from {j}? "
            )
        )

        while num > remaining:

            print(
                f"You can allocate at most {remaining} questions."
            )

            num = int(
                input(
                    f"How many questions from {j}? "
                )
            )

        competency_distribution[j] = num

        remaining -= num
blueprint = {
    "grade": grade,
    "difficulty_distribution": {
        "easy": easy,
        "medium": medium,
        "hard": hard
    }
}

# Generate Paper

def generate_question_paper(data, blueprint, competency_distribution):

    grade_data = data[
        data["grade"] == blueprint["grade"]
    ]

    selected_questions = []

    used_ids = set()

    for difficulty, count in blueprint["difficulty_distribution"].items():

        difficulty_data = grade_data[
            grade_data["difficulty"].str.lower()
            == difficulty.lower()
        ]

        if len(competency_distribution) > 0:

            for j in list(competency_distribution.keys()):

                if count == 0:
                    break

                needed = competency_distribution[j]

                if needed == 0:
                    continue

                comp_data = difficulty_data[
                    (difficulty_data["competency"] == j)
                    &
                    (~difficulty_data["question_id"].isin(used_ids))
                ]

                take = min(
                    needed,
                    count,
                    len(comp_data)
                )

                if take > 0:

                    sample = comp_data.sample(
                        n=take,
                        replace=False,
                        random_state=random.randint(1,10000)
                    )

                    selected_questions.append(sample)

                    used_ids.update(
                        sample["question_id"]
                    )

                    competency_distribution[j] -= take

                    count -= take

        if count > 0:

            remaining_data = difficulty_data[
                ~difficulty_data["question_id"].isin(
                    used_ids
                )
            ]

            take = min(
                count,
                len(remaining_data)
            )

            if take > 0:

                sample = remaining_data.sample(
                    n=take,
                    replace=False,
                    random_state=random.randint(1,10000)
                )

                selected_questions.append(sample)

                used_ids.update(
                    sample["question_id"]
                )

    final_paper = pd.concat(
        selected_questions
    )

# Sort questions by difficulty

    difficulty_order = {
        "easy": 1,
        "medium": 2,
        "hard": 3
    }

    final_paper["difficulty_order"] = final_paper["difficulty"].str.lower().map(
        difficulty_order
    )

    final_paper = final_paper.sort_values(
        by="difficulty_order"
    )

    final_paper = final_paper.drop(
        columns=["difficulty_order"]
    )

    final_paper = final_paper.reset_index(drop=True)

    # Add Question Numbers
    final_paper.index += 1

    return final_paper

# Generate

question_paper = generate_question_paper(
    df,
    blueprint,
    competency_distribution
)

# Display

print("QUESTION PAPER")

for i, row in question_paper.iterrows():

    print(f"\nQ{i}")

    print(row["question_text"])

    print(
        "Difficulty :",
        row["difficulty"]
    )

    print(
        "Competency :",
        row["competency"]
    )

    print(
        "Marks :",
        row["marks"]
    )

# Export

ans_file = "Generated_Question_Paper.csv"

question_paper.to_csv(
    ans_file,
    index=False
)

print("\nQuestion paper generated successfully.")
print(
    "Saved as:",
    ans_file
)
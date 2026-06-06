-- Grade 6 Mathematics Question Paper Generator
-- Requirements:
-- 4 Easy Questions
-- 4 Medium Questions
-- 2 Hard Questions
-- Minimum 3 competencies
-- No duplicate questions

WITH grade6_math AS (
    SELECT *
    FROM question_bank
    WHERE subject = 'Mathematics'
      AND grade = 6
),

competency_summary AS (
    SELECT COUNT(DISTINCT competency) AS competency_count
    FROM grade6_math
),

easy AS (
    SELECT *,
           ROW_NUMBER() OVER (ORDER BY RANDOM()) AS seq_no
    FROM grade6_math
    WHERE difficulty ILIKE 'easy'
),

medium AS (
    SELECT *,
           ROW_NUMBER() OVER (ORDER BY RANDOM()) AS seq_no
    FROM grade6_math
    WHERE difficulty ILIKE 'medium'
),

hard AS (
    SELECT *,
           ROW_NUMBER() OVER (ORDER BY RANDOM()) AS seq_no
    FROM grade6_math
    WHERE difficulty ILIKE 'hard'
),

final_paper AS (
    SELECT * FROM easy
    WHERE seq_no <= 4

    UNION ALL

    SELECT * FROM medium
    WHERE seq_no <= 4

    UNION ALL

    SELECT * FROM hard
    WHERE seq_no <= 2
)

SELECT
    ROW_NUMBER() OVER (
        ORDER BY
            CASE difficulty
                WHEN 'Easy' THEN 1
                WHEN 'Medium' THEN 2
                ELSE 3
            END,
            question_id
    ) AS q_no,

    question_id,
    subject,
    grade,
    competency,
    difficulty,
    question_type,
    marks,
    question_text

FROM final_paper
WHERE (
    SELECT competency_count
    FROM competency_summary
) >= 3;

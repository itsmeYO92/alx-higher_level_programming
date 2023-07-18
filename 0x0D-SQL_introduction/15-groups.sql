-- select rows where the score is the same
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;

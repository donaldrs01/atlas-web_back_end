-- Task 7: Procedure to calculate and stores the average score for student based on user_id

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id int
)
BEGIN
    DECLARE avg_score FLOAT 
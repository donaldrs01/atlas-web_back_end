-- Task 7: Procedure to calculate and stores the average score for student based on user_id

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN input_id int
)
BEGIN
    DECLARE avg_score FLOAT; -- declare avg_score variable
    -- Use corrections values to calculate average score and store in variable
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = input_id;
    -- Update average_score column in 'users' table with avg_score value
    UPDATE users
    SET average_score = avg_score
    WHERE id = input_id;
END$$

DELIMITER ;

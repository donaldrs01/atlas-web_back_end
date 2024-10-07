-- Task 10: SafeDiv function that performs division operation

DELIMITER $$

CREATE FUNCTION SafeDiv(
    a INT,
    b INT
)
RETURNS FLOAT
DETERMINISTIC -- specifies that function will always return same result for same input values
BEGIN
    -- If divisor is 0, return 0 in order to perform 'safe division'
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END$$

DELIMITER ;
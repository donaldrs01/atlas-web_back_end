-- Task 10: SafeDiv function that performs division operation

CREATE FUNCTION SafeDiv(
    a INT,
    b INT
)
RETURNS FLOAT
BEGIN
    -- If divisor is 0, return 0 in order to perform 'safe division'
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END$$

DELIMITER ;
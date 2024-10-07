-- Task 5: Creating trigger to reset valid email attribute when email updated

DELIMITER $$

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users -- Trigger only activated before any updates on user table
FOR EACH ROW
BEGIN
    -- Check if email has been updated
    IF NEW.email != OLD.email THEN
        -- Reset attribute when changed
        SET NEW.valid_email = 0;
    END IF; -- Do nothing if new email same as old email
END$$

DELIMITER ;
-- Working with procedures to implement AddBonus to give bonus on a particular project
DELIMITER $$

CREATE PROCEDURE AddBonus( -- three input parameters
    IN user_id INT,
    IN project_name VARCHAR(256),
    IN score INT
)
BEGIN
    DECLARE project_id INT;  -- Search for existing project_id

    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name

    IF project_id IS NULL THEN -- if project doesn't exist, create new one
        -- Add new project into row 'projects' with the given project_name
        INSERT INTO projects (name) VALUES (project_name);
        -- Retrieves ID of new project and sets it as project_id value
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert bonus / correction
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END$$

DELIMITER ;
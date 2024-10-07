-- Task 4: Create trigger to decrease quantity of item when ordered

-- Change delimiter to temporarily ignore ;
delimiter $$

CREATE TRIGGER update_quantity
AFTER INSERT ON orders 
FOR EACH ROW 
BEGIN 
    -- Decrease item quantity in items table
    UPDATE items
    SET quantity = quantity - NEW.number -- update quantity in items table
    WHERE name = NEW.item_name; -- update name in items table
END$$

DELIMITER ;
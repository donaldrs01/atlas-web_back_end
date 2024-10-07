-- Task 9: Creating a composite index
-- Index on first letter of 'name' column and 'score' column
CREATE INDEX idx_name_first_score ON names (name(1), score);


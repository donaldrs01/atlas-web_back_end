-- Task 8: Creating an index on large datasets

CREATE INDEX idx_name_first ON names (name(1));
-- Creating index on table 'names'
-- Uses only first character of name column
-- Forward engineer the users_schema you created in the previous chapter

-- Create a .txt file where you'll save each of the queries you'll run in the workbench

-- Query: Create 3 new users

INSERT INTO users (first_name, last_name, email) VALUES ("Tyler", "Maxwell", "tm@email.com"), ("Ed", "Im", "ei@email.com"), ("Shawn", "Converse", "sdog@email.com");

-- Query: Retrieve all the users

SELECT * FROM users;

-- Query: Retrieve the first user using their email address

SELECT * FROM users WHERE email LIKE "tm%";

-- Query: Retrieve the last user using their id

SELECT * FROM users WHERE id = 3;

-- Query: Change the user with id=3 so their last name is Pancakes

UPDATE users SET last_name = "Pancakes" WHERE id=3;
SELECT * FROM users;

-- Query: Delete the user with id=2 from the database

SET SQL_SAFE_UPDATES = 0;
DELETE FROM users WHERE id = 2;

-- Query: Get all the users, sorted by their first name

SELECT * FROM users
ORDER BY first_name;

-- BONUS Query: Get all the users, sorted by their first name in descending order
SELECT * FROM users
ORDER BY first_name DESC;
-- Submit your .txt file that contains all the queries you ran in the workbench
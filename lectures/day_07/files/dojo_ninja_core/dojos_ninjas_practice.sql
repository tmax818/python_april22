-- dojos and ninjas practice

-- Forward engineer the dojos_and_ninjas_schema from the previous chapter

-- Create a .txt file where you'll save each of your queries from below

-- Query: Create 3 new dojos
INSERT INTO dojos (name) VALUES ('Burbank'),('San Jose'),('Chicago');


-- Query: Delete the 3 dojos you just created
-- SET SQL_SAFE_UPDATES = 0;
-- DELETE FROM dojos;

-- Query: Create 3 more dojos
INSERT INTO dojos (name) VALUES ('Burbank'),('San Jose'),('Chicago');


-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Joe", "Coder",39, 13),("Jessica", "Coder",29, 13),("Linus", "To",49, 13);


-- Query: Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Jenny", "Sam",39, 14),("Marty", "McCoder",29, 14),("Jesus", "Montes",33, 14);

-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Jenny", "Jenny",39, 15),("Sid", "Virtuous",29, 15),("Jesus", "Jones",33, 15);

-- Query: Retrieve all the ninjas from the first dojo
SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojos.id = 13;

-- Query: Retrieve all the ninjas from the last dojo
SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojos.id = (SELECT id FROM dojos ORDER BY id DESC LIMIT 1);

-- Query: Retrieve the last ninja's dojo
SELECT * FROM dojos
WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);

-- Submit your .txt file that contains all the queries you ran in the shell
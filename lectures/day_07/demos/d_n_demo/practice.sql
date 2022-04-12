-- Query: Create 3 new dojos

INSERT INTO dojos (name) VALUES("Burbank"),("San Jose"),("On line");

-- Query: Delete the 3 dojos you just created
DELETE FROM dojos WHERE id=1;

-- Query: Create 3 more dojos
INSERT INTO dojos (name) VALUES("Chicago"),("Seattle"),("Tulsa");

-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Jenny", "Sam",39, 14),("Marty", "McCoder",29, 14),("Jesus", "Montes",33, 14);

-- Query: Create 3 ninjas that belong to the second dojo

-- Query: Create 3 ninjas that belong to the third dojo

-- Query: Retrieve all the ninjas from the first dojo

SELECT * FROM ninjas WHERE dojo_id = 3;

-- Query: Retrieve all the ninjas from the last dojo

-- Query: Retrieve the last ninja's dojo
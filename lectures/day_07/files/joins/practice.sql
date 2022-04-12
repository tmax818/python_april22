SET SQL_SAFE_UPDATES = 0;
DELETE from lefts;
DELETE from rights;
DELETE from left_right;

SELECT * FROM lefts;
SELECT * FROM rights;
INSERT INTO lefts (left_name) VALUES ("Lisa"), ("Larry"), ("Louis"),("Lafonda"),("Lonely");
INSERT INTO rights (right_name) VALUES ("Ronnie"), ("Robert"), ("Reggie"),("Rita"),("Really Stinky");

INSERT INTO left_right (left_id, right_id) VALUES (1,1),(2,2),(3,3),(4,4);

SELECT lefts.left_name, rights.right_name FROM lefts
RIGHT JOIN left_right ON lefts.id = left_right.left_id
RIGHT JOIN rights ON left_right.right_id = rights.id;

SELECT * FROM lefts
LEFT JOIN left_right ON lefts.id = left_right.left_id
LEFT JOIN rights ON left_right.right_id = rights.id;



SELECT * FROM rights
LEFT JOIN left_right ON rights.id = left_right.right_id
LEFT JOIN lefts ON left_right.left_id = lefts.id;




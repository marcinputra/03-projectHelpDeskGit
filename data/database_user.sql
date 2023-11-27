DROP TABLE IF EXISTS "users";
DROP TABLE IF EXISTS "organization";

CREATE TABLE "users"
(
    "id"                INTEGER PRIMARY KEY AUTOINCREMENT,
    "name"              TEXT NOT NULL,
    "lastname"          TEXT NOT NULL,
    "login"             TEXT NOT NULL,
    "password"          TEXT NOT NULL,
    "id_organization"   TEXT NOT NULL
);

CREATE TABLE "organization"
(
    "id"                INTEGER PRIMARY KEY AUTOINCREMENT,
    "nameorganiztaion"  TEXT NOT NULL,
    "adress"            TEXT NOT NULL,
    "city"              TEXT NOT NULL
);

INSERT INTO "users"
VALUES (NULL, 'user', 'userLast', 'user', '1234', 1);

INSERT INTO "organization"
VALUES (NULL, 'Biuro1', 'Polna 1', 'Sopot');
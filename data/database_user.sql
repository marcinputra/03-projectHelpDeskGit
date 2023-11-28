--PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS "users";
DROP TABLE IF EXISTS "organization";
DROP TABLE IF EXISTS "reports";

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

CREATE TABLE "reports"
(
    "id_reports" INTEGER PRIMARY KEY AUTOINCREMENT,
    "type_e"     TEXT NOT NULL,
    "id_user"    INTEGER,
    "data"       DATE,
    "state"      TEXT,
    "location"   TEXT,
    FOREIGN KEY ("id_user") REFERENCES "users" ("id")
);


INSERT INTO "users"
VALUES  (NULL, 'user', 'userLast', 'user', '1234', 1),
        (NULL, 'admin', 'userLast', 'admin', '1234', 1);

INSERT INTO "organization"
VALUES (NULL, 'Biuro1', 'Polna 1', 'Sopot');

INSERT INTO "reports"
VALUES  (NULL, 'Naprawa PC', 1, '2012-12-02', 'Otwarte', 'sala 1'),
        (NULL, 'Wymiana SSD', 2, '2013-01-08', 'Otwarte', 'sala 3');

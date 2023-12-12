PRAGMA FOREIGN_KEY = ON;

DROP TABLE IF EXISTS "users";
DROP TABLE IF EXISTS "organization";
DROP TABLE IF EXISTS "reports";
DROP TABLE IF EXISTS "events";

CREATE TABLE "users"
(
    "id"                INTEGER PRIMARY KEY AUTOINCREMENT,
    "name"              TEXT NOT NULL,
    "lastname"          TEXT NOT NULL,
    "login"             TEXT NOT NULL,
    "password"          TEXT NOT NULL,
    "id_organization"   TEXT NOT NULL,
    "is_admin"          INTEGER NOT NULL
);

CREATE TABLE "organization"
(
    "id"                INTEGER PRIMARY KEY AUTOINCREMENT,
    "nameorganiztaion"  TEXT NOT NULL,
    "adress"            TEXT NOT NULL,
    "city"              TEXT NOT NULL
);

CREATE TABLE "events"
(
    "id_events" INTEGER PRIMARY KEY AUTOINCREMENT,
    "type_e"    TEXT NOT NULL
);

CREATE TABLE "reports"
(
    "id_reports" INTEGER PRIMARY KEY AUTOINCREMENT,
    "id_events"  INTEGER,
    "id_user"    INTEGER,
    "data"       DATE,
    "state"      TEXT,
    "location"   TEXT,
    "description"TEXT,
    "phone"      TEXT,
    "mail"       TEXT,
    FOREIGN KEY ("id_user") REFERENCES "users" ("id"),
    FOREIGN KEY ("id_events") REFERENCES "events" ("id_events")
);

INSERT INTO "users"
VALUES  (NULL, 'user', 'userLast', 'user', '1234', 1, false),
        (NULL, 'admin', 'userLast', 'admin', '1234', 1, true);

INSERT INTO "organization"
VALUES (NULL, 'Biuro1', 'Polna 1', 'Sopot');

INSERT INTO "events"
VALUES  (NULL, 'Naprawa PC'),
        (NULL, 'Wymiana dysku'),
        (NULL, 'Instalacja oprogramowania');

INSERT INTO "reports"
VALUES  (NULL, 1, 1, '2012-12-02', 'Otwarte', 'sala 1', 'Opis zadania nr 1','540123123','user@mail.pl'),
        (NULL, 3, 1, '2012-12-06', 'Zamknięte', 'sala 6', 'Opis zadania nr 3','670124543','admin@mail.com'),
        (NULL, 2, 2, '2013-01-08', 'Otwarte', 'sala 3', 'Opis zadania nr 2','600100100','user@domena.pl');

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
VALUES  (NULL, 'Jan', 'Nowak', 'user', 'scrypt:32768:8:1$m2MIEMl5mQTJx2js$c596ac7662dcc4db97c8370487879718c0478f565fd468e5fdb965269c146d2bf723e2bbe8ebbc61be7821bf91847bd5f0697d2823c2a3874a6e17c7f8c5ac43', 1, false),
        (NULL, 'Piotr', 'Kowalski', 'admin', 'scrypt:32768:8:1$m2MIEMl5mQTJx2js$c596ac7662dcc4db97c8370487879718c0478f565fd468e5fdb965269c146d2bf723e2bbe8ebbc61be7821bf91847bd5f0697d2823c2a3874a6e17c7f8c5ac43', 1, true);

INSERT INTO "organization"
VALUES (NULL, 'Biuro1', 'Polna 1', 'Sopot');

INSERT INTO "events"
VALUES  (NULL, 'Naprawa PC'),
        (NULL, 'Wymiana dysku'),
        (NULL, 'Instalacja oprogramowania');

INSERT INTO "reports"
VALUES  (NULL, 1, 1, '2022-12-02', 'Otwarte', 'sala 1', 'Opis zadania nr 1','540123123','user@mail.pl'),
        (NULL, 2, 1, '2023-12-06', 'Zamknięte', 'sala 6', 'Opis zadania nr 2','670124543','admin@mail.com'),
        (NULL, 3, 2, '2023-09-20', 'Otwarte', 'sala 3', 'Opis zadania nr 3','567780018','main@abc.pl'),
        (NULL, 1, 1, '2023-10-10', 'Otwarte', 'sala 3', 'Opis zadania nr 4','687298345','root@poland.pl'),
        (NULL, 2, 2, '2023-11-09', 'Otwarte', 'sala 3', 'Opis zadania nr 5','456012892','port@wer.pl');

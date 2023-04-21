DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    displayName TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL
);



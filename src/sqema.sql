CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);



CREATE TABLE tasks(
    id INTEGER PRIMARY KEY,
    task TEXT,
    user_id INTEGER REFERENCES users
);


CREATE TABLE task_classes (
    id INTEGER PRIMARY KEY,
    task_id INTEGER REFERENCES tasks,
    value TEXT
);
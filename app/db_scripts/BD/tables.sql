CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100)
);

CREATE TABLE notes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_notes VARCHAR(100),
    text text,
    time_create INT NOT NULL DEFAULT (strftime('%s','now')),
    time_update INT NOT NULL DEFAULT (strftime('%s','now')),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
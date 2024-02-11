CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100)
);

CREATE TABLE tools(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_tools VARCHAR(100),
    text text,
    time_create INT NOT NULL DEFAULT (strftime('%s','now')),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
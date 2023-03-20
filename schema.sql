DROP TABLE IF EXISTS posts;
/*
DROP TABLE IF EXISTS env_data;
DROP TABLE IF EXISTS setting_data;
*/
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT (datetime('now','localtime')),
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
/*
CREATE TABLE env_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT (datetime('now','localtime')),
    pm25 REAL DEFAULT 0,
    pm10 REAL DEFAULT 0,
    temperature REAL DEFAULT 0,
    humidity REAL DEFAULT 0,
    noise REAL DEFAULT 0
);

CREATE TABLE setting_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT (datetime('now','localtime')),
    brightness varchar DEFAULT '-',
    systemname varchar DEFAULT '-'
);
*/

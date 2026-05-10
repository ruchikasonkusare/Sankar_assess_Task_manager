CREATE DATABASE taskdb;

\c taskdb;

CREATE TABLE users (
    id         SERIAL PRIMARY KEY,
    username   VARCHAR(80)  UNIQUE NOT NULL,
    email      VARCHAR(120) UNIQUE NOT NULL,
    password   VARCHAR(200) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tasks (
    id          SERIAL PRIMARY KEY,
    title       VARCHAR(200) NOT NULL,
    description TEXT,
    priority    VARCHAR(20) DEFAULT 'Medium',
    status      VARCHAR(20) DEFAULT 'Pending',
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id     INTEGER REFERENCES users(id) ON DELETE CASCADE
);
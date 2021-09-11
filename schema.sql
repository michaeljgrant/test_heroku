CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    username TEXT,
    email TEXT,
    password_hash TEXT
)

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    comment_poster INTEGER,
    post_content TEXT,
)

CREATE TABLE likes (
    post_id INTEGER,
    username_id INTEGER,
    post_like BOOLEAN,

)


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    username TEXT,
    email TEXT,
    password_hash TEXT
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    poster_id INTEGER,
    post_content TEXT,
    post_title,
    FOREIGN KEY(poster_id)
    REFERENCES users(id)
);

CREATE TABLE likes (
    post_id INTEGER,
    user_id INTEGER,
    post_like BOOLEAN,
    FOREIGN KEY(user_id)
    REFERENCES users(id)
);



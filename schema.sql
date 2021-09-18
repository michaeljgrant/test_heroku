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
    imageurl,
    FOREIGN KEY(poster_id)
    REFERENCES users(id)
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    post_id INTEGER,
    commenter_id INTEGER,
    comment_content TEXT,
    FOREIGN KEY (post_id)
    REFERENCES posts(id)
);


CREATE TABLE likes (
    post_id INTEGER,
    user_id INTEGER,
    post_like BOOLEAN,
    FOREIGN KEY(user_id)
    REFERENCES users(id)
);


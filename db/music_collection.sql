DROP TABLE if EXISTS albums;
DROP TABLE if EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    year VARCHAR(255),
    artist_id INT REFERENCES artists(id)
);
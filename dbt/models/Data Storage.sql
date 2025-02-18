CREATE TABLE covid_cleaned (
    id SERIAL PRIMARY KEY,
    state VARCHAR(255),
    country VARCHAR(255),
    date DATE,
    cases INT
);
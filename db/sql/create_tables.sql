CREATE DATABASE mycarrer;

GRANT ALL PRIVILEGES ON DATABASE mycarrer TO postgres;

\c mycarrer

CREATE TABLE "jobs" (
  "id" SERIAL PRIMARY KEY,
  "title" varchar,
  "description" text,
  "started_at" timestamp,
  "finished_at" timestamp
);

INSERT INTO jobs(title, description, started_at)
VALUES
    ('My Job 1','Lorem ipsum dolor sit amet, consectetur', NOW()),
    ('My Job 2','Lorem ipsum dolor sit amet, consectetur', NOW()),
    ('My Job 3','Lorem ipsum dolor sit amet, consectetur', NOW()),
    ('My Job 4','Lorem ipsum dolor sit amet, consectetur', NOW()),
    ('My Job 5','Lorem ipsum dolor sit amet, consectetur', NOW()),
    ('My Job 6','Lorem ipsum dolor sit amet, consectetur', NOW());
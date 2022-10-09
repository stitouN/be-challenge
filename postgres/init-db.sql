CREATE TABLE IF NOT EXISTS users(
user_id bigserial PRIMARY key NOT NULL,
    firstName text NOT NULL,
    lastName  text NOT NULL,
    phoneNumber character  NOT null
);
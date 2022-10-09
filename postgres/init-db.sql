-- A script that will be initialize the postgres database
-- During the building of the image so it will be executed once 
-- Remember to run docker-compose down --volumes

CREATE TABLE IF NOT EXISTS users(
user_id bigserial PRIMARY key NOT NULL,
    firstName text NOT NULL,
    lastName  text NOT NULL,
    phoneNumber text  NOT null
);

--
-- The query to insert a 1MM data randomly 

INSERT INTO users (firstName, lastName, phoneNumber)
SELECT CONCAT ('NAJ','', substr('ABCDEFGHIJKLMNOPQRSTUVWXYZ', round(random() * 30)::integer, 5)),
    CONCAT ('STI','', substr('ABCDEFGHIJKLMNOPQRSTUVWXYZ', round(random() * 30)::integer, 5)),
   CONCAT ('06','', trunc(random() * 10000000 + 99999999))
FROM generate_series(1, 1000000);
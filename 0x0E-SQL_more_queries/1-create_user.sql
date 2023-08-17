-- 1-create_user.sql
-- Create the user if it doesn't exist, and set its password

CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO user_0d_1@localhost;

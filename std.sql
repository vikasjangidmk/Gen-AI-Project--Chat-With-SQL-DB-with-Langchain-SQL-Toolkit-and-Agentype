-- Use the created database
USE student;

-- Create the STUDENT table
CREATE TABLE STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);

-- Insert data into the STUDENT table
INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Krish', 'Data Science', 'A', 90);
INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Vikas', 'Data Science', 'B', 92);
INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Muskan', 'Data Science', 'C', 93);

select * from STUDENT;


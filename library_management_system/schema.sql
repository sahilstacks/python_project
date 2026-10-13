CREATE DATABASE library;
USE library;

CREATE TABLE users ( 
						Userid VARCHAR(100) NOT NULL,
						Password VARCHAR(100) NOT NULL 
					);

CREATE TABLE Student ( 
						Student_ID VARCHAR(25) PRIMARY KEY, 
						Name VARCHAR(100), 
						Phone VARCHAR(10), 
						Email VARCHAR(100), 
						DOB DATE, 
						College VARCHAR(100), 
						Course VARCHAR(100)  
					);

CREATE TABLE Book_Issue ( 
							Student_ID VARCHAR(25), 
							Book_ID VARCHAR(50), 
							Book_Name VARCHAR(100), 
							Book_HSN_Code VARCHAR(50), 
							Book_Author VARCHAR(100), 
							Issue_Date DATE, 
							Return_Date DATE, 
							Per_Day_Fine VARCHAR(5), 
							FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID) 
						);
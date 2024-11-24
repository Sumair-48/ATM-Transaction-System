-- Create a Database for ATM Transaction Details:

CREATE DATABASE ATM_SYS;

-- Now we use query to use the database: 

USE atm_sys;

-- Create Table for user details:

CREATE TABLE ATM_ACC_DETAIL
(
ID BIGINT UNSIGNED auto_increment,
Acc_num BIGINT UNSIGNED Check (Acc_num Between 1000000000000 and 9999999999999),
Acc_owner VARCHAR(50),
Acc_pass INT UNSIGNED Check(Acc_pass Between 1000 and 9999) UNIQUE,
Acc_Owner_Occ VARCHAR(50),
CNIC_Num BIGINT UNSIGNED CHECK(CNIC_Num Between 1000000000000 and 9999999999999) UNIQUE,
Age TINYINT UNSIGNED Check (Age between 18 and 110),
City VARCHAR(50),
PRIMARY KEY (ID,Acc_num),
UNIQUE(Acc_num)
);

-- Create Table for Account Transaction Details:

CREATE TABLE ATM 
(
Acc_Id BIGINT UNSIGNED Check (Acc_Id Between 1000000000000 and 9999999999999),
Withdraw INT UNSIGNED,
Deposit INT UNSIGNED,
date_time datetime
);

-- Table For AccountDifference/Balance

CREATE TABLE AccountDifferences (
    Acc_num BIGINT UNSIGNED,
    Difference DECIMAL(10, 2),
    FOREIGN KEY (Acc_num) REFERENCES ATM_ACC_DETAIL(Acc_num)
);

-- Insert Values into AccountDifference

INSERT INTO AccountDifferences (Acc_num, Difference)
SELECT Acc_Id AS Acc_num,SUM(Deposit) - SUM(Withdraw) AS Difference
FROM ATM
GROUP BY Acc_Id;

SELECT * FROM accountdifferences;

SELECT * FROM atm_acc_detail;

SELECT * FROM ATM;


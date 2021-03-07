sql = ('CREATE TABLE ABC.XYZ.students_test (
    id integer PRIMARY KEY,
    first_name text,
    last_name text NOT NULL,
    street text,
    city text,
    st text,
    zip text
);')
sql2 = ' '
        'CREATE DATABASE numismatics;'
sql3 = (' '
        'CREATE TABLE table1 (att_int INT(8) PRIMARY KEY,
			att_char CHAR(2),
			att_varchar VARCHAR(20),
			att_bit BIT,
			att_tinyint TINYINT,
			att_smallint SMALLINT(2),
			att_integer INTEGER(4),
			att_bigint BIGINT,
			att_real REAL,
			att_double DOUBLE,
			att_float FLOAT,
			att_decimal DECIMAL,
			att_numeric NUMERIC,
			att_bin bin(10),
			CONSTRAINT table8_fk FOREIGN KEY(att_integer)
                           REFERENCES table8(att_integer));')
sql4 = ' '
        'CREATE TABLE table2 (att_int INT(8) PRIMARY KEY);'
sql5 = ' '
        'CREATE TABLE table3 (att_char CHAR(2) PRIMARY KEY);'
sql6 = ' '
        'CREATE TABLE table4 (att_varchar VARCHAR(20) PRIMARY KEY);'
sql7 = ' '
        'CREATE TABLE table5 (att_bit BIT PRIMARY KEY);'
sql8 = ' '
        'CREATE TABLE table6 (att_tinyint TINYINT PRIMARY KEY);'
sql9 = ' '
        'CREATE TABLE table7 (att_smallint SMALLINT(2) PRIMARY KEY);'
sql10 = ' '
         'CREATE TABLE table8 (att_integer INTEGER(4) PRIMARY KEY);'
sql11 = ' '
         'CREATE TABLE table9 (att_bigint BIGINT PRIMARY KEY);'
sql12 = ' '
         'CREATE TABLE table10 (att_real REAL PRIMARY KEY);'
sql13 = ' '
         'CREATE TABLE table11 (att_double DOUBLE PRIMARY KEY);'
sql14 = ' '
         'CREATE TABLE table12 (att_float FLOAT PRIMARY KEY);'
sql15 = ' '
         'CREATE TABLE table13 (att_decimal DECIMAL PRIMARY KEY);'
sql16 = ' '
         'CREATE TABLE table14 (att_numeric NUMERIC PRIMARY KEY);'
sql17 = ' '
         'CREATE TABLE table15 (att_binary bin(10) PRIMARY KEY);'
sql18 = (' '
         'CREATE TABLE table16 (att_int INT(8) PRIMARY KEY,
			att_char CHAR(2),
			att_varchar VARCHAR(20),
			att_bit BIT,
			att_tinyint TINYINT,
			att_smallint SMALLINT(2),
			att_integer INTEGER(4),
			att_bigint BIGINT,
			att_real REAL,
			att_double DOUBLE,
			att_float FLOAT,
			att_decimal DECIMAL,
			att_numeric NUMERIC,
			att_bin bin(10),
			CONSTRAINT table17_fk FOREIGN KEY(att_int)
                           REFERENCES table17(att_int));')
sql19 = ' '
         'CREATE TABLE table17 (att_int INT(8) PRIMARY KEY);'
sql20 = ' '
         'CREATE TABLE table18 (att_char CHAR(2) PRIMARY KEY);'
sql21 = ' '
         'CREATE TABLE table19 (att_varchar VARCHAR(20) PRIMARY KEY);'
sql22 = ' '
         'CREATE TABLE table20 (att_bit BIT PRIMARY KEY);'
sql23 = ' '
         'CREATE TABLE table21 (att_tinyint TINYINT PRIMARY KEY);'
sql24 = ' '
         'CREATE TABLE table22 (att_smallint SMALLINT(2) PRIMARY KEY);'
sql25 = ' '
         'CREATE TABLE table23 (att_integer INTEGER(4) PRIMARY KEY);'
sql26 = ' '
         'CREATE TABLE table24 (att_bigint BIGINT PRIMARY KEY);'
sql27 = ' '
         'CREATE TABLE table25 (att_real REAL PRIMARY KEY);'
sql28 = ' '
         'CREATE TABLE table26 (att_double DOUBLE PRIMARY KEY);'
sql29 = ' '
         'CREATE TABLE table27 (att_float FLOAT PRIMARY KEY);'
sql30 = ' '
         'CREATE TABLE table28 (att_decimal DECIMAL PRIMARY KEY);'
sql31 = ' '
         'CREATE TABLE table29 (att_numeric NUMERIC PRIMARY KEY);'
sql32 = ' '
         'CREATE TABLE table30 (att_binary bin(100) PRIMARY KEY);'
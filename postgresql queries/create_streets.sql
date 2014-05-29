-- Table: "STREETS"

-- DROP TABLE "STREETS";

CREATE TABLE "STREETS"
(
STREET varchar,
CROSS1 varchar,
CROSS2 varchar
);

COPY "STREETS" FROM 'C:\Users\Tyler\Documents\RampUp\ProjectX\street_final_sql.csv' USING DELIMITERS ',' CSV;
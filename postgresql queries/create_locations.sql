-- Table: "LOCATIONS"

-- DROP TABLE "LOCATIONS";

CREATE TABLE LOCATIONS
(
LOCATION varchar,
SIGN varchar,
PRIMARY KEY (LOCATION)
);

COPY LOCATIONS FROM 'C:\Users\Tyler\Documents\RampUp\ProjectX\locations_final.csv' USING DELIMITERS ',' CSV;
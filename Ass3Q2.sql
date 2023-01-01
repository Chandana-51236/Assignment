CREATE DATABASE Football;

CREATE TABLE FootBallVenue(
venue_id int NOT NULL PRIMARY KEY,
venue_name varchar(25) NOT NULL,
city_id int NOT NULL,
Capacity int NOT NULL);

INSERT INTO FootballVenue(venue_id,venue_name,city_id,Capacity)
VALUES(20001,"France",10003,42115),
(23789,"Spain",19868,56213),
(20871,"UK",32145,30576),
(98654,"Europe",78436,43268),
(75831,"Japan",54986,49763),
(92413,"India",34782,87543),
(70654,"Malaysia",27631,86324),
(98347,"Russia",56987,39654),
(98236,"Sweden",48537,67943),
(98604,"Singapore",78243,90534);

SELECT count(venue_name) from FootballVenue;

SELECT venue_name as Location,capacity as Volume FROM footballvenue;

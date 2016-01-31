-- Table definitions for the tournament project.


DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE table players (
	id serial primary key,
	name text NOT NULL
	);

CREATE table matches (
	id serial primary key,
	id1 integer references players(id),
	id2 integer references players(id),
	winner integer NOT NULL
	);

CREATE table records(
	id integer references players(id),
	name text NOT NULL,
	wins integer NOT NULL,
	played integer NOT NULL
	);

CREATE table pairings(
	id serial primary key,
	id1 integer references players(id),
	name1 text NOT NULL,
	id2 integer references players(id),
	name2 text NOT NULL
	);

CREATE view standings as 
	select * from records order by wins desc;
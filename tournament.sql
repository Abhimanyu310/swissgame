-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


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

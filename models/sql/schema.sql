CREATE TABLE settings (
	name 				TEXT,
	value				TEXT
);
INSERT INTO settings VALUES ('db_version', 1);
INSERT INTO settings VALUES ('idx_movies', 'TheMovieDb');
INSERT INTO settings VALUES ('idx_tv', 'TheMovieDb');

CREATE TABLE movie (
	movie_id 			INTEGER PRIMARY KEY AUTOINCREMENT,
	indexer 			TEXT,
	id					TEXT,
	imdb_id 			TEXT,
	title 				TEXT,
	date 				DATE,
	overview 			TEXT,
	status 				TEXT,
	rating 				REAL,
	poster 				TEXT
);

CREATE TABLE tv (
	tv_id 				INTEGER PRIMARY KEY AUTOINCREMENT,
	indexer 			TEXT,
	id					TEXT,
	imdb_id 			TEXT,
	title 				TEXT,
	date 				DATE,
	overview 			TEXT,
	status 				TEXT,
	rating 				REAL,
	poster 				TEXT,
	n_episodes 			INTEGER,
	n_seasons 			INTEGER
);

CREATE TABLE episode (
	episode_id 			INTEGER PRIMARY KEY AUTOINCREMENT,
	tv_id 				INTEGER,
	indexer 			TEXT,
	id					TEXT,
	title 				TEXT,
	season_number		INTEGER,
	episode_number		INTEGER,
	date 				DATE,
	overview 			TEXT
);
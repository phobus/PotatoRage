CREATE TABLE db_version (
	db_version INTEGER
);
            
CREATE TABLE indexer (
	indexer_id INTEGER PRIMARY KEY,
	name TEXT,
	url TEXT,
	series INTEGER,
	movies INTEGER
);

CREATE TABLE media (
	media_id INTEGER PRIMARY KEY AUTOINCREMENT,
	type TEXT,
	indexer_id INTEGER,
	imdb_id TEXT,
	title TEXT,
	date DATE,
	overview TEXT,
	status TEXT,
	rating REAL,
	poster TEXT
);

INSERT INTO db_version VALUES (1);
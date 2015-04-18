CREATE TABLE db_version (
	db_version INTEGER
);
            
CREATE TABLE indexer (
	indexer_id INTEGER PRIMARY KEY,
	name TEXT,
	url TEXT,
	idx_tv INTEGER,
	idx_movie INTEGER
);

CREATE TABLE media (
	media_id INTEGER PRIMARY KEY AUTOINCREMENT,
	type TEXT,
	indexer_id INTEGER,
	id INTEGER,
	imdb_id TEXT,
	title TEXT,
	date DATE,
	overview TEXT,
	status TEXT,
	rating REAL,
	poster TEXT,
	n_episodes INTEGER,
	n_seasons INTEGER
);

INSERT INTO db_version VALUES (1);
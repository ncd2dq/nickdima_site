DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS scores;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS feedback;

CREATE TABLE users (
	id int(16) AUTO_INCREMENT,
	username varchar(16) UNIQUE NOT NULL,
	password varchar(150) NOT NULL,
	primary key (id)
);


CREATE TABLE scores (
	id int(16) AUTO_INCREMENT,
	user_id int(16) NOT NULL,
	game_name varchar(150) NOT NULL,
	score int(16) NOT NULL,
	day TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	primary key (id)
);


CREATE TABLE posts (
	id int(16) AUTO_INCREMENT,
	author_id int(16) NOT NULL,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	title varchar(150) NOT NULL,
	body varchar(350) NOT NULL,
	primary key (id)
);


CREATE TABLE feedback (
	id int(16) AUTO_INCREMENT,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	title varchar(150) NOT NULL,
	body varchar(350) NOT NULL,
	primary key (id)
)
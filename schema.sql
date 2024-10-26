CREATE TABLE IF NOT EXISTS "surveyInfo" (
	"id"	INTEGER,
	"longitude"	REAL NOT NULL,
	"latitude"	REAL NOT NULL,
	"response"	TEXT,
	"rating"	INTEGER NOT NULL,
	PRIMARY KEY("id")
)
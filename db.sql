CREATE TABLE IF NOT EXISTS global_prices (
	Date date,
	Symbol VARCHAR(30),
	Open REAL,
	High REAL,
	Low REAL,
	Close REAL,
	"Adj Close" REAL,
	Volume REAL,
	PRIMARY KEY (Date, Symbol)
);

SELECT * FROM global_prices;

SELECT * FROM us_tickers_kr;

DROP TABLE global_prices;
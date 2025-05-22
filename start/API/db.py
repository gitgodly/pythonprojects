import logging
import psycopg2

class PostgresHandler(logging.Handler):
    def __init__(self, conn_params):
        logging.Handler.__init__(self)
        self.conn = psycopg2.connect(**conn_params)
        self.cursor = self.conn.cursor()

    def emit(self, record):
        log_entry = self.format(record)
        self.cursor.execute(
            "INSERT INTO logs (message, level, timestamp) VALUES (%s, %s, now())",
            (log_entry, record.levelname)
        )
        self.conn.commit()

# Usage
logger = logging.getLogger("pgLogger")
logger.setLevel(logging.INFO)

pg_handler = PostgresHandler({
    "dbname": "postgres",
    "user": "postgres",
    "password": "bcmch",
    "host": "localhost"
})
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
pg_handler.setFormatter(formatter)
logger.addHandler(pg_handler)

logger.info("This log is stored in PostgreSQL!")

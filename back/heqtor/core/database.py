from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import config

# url format : dialect+driver://username:password@host:port/database
def url_formatter(database_config):
    if "url" in database_config and database_config["url"] is not None:
        return database_config["url"]
    try:
        url = database_config["dialect"] if "dialect" in database_config else "sqlite"
        if "driver" in database_config and database_config["driver"] is not None:
            url += f"+{database_config['driver']}"
        url += "://"
        if url == "sqlite://":
            if "path_to_sqlite_db" in database_config:
                url += database_config["path_to_sqlite_db"]
            return url
        url += f"{database_config['username']}:{database_config['password']}@{database_config['host']}:{database_config['port']}/{database_config['database']}"
    except:
        print("Wrong database config, using sqlite in-memory database instead.")
        url = "sqlite://"
    finally:
        return url


db = create_engine(
    url_formatter(config["database"]), echo=config["database"]["echo"] == "True"
)
Session = sessionmaker(bind=db)

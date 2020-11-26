import logging
import os

config = {
    "database": {
        "dialect": os.environ.get("DB_DIALECT", "sqlite"),
        "driver": os.environ.get("DB_DRIVER", None),
        "username": os.environ.get("DB_USERNAME", None),
        "password": os.environ.get("DB_PASSWORD", None),
        "host": os.environ.get("DB_HOST", "localhost"),
        "port": os.environ.get("DB_PORT", None),
        "database": os.environ.get("DB_DATABASE", None),
        "path_to_sqlite_db": "/test.db",
        "url": None,
        "echo": os.environ.get("DB_ECHO", False),
    },
    "flask_app": {
        "name": os.environ.get("FLASK_APP_NAME", "heqtor"),
        "env": os.environ.get(
            "FLASK_APP_ENV", os.environ.get("BACKEND_ENV", "development")
        ),
        "debug": os.environ.get("FLASK_APP_DEBUG", True),
        "jwt_key": os.environ.get("FLASK_APP_JWT_SECRET_KEY", "ksjdflj_uaAAHU&$$^,dsq"),
        "jwt_expires": os.environ.get("FLASK_APP_JWT_ACCESS_TOKEN_EXPIRES", 86400),
    },
    "env": os.environ.get("BACKEND_ENV", "development"),
}

logger = logging.getLogger()
formatter = logging.Formatter(
    "%(process)d %(asctime)s %(name)-12s %(levelname)-8s %(message)s"
)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

log_level = config.get("log", "INFO")
if log_level == "DEBUG":
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

logger = logging.getLogger("heqtor")

version = "0.1.0"

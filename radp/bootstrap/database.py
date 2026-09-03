from radp.config.settings import DatabaseSettings
from radp.infrastructure.persistence.database import (create_engine_from_url,
                                                      create_schema,
                                                      create_session_factory,
                                                      drop_schema)


def create_database(settings: DatabaseSettings):
    engine = create_engine_from_url(settings.url)
    create_schema(engine)


def drop_database(settings: DatabaseSettings):
    engine = create_engine_from_url(settings.url)
    drop_schema(engine)


def reset_database(settings: DatabaseSettings):
    engine = create_engine_from_url(settings.url)
    drop_schema(engine)
    create_schema(engine)


def session_factory(settings: DatabaseSettings):
    engine = create_engine_from_url(settings.url)
    return create_session_factory(engine)

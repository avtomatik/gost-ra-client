from pydantic_settings import BaseSettings

from radp.infrastructure.persistence.database import (create_engine_from_url,
                                                      create_schema,
                                                      create_session_factory)


def build_persistence(settings: BaseSettings):
    engine = create_engine_from_url(settings.database_url)
    create_schema(engine)
    return create_session_factory(engine)

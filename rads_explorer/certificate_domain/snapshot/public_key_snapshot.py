from rads_explorer.certificate_domain.models.base import DomainModel


class PublicKeySnapshot(DomainModel):
    algorithm: str
    oid: str | None = None
    key_size: int | None = None
    parameters: str | None = None

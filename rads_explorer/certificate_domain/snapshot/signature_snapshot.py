from rads_explorer.certificate_domain.models.base import DomainModel


class SignatureSnapshot(DomainModel):
    oid: str
    algorithm: str | None = None

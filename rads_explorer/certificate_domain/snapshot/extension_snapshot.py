from pydantic import Field

from rads_explorer.certificate_domain.models.base import DomainModel


class ExtensionSnapshot(DomainModel):
    oid: str
    name: str | None = None
    critical: bool
    value: str
    python_type: str | None = Field(
        default=None, description="cryptography class name"
    )

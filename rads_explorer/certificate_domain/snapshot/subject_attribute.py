from pydantic import Field

from rads_explorer.certificate_domain.models.base import DomainModel


class SubjectAttribute(DomainModel):
    oid: str
    name: str | None = None
    value: str
    short_name: str | None = Field(default=None, description="CN, O, OU, etc.")

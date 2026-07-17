from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from rads_explorer.api.schemas.extension import Extension
from rads_explorer.api.schemas.name_attributes import NameAttributes


class Certificate(BaseModel):
    id: UUID
    name_attributes: NameAttributes

    serial_number: str
    thumbprint: str

    not_before: datetime
    not_after: datetime
    key_not_after: datetime
    created_when: datetime

    status: str

    cert_request_id: UUID | None = None
    subject: str | None = None
    issuer: str | None = None
    user_id: UUID | None = None

    version: int = 3

    public_key: str | None = None
    public_key_parameters: str | None = None
    public_key_oid: str | None = None
    public_key_oid_description: str | None = None

    extensions: list[Extension] | None = None

    signature: str | None = None
    signature_oid: str | None = None
    signature_oid_description: str | None = None

    raw_certificate: bytes | None = None

    revocation_reason: str | None = None
    revoked_when: datetime | None = None

    folder: str | None = None

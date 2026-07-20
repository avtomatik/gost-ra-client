from datetime import datetime

from rads_explorer.certificate_domain.models.base import DomainModel


class ValiditySnapshot(DomainModel):
    not_before: datetime
    not_after: datetime

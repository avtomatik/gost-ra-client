from typing import Protocol

from cryptography.x509 import Certificate, ObjectIdentifier


class CertificateInspector(Protocol):
    def subject(
        self, certificate: Certificate, oid: ObjectIdentifier
    ) -> str | None: ...
    def certificate_template_oid(
        self, certificate: Certificate
    ) -> str | None: ...

from cryptography.x509 import Certificate

from rads_explorer.certificate_domain.models.base import DomainModel

from .extension_snapshot import ExtensionSnapshot
from .public_key_snapshot import PublicKeySnapshot
from .signature_snapshot import SignatureSnapshot
from .subject_attribute import SubjectAttribute
from .validity_snapshot import ValiditySnapshot


class CertificateSnapshot(DomainModel):
    """
    Canonical parsed representation of an X.509 certificate.
    Every consumer in the application operates on this model
    instead of directly inspecting cryptography objects.
    """

    certificate: Certificate
    serial_number: str
    version: int
    fingerprint_sha1: str
    fingerprint_sha256: str
    subject: str
    issuer: str
    subject_attributes: list[SubjectAttribute]
    issuer_attributes: list[SubjectAttribute]
    extensions: list[ExtensionSnapshot]
    public_key: PublicKeySnapshot
    signature: SignatureSnapshot
    validity: ValiditySnapshot

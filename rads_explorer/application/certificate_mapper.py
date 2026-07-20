from cryptography.x509 import ObjectIdentifier
from cryptography.x509.oid import NameOID

from rads_explorer.certificate_domain.constants.oids import OID
from rads_explorer.certificate_domain.contracts.inspector import \
    CertificateInspector
from rads_explorer.certificate_domain.crypto.parser import CertificateParser
from rads_explorer.certificate_domain.models.certificate import Certificate
from rads_explorer.data.reports_models import CertificateDetailReportRow


class CertificateDetailMapper:
    def __init__(self, inspector: CertificateInspector) -> None:
        self._inspector = inspector

    def map(self, certificate: Certificate) -> CertificateDetailReportRow:
        x509_certificate = CertificateParser.parse(certificate.raw_certificate)

        return CertificateDetailReportRow(
            ogrn=self._inspector.subject(x509_certificate, NameOID.OGRN),
            organization_name=self._inspector.subject(
                x509_certificate, NameOID.ORGANIZATION_NAME
            ),
            guid=self._inspector.subject(
                x509_certificate, ObjectIdentifier(OID.GUID)
            ),
            surname=self._inspector.subject(x509_certificate, NameOID.SURNAME),
            given_name=self._inspector.subject(
                x509_certificate, NameOID.GIVEN_NAME
            ),
            organizational_unit_name=self._inspector.subject(
                x509_certificate, NameOID.ORGANIZATIONAL_UNIT_NAME
            ),
            title=self._inspector.subject(x509_certificate, NameOID.TITLE),
            common_name=self._inspector.subject(
                x509_certificate, NameOID.COMMON_NAME
            ),
            serial_number=certificate.serial_number,
            snils=self._inspector.subject(x509_certificate, NameOID.SNILS),
            status=certificate.status,
            certificate_template=self._inspector.certificate_template_oid(
                x509_certificate
            ),
            revoked_when=certificate.revoked_when,
            not_before=x509_certificate.not_valid_before_utc,
            not_after=x509_certificate.not_valid_after_utc,
        )

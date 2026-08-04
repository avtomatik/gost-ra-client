from radp.domain.models.certificate import CertificateSnapshot
from radp.oid_registry import oids

from .models import CertificateInventoryRow


class CertificateProjection:
    @staticmethod
    def inventory(snapshot: CertificateSnapshot) -> CertificateInventoryRow:
        subject = snapshot.subject_by_oid
        extensions = snapshot.extension_by_oid
        return CertificateInventoryRow(
            ogrn=subject.get(oids.OGRN),
            organization_name=subject.get(oids.O),
            guid=subject.get(oids.GUID),
            surname=subject.get(oids.SN),
            given_name=subject.get(oids.GIVEN_NAME),
            organizational_unit_name=subject.get(oids.OU),
            title=subject.get(oids.T),
            common_name=subject.get(oids.CN),
            serial_number=snapshot.metadata.serial_number,
            snils=subject.get(oids.SNILS),
            status=snapshot.metadata.status,
            certificate_template=extensions.get(oids.CERTIFICATE_TEMPLATE),
            revoked_when=snapshot.metadata.revoked_when,
            not_before=snapshot.metadata.not_before,
            not_after=snapshot.metadata.not_after,
        )

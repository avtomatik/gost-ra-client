from cryptography.x509 import (AttributeNotFound, Certificate,
                               ExtensionNotFound, ObjectIdentifier)

from rads_explorer.api.schemas.oids import OID


class X509Inspector:

    @staticmethod
    def subject(cert: Certificate, oid: ObjectIdentifier) -> str | None:
        try:
            attrs = cert.subject.get_attributes_for_oid(oid)

        except AttributeNotFound:
            return None

        return attrs[0].value if attrs else None

    @staticmethod
    def extension(cert: Certificate, oid: ObjectIdentifier):
        try:
            return cert.extensions.get_extension_for_oid(oid)

        except ExtensionNotFound:
            return None

    @staticmethod
    def certificate_template_oid(cert: Certificate) -> str | None:
        ext = X509Inspector.extension(
            cert,
            ObjectIdentifier(OID.CERTIFICATE_TEMPLATE),
        )

        if ext is None:
            return None

        return ext.value.template_id.dotted_string

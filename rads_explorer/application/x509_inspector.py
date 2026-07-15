import logging

from cryptography.x509 import (AttributeNotFound, Certificate,
                               ExtensionNotFound, ObjectIdentifier)

from rads_explorer.api.schemas.oids import OID

logger = logging.getLogger(__name__)


class X509Inspector:
    @staticmethod
    def subject(cert: Certificate, oid: ObjectIdentifier):
        def load():
            attrs = cert.subject.get_attributes_for_oid(oid)
            return attrs[0].value if attrs else None

        try:
            return X509Inspector._safe(load)
        except AttributeNotFound:
            return None

    @staticmethod
    def extension(cert: Certificate, oid: ObjectIdentifier):
        try:
            return cert.extensions.get_extension_for_oid(oid)
        except ExtensionNotFound:
            return None
        except Exception:
            logger.exception(
                "Unable to parse certificate extensions while reading %s",
                oid.dotted_string,
            )
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

    @staticmethod
    def _safe(fn, *, default=None, operation="inspection"):
        try:
            return fn()
        except Exception:
            logger.exception("Certificate %s failed", operation)
            return default

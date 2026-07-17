import logging
from collections.abc import Callable
from typing import Any

from cryptography.x509 import (AttributeNotFound, Certificate, Extension,
                               ExtensionNotFound, ObjectIdentifier)

from rads_explorer.certificate_domain.constants.oids import OID

logger = logging.getLogger(__name__)


class X509Inspector:
    def subject(self, cert: Certificate, oid: ObjectIdentifier) -> str | None:
        def load() -> str | None:
            attrs = cert.subject.get_attributes_for_oid(oid)
            return attrs[0].value if attrs else None

        try:
            return self._safe(load, operation="subject lookup")
        except AttributeNotFound:
            return None

    def extension(
        self, cert: Certificate, oid: ObjectIdentifier
    ) -> Extension[Any] | None:
        try:
            return cert.extensions.get_extension_for_oid(oid)
        except ExtensionNotFound:
            return None
        except Exception:
            logger.exception(
                "Unable to parse certificate extension %s", oid.dotted_string
            )
            return None

    def certificate_template_oid(self, cert: Certificate) -> str | None:
        ext = self.extension(
            cert,
            ObjectIdentifier(OID.CERTIFICATE_TEMPLATE),
        )

        if ext is None:
            return None

        return ext.value.template_id.dotted_string

    @staticmethod
    def _safe(
        fn: Callable[[], Any], *, default: Any = None, operation: str
    ) -> Any:
        try:
            return fn()
        except Exception:
            logger.exception("Certificate %s failed", operation)
            return default

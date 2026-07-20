from cryptography.x509 import Certificate

from .certificate_snapshot import CertificateSnapshot


class CertificateAnalyzer:
    def analyze(self, certificate: Certificate) -> CertificateSnapshot: ...

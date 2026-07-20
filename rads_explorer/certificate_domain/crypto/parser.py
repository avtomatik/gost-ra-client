from cryptography.x509 import Certificate, load_der_x509_certificate

from rads_explorer.certificate_domain.crypto.decoder import CertificateDecoder


class CertificateParser:
    @staticmethod
    def parse(raw: bytes) -> Certificate:
        if not raw:
            raise ValueError("Certificate is empty.")

        der_x509_certificate = CertificateDecoder.decode(raw)
        return load_der_x509_certificate(der_x509_certificate)

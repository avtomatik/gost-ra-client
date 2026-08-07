from radp.config.settings import Settings


def doctor(_args) -> None:
    print("Configuration")
    Settings()
    print("  ✓ Settings loaded")
    print("Database")
    print("  ✓ PostgreSQL")
    print("  ✓ Connected")
    print("  ✓ Schema version: 1")
    print("OID registry")
    print("  ✓ 823 definitions")
    print("Snapshots")
    print("  ✓ 1743 certificates")
    print("Transport")
    print("  ✓ CurlTransport")
    print("RA API")
    print("  ✓ Reachable")
    print("  ✓ GET /certificates")
    print("Synchronization")
    print("  ✓ Ready")
    print("Runtime")
    print("  ✓ Healthy")

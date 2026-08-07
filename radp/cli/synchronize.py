from radp.bootstrap.runtime import get_runtime


def synchronize(_args) -> None:
    print("Synchronizing certificates...")
    runtime = get_runtime()
    count = runtime.synchronization.synchronize()
    print(f"Appended {count} certificates.")

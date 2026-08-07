import argparse

from radp.bootstrap.initialize import initialize_runtime


def bootstrap(args: argparse.Namespace) -> None:
    initialize_runtime(reset=args.reset)
    print("Initialization completed.")

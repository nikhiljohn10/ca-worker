#!/usr/bin/env python3

from caworker.deploy import deploy
from caworker.utils import arguments


def main():
    input = arguments()
    deploy(
        input.token,
        input.worker,
        input.worker_file,
        input.caurl,
        input.fingerprint,
        input.rootca,
    )


if __name__ == "__main__":
    main()

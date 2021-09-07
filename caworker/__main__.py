#!/usr/bin/env python3

from .deploy import deploy
from .utils import arguments


def main():
    input = arguments()
    deploy(
        input.title,
        input.worker,
        input.worker_file,
        input.caurl,
        input.fingerprint,
        input.rootca,
    )


if __name__ == "__main__":
    main()

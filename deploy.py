#!/usr/bin/env python3

from caworker import CAWorker, workerArgs


def main(title: str, name: str, file: str, ca: str, fp: str, ca_url: str):
    worker = CAWorker(title, fp, ca_url)
    worker.loadCA(ca)
    url = worker.deploy(name, file)
    print("Worker is deployed successfully")
    print(f"{title} URL:", url)


if __name__ == "__main__":
    args = workerArgs()
    main(
        title=args.title,
        name=args.worker,
        file=args.file,
        ca=args.rootca,
        fp=args.fingerprint,
        ca_url=args.caurl,
    )

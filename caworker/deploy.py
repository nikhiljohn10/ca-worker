#!/usr/bin/env python3

from pathlib import Path
from CloudflareAPI import Cloudflare
from CloudflareAPI.exceptions import CFError


def deploy(
    token: str,
    name: str,
    worker: str,
    worker_file: str,
    caurl: str,
    fingerprint: str,
    rootca: str,
):

    worker_file = Path(worker_file).resolve(strict=True)
    rootca = Path(rootca).resolve(strict=True)

    print(f"Deploying worker: {worker}")
    cf = Cloudflare(token)

    try:
        namespace_id = cf.store.get_id("STEPCA_KEYSTORE")
    except CFError:
        namespace_id = cf.store.create("STEPCA_KEYSTORE")

    metadata = cf.worker.Metadata()
    metadata.add_binding("STEPCA_KEYSTORE", namespace_id)
    metadata.add_variable("ROOT_CA_FINGERPRINT", fingerprint)
    metadata.add_variable("ROOT_CA_URL", caurl)
    metadata.add_variable("CA_TITLE", name)
    metadata.add_secret("ACCESS_TOKEN", token)

    if cf.worker.upload(worker, worker_file, metadata):
        if cf.worker.deploy(worker):
            subdomain = cf.worker.subdomain.get()
            print(f"Worker is deployed for {name}")
            print(f"URL: https://{worker}.{subdomain}.workers.dev")

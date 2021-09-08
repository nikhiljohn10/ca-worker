#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path
from CloudflareAPI import Cloudflare
from CloudflareAPI.exceptions import CFError

WORKER_NS_NAME_KEY = "CA_CERTSTORE"
WORKER_TITLE_KEY = "CA_TITLE"
WORKER_FINGERPRINT_KEY = "ROOT_CA_FINGERPRINT"
WORKER_CA_URL_KEY = "ROOT_CA_URL"


@dataclass
class WorkerData:
    title: str
    fingerprint: str
    url: str

    def get_metadata(self, worker):
        metadata = worker.Metadata()
        metadata.add_variable(WORKER_TITLE_KEY, self.title)
        metadata.add_variable(WORKER_FINGERPRINT_KEY, self.fingerprint)
        metadata.add_variable(WORKER_CA_URL_KEY, self.url)
        return metadata


class CAWorker(Cloudflare):
    def __init__(self, web_title: str, fingerprint: str, ca_url: str) -> None:
        super().__init__()
        data = WorkerData(web_title, fingerprint, ca_url)
        self.metadata = data.get_metadata(self.worker)

    def loadCA(self, rootCA: str):
        try:
            rootca = Path(rootCA).read_text()
        except UnicodeDecodeError:
            rootca = Path(rootCA).read_bytes()
        try:
            namespace = self.store.get_ns(WORKER_NS_NAME_KEY)
        except CFError:
            namespace = self.store.create(WORKER_NS_NAME_KEY)
        namespace.write("root_ca", rootca)
        self.metadata.add_binding(WORKER_NS_NAME_KEY, namespace.id)

    def deploy(self, worker_name, file):
        worker_file = Path(file).resolve(strict=True)
        if self.worker.upload(
            name=worker_name,
            file=worker_file,
            metadata=self.metadata,
        ):
            if self.worker.deploy(worker_name):
                subdomain = self.worker.subdomain.get()
                return f"https://{worker_name}.{subdomain}.workers.dev"

        raise ValueError("Unexpected input error")

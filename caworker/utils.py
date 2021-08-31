#!/usr/bin/env python3

import argparse


def arguments():
    parser = argparse.ArgumentParser(
        prog="deploy", description="Worker Deployment"
    )
    parser.add_argument(
        "-t",
        "--token",
        dest="token",
        type=str,
        help="Cloudflare API Token",
    )
    parser.add_argument(
        "-u",
        "--url",
        dest="caurl",
        type=str,
        help="CA Server's URL",
    )
    parser.add_argument(
        "-f",
        "--fingerprint",
        dest="fingerprint",
        type=str,
        help="Root CA Certificate's fingerprint",
    )
    parser.add_argument(
        "-w",
        "--worker",
        dest="worker",
        type=str,
        help="Name of the worker",
        default="ca",
    )
    parser.add_argument(
        "-l",
        "--location",
        dest="worker_file",
        type=str,
        help="Worker file location",
        default="./worker/worker.js",
    )
    parser.add_argument(
        "-r",
        "--rootca",
        dest="rootca",
        type=str,
        help="CA Root Certificate file in PEM or DER format",
        default="./certs/Cloudflare_CA.crt",
    )
    return parser.parse_args()

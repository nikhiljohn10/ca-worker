# ca-worker
A Cloudflare worker which can be deployed by a CA to publish certificates and fingerprint securely to users for bootstrapping.


## Deployment

```
export TOKEN="YOUR_ACCESS_TOKEN"
export FINGERPRINT="YOUR_ROOT_CA_FINGERPRINT"
export CA_URL="YOUR_ROOT_CA_SERVER_URL"
make deploy
```
addEventListener("fetch", (event) => {
  event.respondWith(
    handleRequest(event.request).catch(
      (err) => new Response(err.stack, {
        status: 500
      })
    )
  )
})

async function handleRequest(request) {
  const { pathname } = new URL(request.url)

  if (pathname.startsWith("/root_ca.crt")) {
    let certificate
    const format = await CA_CERT_STORE.get("root_ca_format")
    if (format == "der") {
      certificate = await CA_CERT_STORE.get("root_ca", "arrayBuffer")
      return new Response(certificate, {
        headers: {
          "Content-Type": "application/octet-stream"
        }
      })
    }
    certificate = await CA_CERT_STORE.get("root_ca")
    return new Response(certificate, {
      headers: {
        "Content-Type": "application/x-x509-ca-cert"
      }
    })
  }

  if (pathname.startsWith("/fp")) {
    return new Response(ROOT_CA_FINGERPRINT)
  }

  if (pathname.startsWith("/url")) {
    return new Response(ROOT_CA_URL)
  }

  if (pathname == ("/" || "")) {
    return new Response(get_html(), {
      headers: {
        "Content-Type": "text/html;charset=UTF-8"
      }
    })
  }

  return new Response(new Error("Path not found"), {
    status: 404
  })
}

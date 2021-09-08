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
    certificate = await CA_CERTSTORE.get("root_ca", "arrayBuffer")
    return new Response(certificate, {
      headers: {
        "Content-Type": "application/octet-stream"
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

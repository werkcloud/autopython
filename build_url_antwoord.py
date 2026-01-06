def build_url(hostname, path, resource, port=443, ext=".html"):
    """Bouw volledige HTTPS URL met defaults."""
    port_part = f":{port}" if port != 443 else ""
    return f"https://{hostname}{port_part}/{path}{resource}{ext}"


def main():
    url = build_url("service.org", "api/v2/", "servers", port=7700, ext=".json")
    print(url)
    url = build_url("service.org", "api/v2/", "routers")  # defaults
    print(url)


if __name__ == "__main__":
    main()

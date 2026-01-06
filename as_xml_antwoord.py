def indent(content, spaces=2):
    '''Voeg spaces voor content en return resultaat.'''
    return " " * spaces + content


def as_xml(content, tag_name):
    '''Wrap content in XML tags en return.'''
    return f"<{tag_name}>{content}</{tag_name}>"


def main():
    name = "Paris"
    ip = "10.0.0.135"
    xml_name = as_xml(name, "name")
    xml_ip = as_xml(ip, "ip4")

    print(indent(xml_name))       # default spaces=2
    print(indent(xml_ip, 4))      # override spaces


if __name__ == "__main__":
    main()

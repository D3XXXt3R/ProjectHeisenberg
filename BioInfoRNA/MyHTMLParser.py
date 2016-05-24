from html.parser import HTMLParser
import re


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
            # Check the list of defined attributes.
            for name, value in attrs:
                # If href is defined, print it.
                if name == "href":
                    if (value[7:15] == 'www.rcsb'):
                        # print(name, "=", value)
                        if (re.findall('\d+', value[-4:])):
                            # print(name, "=", value)
                            print("PDB id")
                            print(value[-4:])
                            print(value)
                    if (value[7:15] == 'ndbserve'):
                        if (re.findall('\d+', value[-6:]) and not ('=' in value[-6:])):
                            # print(name, "=", value)
                            print("NDB id")
                            print(value[-6:])
                            print(value)
                        elif (re.findall('\d+', value[-6:])):
                            print("NDB id")
                            print(value[-4:])
                            print(value)

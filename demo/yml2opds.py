import argparse
import yaml
from catalog import Catalog, to_opds


def mimetype(entry):
    if entry['type'] == 'static-site':
        return 'application/zip+html'
    elif entry['type'] in ('zim', 'kiwix'):
        return 'application/zim'
    else:
        return 'application/unknown'


def yml_to_opds(yml_file, title, url, **options):
    catalog = Catalog(title=title, **options)
    with open(yml_file) as f:
        file_content = f.read()
    loaded = yaml.load(file_content)
    for (uuid, e) in loaded['all'].items():
        print e['version']
        catalog.add_entry(
            uuid=uuid,
            title=e['name'],
            issued=e['version'],
            urls={mimetype(e): e['url']},
            file_size=e['size'],
            checksum=e['sha256sum'],
            checksum_algorithm='sha256')

    return to_opds(catalog, url)


def main():
    description = 'Converts yaml files to opml.'
    parser = argparse.ArgumentParser(description=description)

    # Optional arguments. They will be derivated from the remote ones.
    parser.add_argument('--input',
                        help='Location of the yaml input file',
                        default='catalog.yml')

    parser.add_argument('--title',
                        help='Title of the OPDS feed',
                        default='A Random name')

    parser.add_argument('--url',
                        help='The URL where the catalog will be served at',
                        default="http://localhost:8000/catalog.opds")
    args = parser.parse_args()
    print(yml_to_opds(args.input, args.title, args.url))

if __name__ == "__main__":  # pragma: nocover
    main()

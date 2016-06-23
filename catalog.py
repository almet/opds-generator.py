import datetime
import os
from uuid import uuid4

from jinja2 import FileSystemLoader, Environment


HERE = os.path.dirname(__file__)


class Catalog(object):

    def __init__(self, title, packager_name, author_name=None,
                 author_uri=None):
        """Generates a catalog for the given passed data.

        Required parameters:

        :param title:
            The title of the catalog in human-readable form.
        :param packager_name:
            The name of the packager (most probably the entity running this
            script).

        Optional parameters:

        :param updated:
            A python date object describing when the OPDS has been
            generated (defaults to now).
        :param author_name:
            The name of the author.
        :param author_uri:
            An URI to retrieve more information about the author.
        """
        self.title = title
        self.packager_name = packager_name
        self.author_name = author_name
        self.author_uri = author_uri

    def add_entry(self, title, issued, urls, id=None, summary=None,
                  author_name=None, author_uri=None, checksum=None,
                  file_size=None, tags=None, requires_mimetypes=None,
                  image=None, thumbnail=None, languages=("eng", ),
                  checksum_algorithm="sha256"):
        """Adds an entry to the catalog.

        Required parameters:

        XXX: Should add this.
        A human readable identifier for the resource. It's the same
        across versions (should be stable across time).
        MUST be prefixed by the packager name.

        :param title:
            The title of the resource.
        :param issued:
            A python datetime object describing when the resource was issued by
            its producer.
        :param urls:
            A dictionary with MimeTypes as keys and URLs as values.

        Optional keys:

        :param id:
            A unique identifier for the resource. (defaults to a generated UUID
            if not specified).
        :param summary:
            The description of the resource.
        :param author_name:
            The name of the author.
        :param author_uri:
            An URI to retrieve more information about the author.
        :param languages:
            A list of ISO-639-3 (3 characters) languages the resource uses.
        :param checksum:
            The checksum of the resource (by default a sha2566 value should be
            provided)
        :param checksum_algorithm:
            The checksum algorithm to use (defaults to sha256).
        :param file_size:
            The size of the file, in bytes.
        :param tags:
            A list of tags (specified as text values)
        :param requires_mimetypes:
            A list of mimetypes that if not supported will prevent this
            content from being played.
        :param image:
            An URI to an image (large) representation of the content.
        :param thumbnail:
            An URI to a thumbnail (small) representation of the content.
        """
        self.entries.append(dict(
            title=title,
            issued=issued,
            urls=urls,
            id=id,
            summary=summary,
            author_name=author_name,
            author_uri=author_uri,
            checksum=checksum,
            file_size=file_size,
            tags=tags,
            requires_mimetypes=requires_mimetypes,
            image=image,
            thumbnail=thumbnail,
            languages=languages,
            checksum_algorithm=checksum_algorithm))


def export_as_opds(catalog, url=None, root_url=None, updated=None, uuid=None):
    """Exports the given catalog in the OPDS format.

    :param catalog:
        The catalog object.
    :param uuid:
        The unique id of the feed.
    :param updated:
        A python date object representing the feed generation time
        (defaults to now).
    :param url:
        Absolute URL of the current catalog.
    :param root_url:
        Absolute URL to the root catalog (defaults to the same value
        url is providing).
    """
    updated = updated or datetime.now()
    uuid = uuid or uuid4()
    root_url = root_url or url

    env = Environment(loader=FileSystemLoader(HERE))
    template = env.get_template("catalog.opds.jinja2")
    return template.render(
        catalog=catalog,
        uuid=uuid,
        updated=updated,
        url=url,
        root_url=root_url)

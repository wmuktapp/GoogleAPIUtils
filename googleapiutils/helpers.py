import re

from googleapiclient import discovery
from oauth2client import client, file, tools
import httplib2


class DummyArgParser(object):
    """Dummy class that can be passed to the 4th argument for helpers.Service to enable click to manage the entry point args instead of argparse."""

    auth_host_name = "localhost"
    auth_host_port = [8080, 8090]
    logging_level = "ERROR"
    noauth_local_webserver = True


class Collection(object):
    def __init__(self, collection):
        self._collection = collection

    def __getattr__(self, name):
        return getattr(self._collection, name)

    def _find(self, partial, searchField, pattern, returnFirstResult=True):
        pageToken = None
        items = []
        matches = []
        r = re.compile(pattern)
        while pageToken != "":
            response = partial(pageToken=pageToken).execute()
            items = response["items"]
            for item in items:
                if r.match(item[sortFieldToProperty(searchField)]) is not None:
                    if returnFirstResult:
                        return item
                    matches.append(item)
            pageToken = response["nextPageToken"]
        return matches or None


class GoogleAPIUtilsError(Exception):
    pass


class Service(object):
    _SCOPES = ()
    _SERVICE_NAME = ""
    _SERVICE_VERSION = ""

    def __init__(self, pathToCredentialFile, clientId=None, clientSecret=None, flags=None, verify=False):
        storage = file.Storage(pathToCredentialFile)
        self.credentials = storage.get()
        if self.credentials is None or self.credentials.invalid:
            if clientId is None or clientSecret is None:
                raise GoogleAPIUtilsError("credentials were invalid and either clientId or clientSecret were not provided")
            self.credentials = tools.run_flow(client.OAuth2WebServerFlow(clientId, clientSecret, self._SCOPES), storage, flags or tools.argparser.parse_args())
        self._service = discovery.build(self._SERVICE_NAME, self._SERVICE_VERSION, http=self.credentials.authorize(httplib2.Http(disable_ssl_certificate_validation=not verify)))

    def __getattr__(self, name):
        return getattr(self._service, name)

    def newBatchHttpRequest(self, *args, **kwargs):
        return self._service.new_batch_http_request(*args, **kwargs)


def sortFieldToProperty(sortField):
    return re.sub(r"(?!^)_([a-zA-Z])", lambda m: m.group(1).upper(), sortField.lower())

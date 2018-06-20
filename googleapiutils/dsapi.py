from googleapiutils import helpers


class DSService(helpers.Service):
    _SCOPES = ("https://www.googleapis.com/auth/doubleclicksearch")
    _SERVICE_NAME = "doubleclicksearch"
    _SERVICE_VERSION = "v2"

from googleapiutils import helpers


class DBMService(helpers.Service):
    _SCOPES = ("https://www.googleapis.com/auth/doubleclickbidmanager")
    _SERVICE_NAME = "doubleclickbidmanager"
    _SERVICE_VERSION = "v1"

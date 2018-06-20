from googleapiutils import helpers


class SearchConsoleService(helpers.Service):
    _SCOPES = ("https://www.googleapis.com/auth/webmasters.readonly", "https://www.googleapis.com/auth/webmasters")
    _SERVICE_NAME = "webmasters"
    _SERVICE_VERSION = "v3"

    def searchanalytics(self, *args, **kwargs):
        return SearchAnalytics(self._service.searchanalytics(*args, **kwargs))


class SearchAnalytics(helpers.Collection):
    pass

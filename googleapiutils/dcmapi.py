import functools

from googleapiutils import helpers


class DCMService(helpers.Service):
    _SCOPES = ("https://www.googleapis.com/auth/dfatrafficking", "https://www.googleapis.com/auth/dfareporting",
               "https://www.googleapis.com/auth/ddmconversions")
    _SERVICE_NAME = "dfareporting"
    _SERVICE_VERSION = "v3.0"

    def reports(self, *args, **kwargs):
        return Reports(self._service.reports(*args, **kwargs))


class Reports(helpers.Collection):
    def find(self, profileId, searchField, pattern, maxResults=None, sortOrder=None, scope=None, fields=None, returnFirstResult=True):
        return self._find(functools.partial(self.list, profileId=profileId, maxResults=maxResults or 10, sortOrder=sortOrder, scope=scope,
                                            fields=fields), searchField, pattern, returnFirstResult)

    def files(self):
        return ReportsFiles(self._collection.files())


class ReportsFiles(helpers.Collection):
    def find(self, profileId, reportId, searchField, pattern, maxResults=None, sortOrder=None, scope=None, fields=None, returnFirstResult=True):
        return self._find(functools.partial(self.list, profileId=profileId, reportId=reportId, maxResults=maxResults or 10, sortOrder=sortOrder,
                                            scope=scope, fields=fields), searchField, pattern, returnFirstResult)

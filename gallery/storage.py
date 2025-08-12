from django.contrib.staticfiles.storage import StaticFilesStorage

class RelativeStaticFilesStorage(StaticFilesStorage):
    def url(self, name):
        url = super().url(name)
        if url.startswith('/'):
            return url[1:]
        return url

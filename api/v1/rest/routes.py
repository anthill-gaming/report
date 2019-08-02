# For more details about routing, see
# http://www.tornadoweb.org/en/stable/routing.html
from tornado.web import url
from . import handlers as h


route_patterns = [
    url(r'^/report/(?P<id>[^/]+)/?$', h.ReportHandler, name='report'),
    url(r'^/report/(?P<app_name>[^/]+)/(?P<app_version>[^/]+)/?$', h.ReportHandler, name='create_report'),
    url(r'^/reports/?$', h.ReportListHandler, name='reports'),
]

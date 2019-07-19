# For more details about routing, see
# http://www.tornadoweb.org/en/stable/routing.html
from tornado.web import url
from . import handlers


route_patterns = [
    url(r'^/report/(?P<id>[^/]+)/?$', handlers.ReportHandler, name='report'),
    url(r'^/report/(?P<app_name>[^/]+)/(?P<app_version>[^/]+)/?$', handlers.ReportHandler, name='create_report'),
    url(r'^/reports/?$', handlers.ReportListHandler, name='reports'),
]

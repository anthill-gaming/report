from anthill.platform.api.rest.handlers.edit import CreatingMixin, ModelFormHandler
from anthill.framework.utils.ip import get_ip
from report.models import Report
import json


class UploadReport(CreatingMixin, ModelFormHandler):
    model = Report

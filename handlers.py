from anthill.platform.api.rest.handlers.edit import CreatingMixin, ModelFormHandler
from anthill.framework.utils.ip import get_ip
from report.models import Report
import json


class CreateReportHandler(CreatingMixin, ModelFormHandler):
    model = Report

    def configure_object(self, form):
        super().configure_object(form)

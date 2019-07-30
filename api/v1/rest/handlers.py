from anthill.platform.api.rest.handlers.edit import CreatingMixin, DetailHandler, ModelFormHandler
from anthill.platform.api.rest.handlers.list import ListHandler
from anthill.framework.utils.ip import get_ip
from report.models import Report
import json


class ReportHandler(CreatingMixin, DetailHandler, ModelFormHandler):
    """
    Multiple operations with report items:
        fetching, creating.
    """
    model = Report

    def configure_object(self, form):
        super().configure_object(form)
        # customize self.object


class ReportListHandler(ListHandler):
    """Get report list."""
    model = Report

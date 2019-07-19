# For more details, see
# http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#declare-a-mapping
from anthill.framework.db import db
from anthill.framework.utils import timezone
from anthill.platform.api.internal import InternalAPIMixin
from anthill.platform.auth import RemoteUser
from sqlalchemy_utils.types import JSONType, ChoiceType, IPAddressType
import enum


class Report(InternalAPIMixin, db.Model):
    __tablename__ = 'reports'

    class Formats(enum.Enum):
        BINARY = 1
        JSON = 2
        TEXT = 3
        XML = 4

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    created = db.Column(db.DateTime, default=timezone.now)
    payload = db.Column(JSONType, nullable=False, default={})
    info = db.Column(JSONType, nullable=False, default={})
    ip_address = db.Column(IPAddressType)
    app_name = db.Column(db.String(64), nullable=False)
    app_version = db.Column(db.String(64), nullable=False)
    category = db.Column(db.String(64), nullable=False)
    message = db.Column(db.String(256), nullable=False)
    format = db.Column(ChoiceType(Formats, impl=db.Integer()), default=Formats.BINARY)

    async def get_user(self) -> RemoteUser:
        data = await self.internal_request('login', 'get_user', user_id=self.user_id)
        return RemoteUser(**data)

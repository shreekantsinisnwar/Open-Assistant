from oasst_backend.config import settings
from oasst_backend.exceptions import OasstError, OasstErrorCode
from sqlmodel import create_engine

if settings.DATABASE_URI is None:
    raise OasstError("DATABASE_URI is not set", error_code=OasstErrorCode.DATABASE_URI_NOT_SET)

engine = create_engine(settings.DATABASE_URI)

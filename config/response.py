from enum import Enum
from http import HTTPStatus


class Success(Enum):
    OK = HTTPStatus.OK


class ClientError(Enum):
    BAD_REQUEST = HTTPStatus.BAD_REQUEST

from ser_api.utils.config import CONFIG_ENV, config
from slowapi import Limiter
from slowapi.util import get_remote_address

default_minutely_limit = config[CONFIG_ENV].DEFAULT_MINUTELY_RATE_LIMIT
default_hourly_limit = config[CONFIG_ENV].DEFAULT_HOURLY_RATE_LIMIT

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=[default_minutely_limit, default_hourly_limit],
)

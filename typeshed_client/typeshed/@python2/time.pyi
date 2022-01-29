import sys
from typing import Any, NamedTuple

_TimeTuple = tuple[int, int, int, int, int, int, int, int, int]

accept2dyear: bool
altzone: int
daylight: int
timezone: int
tzname: tuple[str, str]

class _struct_time(NamedTuple):
    tm_year: int
    tm_mon: int
    tm_mday: int
    tm_hour: int
    tm_min: int
    tm_sec: int
    tm_wday: int
    tm_yday: int
    tm_isdst: int
    @property
    def n_fields(self) -> int: ...
    @property
    def n_sequence_fields(self) -> int: ...
    @property
    def n_unnamed_fields(self) -> int: ...

class struct_time(_struct_time):
    def __init__(self, o: _TimeTuple, _arg: Any = ...) -> None: ...
    def __new__(cls, o: _TimeTuple, _arg: Any = ...) -> struct_time: ...

def asctime(t: _TimeTuple | struct_time = ...) -> str: ...
def clock() -> float: ...
def ctime(secs: float | None = ...) -> str: ...
def gmtime(secs: float | None = ...) -> struct_time: ...
def localtime(secs: float | None = ...) -> struct_time: ...
def mktime(t: _TimeTuple | struct_time) -> float: ...
def sleep(secs: float) -> None: ...
def strftime(format: str, t: _TimeTuple | struct_time = ...) -> str: ...
def strptime(string: str, format: str = ...) -> struct_time: ...
def time() -> float: ...

if sys.platform != "win32":
    def tzset() -> None: ...  # Unix only

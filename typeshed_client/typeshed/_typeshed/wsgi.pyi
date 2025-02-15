# Types to support PEP 3333 (WSGI)
#
# Obsolete since Python 3.11: Use wsgiref.types instead.
#
# See the README.md file in this directory for more information.

import sys
from _typeshed import OptExcInfo
from typing import Any, Callable, Iterable, Protocol
from typing_extensions import TypeAlias

class _Readable(Protocol):
    def read(self, size: int = ...) -> bytes: ...
    # Optional: def close(self) -> object: ...

if sys.version_info >= (3, 11):
    from wsgiref.types import *
else:
    # stable
    class StartResponse(Protocol):
        def __call__(
            self, __status: str, __headers: list[tuple[str, str]], __exc_info: OptExcInfo | None = ...
        ) -> Callable[[bytes], object]: ...

    WSGIEnvironment: TypeAlias = dict[str, Any]  # stable
    WSGIApplication: TypeAlias = Callable[[WSGIEnvironment, StartResponse], Iterable[bytes]]  # stable

    # WSGI input streams per PEP 3333, stable
    class InputStream(Protocol):
        def read(self, __size: int = ...) -> bytes: ...
        def readline(self, __size: int = ...) -> bytes: ...
        def readlines(self, __hint: int = ...) -> list[bytes]: ...
        def __iter__(self) -> Iterable[bytes]: ...

    # WSGI error streams per PEP 3333, stable
    class ErrorStream(Protocol):
        def flush(self) -> object: ...
        def write(self, __s: str) -> object: ...
        def writelines(self, __seq: list[str]) -> object: ...

    # Optional file wrapper in wsgi.file_wrapper
    class FileWrapper(Protocol):
        def __call__(self, __file: _Readable, __block_size: int = ...) -> Iterable[bytes]: ...

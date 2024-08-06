from collections.abc import Callable
from collections.abc import Iterable
from collections.abc import Mapping
from typing import Literal
from typing import TypeVar

from .mixins import ImmutableDictMixin
from .mixins import UpdateDictMixin

T = TypeVar("T")
_CPT = TypeVar("_CPT", str, int, bool)

def cache_control_property(
    key: str, empty: _CPT | None, type: type[_CPT]
) -> property: ...

class _CacheControl(
    UpdateDictMixin[str, str | int | bool | None], dict[str, str | int | bool | None]
):
    provided: bool
    def __init__(
        self,
        values: Mapping[str, str | int | bool | None]
        | Iterable[tuple[str, str | int | bool | None]] = (),
        on_update: Callable[[_CacheControl], None] | None = None,
    ) -> None: ...
    @property
    def no_cache(self) -> str | None: ...
    @no_cache.setter
    def no_cache(self, value: Literal[True] | str | None) -> None: ...
    @no_cache.deleter
    def no_cache(self) -> None: ...
    @property
    def no_store(self) -> bool: ...
    @no_store.setter
    def no_store(self, value: bool | None) -> None: ...
    @no_store.deleter
    def no_store(self) -> None: ...
    @property
    def max_age(self) -> int | None: ...
    @max_age.setter
    def max_age(self, value: int | None) -> None: ...
    @max_age.deleter
    def max_age(self) -> None: ...
    @property
    def no_transform(self) -> bool: ...
    @no_transform.setter
    def no_transform(self, value: bool | None) -> None: ...
    @no_transform.deleter
    def no_transform(self) -> None: ...
    def _get_cache_value(self, key: str, empty: T | None, type: type[T]) -> T: ...
    def _set_cache_value(self, key: str, value: T | None, type: type[T]) -> None: ...
    def _del_cache_value(self, key: str) -> None: ...
    def to_header(self) -> str: ...
    @staticmethod
    def cache_property(key: str, empty: _CPT | None, type: type[_CPT]) -> property: ...

class RequestCacheControl(  # type: ignore[misc]
    ImmutableDictMixin[str, str | int | bool | None], _CacheControl
):
    @property  # type: ignore
    def no_cache(self) -> str | None: ...
    @property  # type: ignore
    def no_store(self) -> bool: ...
    @property  # type: ignore
    def max_age(self) -> int | None: ...
    @property  # type: ignore
    def no_transform(self) -> bool: ...
    @property
    def max_stale(self) -> int | Literal["*"] | None: ...
    @property
    def min_fresh(self) -> int | None: ...
    @property
    def only_if_cached(self) -> bool | None: ...

class ResponseCacheControl(_CacheControl):
    @property
    def public(self) -> bool: ...
    @public.setter
    def public(self, value: bool | None) -> None: ...
    @public.deleter
    def public(self) -> None: ...
    @property
    def private(self) -> str | None: ...
    @private.setter
    def private(self, value: Literal[True] | str | None) -> None: ...
    @private.deleter
    def private(self) -> None: ...
    @property
    def must_revalidate(self) -> bool: ...
    @must_revalidate.setter
    def must_revalidate(self, value: bool | None) -> None: ...
    @must_revalidate.deleter
    def must_revalidate(self) -> None: ...
    @property
    def proxy_revalidate(self) -> bool: ...
    @proxy_revalidate.setter
    def proxy_revalidate(self, value: bool | None) -> None: ...
    @proxy_revalidate.deleter
    def proxy_revalidate(self) -> None: ...
    @property
    def s_maxage(self) -> int | None: ...
    @s_maxage.setter
    def s_maxage(self, value: int | None) -> None: ...
    @s_maxage.deleter
    def s_maxage(self) -> None: ...
    @property
    def immutable(self) -> bool: ...
    @immutable.setter
    def immutable(self, value: bool | None) -> None: ...
    @immutable.deleter
    def immutable(self) -> None: ...
    @property
    def must_understand(self) -> bool: ...
    @must_understand.setter
    def must_understand(self, value: bool | None) -> None: ...
    @must_understand.deleter
    def must_understand(self) -> None: ...

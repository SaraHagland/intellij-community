from typing import Any, overload, Union
from os import PathLike

def baz(akjlkgjdfsakglkd: PathLike) -> None:
    pass

baz("foo<caret>")


def bar(akjlkgjdfsakglkd: Union[str, PathLike]) -> None:
    pass

bar("foo<caret>")


@overload
def foo(akjlkgjdfsakglkd: str) -> None:
    pass

@overload
def foo(akjlkgjdfsakglkd: PathLike) -> None:
    pass

def foo(akjlkgjdfsakglkd):
    pass

foo("foo<caret>")


def qux(akjlkgjdfsakglkd: Union[str, Any]) -> None:
    pass

qux("foo<caret>")


@overload
def quux(akjlkgjdfsakglkd: Any) -> None:
    pass

@overload
def quux(akjlkgjdfsakglkd: str) -> None:
    pass

def quux(akjlkgjdfsakglkd):
    pass

quux("foo<caret>")
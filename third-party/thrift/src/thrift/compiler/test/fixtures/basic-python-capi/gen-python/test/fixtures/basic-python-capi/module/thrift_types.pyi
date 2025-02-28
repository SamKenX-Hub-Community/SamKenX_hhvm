#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations


import typing as _typing

import enum

import folly.iobuf as _fbthrift_iobuf
import thrift.python.types as _fbthrift_python_types
import thrift.python.exceptions as _fbthrift_python_exceptions

import apache.thrift.op.patch.thrift_types

import thrift.test.python_capi.thrift_dep.thrift_types


class MyEnum(_fbthrift_python_types.Enum, int):
    MyValue1: MyEnum = ...
    MyValue2: MyEnum = ...
    def _to_python(self) -> MyEnum: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyEnum": ...  # type: ignore
    def _to_py_deprecated(self) -> int: ...


class AnnoyingEnum(_fbthrift_python_types.Enum, int):
    FOO: AnnoyingEnum = ...
    BAR: AnnoyingEnum = ...
    def _to_python(self) -> AnnoyingEnum: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.AnnoyingEnum": ...  # type: ignore
    def _to_py_deprecated(self) -> int: ...


class MyStruct(_fbthrift_python_types.Struct):
    inty: _typing.Final[int] = ...
    stringy: _typing.Final[str] = ...
    myItemy: _typing.Final[MyDataItem] = ...
    myEnumy: _typing.Final[MyEnum] = ...
    booly: _typing.Final[bool] = ...
    floatListy: _typing.Final[_typing.Sequence[float]] = ...
    strMappy: _typing.Final[_typing.Mapping[bytes, str]] = ...
    intSetty: _typing.Final[_typing.AbstractSet[int]] = ...
    def __init__(
        self, *,
        inty: _typing.Optional[int]=...,
        stringy: _typing.Optional[str]=...,
        myItemy: _typing.Optional[MyDataItem]=...,
        myEnumy: _typing.Optional[MyEnum]=...,
        booly: _typing.Optional[bool]=...,
        floatListy: _typing.Optional[_typing.Sequence[float]]=...,
        strMappy: _typing.Optional[_typing.Mapping[bytes, str]]=...,
        intSetty: _typing.Optional[_typing.AbstractSet[int]]=...
    ) -> None: ...

    def __call__(
        self, *,
        inty: _typing.Optional[int]=...,
        stringy: _typing.Optional[str]=...,
        myItemy: _typing.Optional[MyDataItem]=...,
        myEnumy: _typing.Optional[MyEnum]=...,
        booly: _typing.Optional[bool]=...,
        floatListy: _typing.Optional[_typing.Sequence[float]]=...,
        strMappy: _typing.Optional[_typing.Mapping[bytes, str]]=...,
        intSetty: _typing.Optional[_typing.AbstractSet[int]]=...
    ) -> MyStruct: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, str, MyDataItem, MyEnum, bool, _typing.Sequence[float], _typing.Mapping[bytes, str], _typing.AbstractSet[int]]]]: ...
    def _to_python(self) -> MyStruct: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStruct": ...  # type: ignore


class MyDataItem(_fbthrift_python_types.Struct):
    s: _typing.Final[str] = ...
    def __init__(
        self, *,
        s: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        s: _typing.Optional[str]=...
    ) -> MyDataItem: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    def _to_python(self) -> MyDataItem: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyDataItem": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyDataItem": ...  # type: ignore


class TransitiveDoubler(_fbthrift_python_types.Struct):
    def __init__(
        self,
    ) -> None: ...

    def __call__(
        self,
    ) -> TransitiveDoubler: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[None]]]: ...
    def _to_python(self) -> TransitiveDoubler: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.TransitiveDoubler": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.TransitiveDoubler": ...  # type: ignore


class DoubledPair(_fbthrift_python_types.Struct):
    s: _typing.Final[str] = ...
    x: _typing.Final[int] = ...
    def __init__(
        self, *,
        s: _typing.Optional[str]=...,
        x: _typing.Optional[int]=...
    ) -> None: ...

    def __call__(
        self, *,
        s: _typing.Optional[str]=...,
        x: _typing.Optional[int]=...
    ) -> DoubledPair: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, int]]]: ...
    def _to_python(self) -> DoubledPair: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.DoubledPair": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.DoubledPair": ...  # type: ignore


class StringPair(_fbthrift_python_types.Struct):
    normal: _typing.Final[str] = ...
    doubled: _typing.Final[str] = ...
    def __init__(
        self, *,
        normal: _typing.Optional[str]=...,
        doubled: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        normal: _typing.Optional[str]=...,
        doubled: _typing.Optional[str]=...
    ) -> StringPair: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, str]]]: ...
    def _to_python(self) -> StringPair: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.StringPair": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.StringPair": ...  # type: ignore


class EmptyStruct(_fbthrift_python_types.Struct):
    def __init__(
        self,
    ) -> None: ...

    def __call__(
        self,
    ) -> EmptyStruct: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[None]]]: ...
    def _to_python(self) -> EmptyStruct: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.EmptyStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.EmptyStruct": ...  # type: ignore


class PrimitiveStruct(_fbthrift_python_types.Struct):
    booly: _typing.Final[bool] = ...
    charry: _typing.Final[int] = ...
    shorty: _typing.Final[int] = ...
    inty: _typing.Final[int] = ...
    longy: _typing.Final[int] = ...
    floaty: _typing.Final[_typing.Optional[float]] = ...
    dubby: _typing.Final[_typing.Optional[float]] = ...
    stringy: _typing.Final[_typing.Optional[str]] = ...
    bytey: _typing.Final[_typing.Optional[bytes]] = ...
    def __init__(
        self, *,
        booly: _typing.Optional[bool]=...,
        charry: _typing.Optional[int]=...,
        shorty: _typing.Optional[int]=...,
        inty: _typing.Optional[int]=...,
        longy: _typing.Optional[int]=...,
        floaty: _typing.Optional[float]=...,
        dubby: _typing.Optional[float]=...,
        stringy: _typing.Optional[str]=...,
        bytey: _typing.Optional[bytes]=...
    ) -> None: ...

    def __call__(
        self, *,
        booly: _typing.Optional[bool]=...,
        charry: _typing.Optional[int]=...,
        shorty: _typing.Optional[int]=...,
        inty: _typing.Optional[int]=...,
        longy: _typing.Optional[int]=...,
        floaty: _typing.Optional[float]=...,
        dubby: _typing.Optional[float]=...,
        stringy: _typing.Optional[str]=...,
        bytey: _typing.Optional[bytes]=...
    ) -> PrimitiveStruct: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[bool, int, int, int, int, float, float, str, bytes]]]: ...
    def _to_python(self) -> PrimitiveStruct: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.PrimitiveStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.PrimitiveStruct": ...  # type: ignore


class ListStruct(_fbthrift_python_types.Struct):
    boolz: _typing.Final[_typing.Sequence[bool]] = ...
    intz: _typing.Final[_typing.Optional[_typing.Sequence[int]]] = ...
    stringz: _typing.Final[_typing.Optional[_typing.Sequence[str]]] = ...
    encoded: _typing.Final[_typing.Sequence[bytes]] = ...
    uidz: _typing.Final[_typing.Sequence[int]] = ...
    matrix: _typing.Final[_typing.Sequence[_typing.Sequence[float]]] = ...
    ucharz: _typing.Final[_typing.Sequence[_typing.Sequence[int]]] = ...
    voxels: _typing.Final[_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]] = ...
    def __init__(
        self, *,
        boolz: _typing.Optional[_typing.Sequence[bool]]=...,
        intz: _typing.Optional[_typing.Sequence[int]]=...,
        stringz: _typing.Optional[_typing.Sequence[str]]=...,
        encoded: _typing.Optional[_typing.Sequence[bytes]]=...,
        uidz: _typing.Optional[_typing.Sequence[int]]=...,
        matrix: _typing.Optional[_typing.Sequence[_typing.Sequence[float]]]=...,
        ucharz: _typing.Optional[_typing.Sequence[_typing.Sequence[int]]]=...,
        voxels: _typing.Optional[_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]]=...
    ) -> None: ...

    def __call__(
        self, *,
        boolz: _typing.Optional[_typing.Sequence[bool]]=...,
        intz: _typing.Optional[_typing.Sequence[int]]=...,
        stringz: _typing.Optional[_typing.Sequence[str]]=...,
        encoded: _typing.Optional[_typing.Sequence[bytes]]=...,
        uidz: _typing.Optional[_typing.Sequence[int]]=...,
        matrix: _typing.Optional[_typing.Sequence[_typing.Sequence[float]]]=...,
        ucharz: _typing.Optional[_typing.Sequence[_typing.Sequence[int]]]=...,
        voxels: _typing.Optional[_typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]]=...
    ) -> ListStruct: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.Sequence[bool], _typing.Sequence[int], _typing.Sequence[str], _typing.Sequence[bytes], _typing.Sequence[int], _typing.Sequence[_typing.Sequence[float]], _typing.Sequence[_typing.Sequence[int]], _typing.Sequence[_typing.Sequence[_typing.Sequence[int]]]]]]: ...
    def _to_python(self) -> ListStruct: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.ListStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.ListStruct": ...  # type: ignore


class SetStruct(_fbthrift_python_types.Struct):
    enumz: _typing.Final[_typing.AbstractSet[MyEnum]] = ...
    intz: _typing.Final[_typing.Optional[_typing.AbstractSet[int]]] = ...
    binnaz: _typing.Final[_typing.Optional[_typing.AbstractSet[bytes]]] = ...
    encoded: _typing.Final[_typing.AbstractSet[bytes]] = ...
    uidz: _typing.Final[_typing.AbstractSet[int]] = ...
    charz: _typing.Final[_typing.AbstractSet[int]] = ...
    setz: _typing.Final[_typing.Sequence[_typing.AbstractSet[int]]] = ...
    def __init__(
        self, *,
        enumz: _typing.Optional[_typing.AbstractSet[MyEnum]]=...,
        intz: _typing.Optional[_typing.AbstractSet[int]]=...,
        binnaz: _typing.Optional[_typing.AbstractSet[bytes]]=...,
        encoded: _typing.Optional[_typing.AbstractSet[bytes]]=...,
        uidz: _typing.Optional[_typing.AbstractSet[int]]=...,
        charz: _typing.Optional[_typing.AbstractSet[int]]=...,
        setz: _typing.Optional[_typing.Sequence[_typing.AbstractSet[int]]]=...
    ) -> None: ...

    def __call__(
        self, *,
        enumz: _typing.Optional[_typing.AbstractSet[MyEnum]]=...,
        intz: _typing.Optional[_typing.AbstractSet[int]]=...,
        binnaz: _typing.Optional[_typing.AbstractSet[bytes]]=...,
        encoded: _typing.Optional[_typing.AbstractSet[bytes]]=...,
        uidz: _typing.Optional[_typing.AbstractSet[int]]=...,
        charz: _typing.Optional[_typing.AbstractSet[int]]=...,
        setz: _typing.Optional[_typing.Sequence[_typing.AbstractSet[int]]]=...
    ) -> SetStruct: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.AbstractSet[MyEnum], _typing.AbstractSet[int], _typing.AbstractSet[bytes], _typing.AbstractSet[bytes], _typing.AbstractSet[int], _typing.AbstractSet[int], _typing.Sequence[_typing.AbstractSet[int]]]]]: ...
    def _to_python(self) -> SetStruct: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.SetStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.SetStruct": ...  # type: ignore


class MapStruct(_fbthrift_python_types.Struct):
    enumz: _typing.Final[_typing.Mapping[MyEnum, str]] = ...
    intz: _typing.Final[_typing.Optional[_typing.Mapping[int, str]]] = ...
    binnaz: _typing.Final[_typing.Optional[_typing.Mapping[bytes, PrimitiveStruct]]] = ...
    encoded: _typing.Final[_typing.Mapping[str, float]] = ...
    flotz: _typing.Final[_typing.Mapping[int, float]] = ...
    map_list: _typing.Final[_typing.Sequence[_typing.Mapping[int, int]]] = ...
    list_map: _typing.Final[_typing.Mapping[int, _typing.Sequence[int]]] = ...
    fast_list_map: _typing.Final[_typing.Mapping[int, _typing.Sequence[float]]] = ...
    def __init__(
        self, *,
        enumz: _typing.Optional[_typing.Mapping[MyEnum, str]]=...,
        intz: _typing.Optional[_typing.Mapping[int, str]]=...,
        binnaz: _typing.Optional[_typing.Mapping[bytes, PrimitiveStruct]]=...,
        encoded: _typing.Optional[_typing.Mapping[str, float]]=...,
        flotz: _typing.Optional[_typing.Mapping[int, float]]=...,
        map_list: _typing.Optional[_typing.Sequence[_typing.Mapping[int, int]]]=...,
        list_map: _typing.Optional[_typing.Mapping[int, _typing.Sequence[int]]]=...,
        fast_list_map: _typing.Optional[_typing.Mapping[int, _typing.Sequence[float]]]=...
    ) -> None: ...

    def __call__(
        self, *,
        enumz: _typing.Optional[_typing.Mapping[MyEnum, str]]=...,
        intz: _typing.Optional[_typing.Mapping[int, str]]=...,
        binnaz: _typing.Optional[_typing.Mapping[bytes, PrimitiveStruct]]=...,
        encoded: _typing.Optional[_typing.Mapping[str, float]]=...,
        flotz: _typing.Optional[_typing.Mapping[int, float]]=...,
        map_list: _typing.Optional[_typing.Sequence[_typing.Mapping[int, int]]]=...,
        list_map: _typing.Optional[_typing.Mapping[int, _typing.Sequence[int]]]=...,
        fast_list_map: _typing.Optional[_typing.Mapping[int, _typing.Sequence[float]]]=...
    ) -> MapStruct: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.Mapping[MyEnum, str], _typing.Mapping[int, str], _typing.Mapping[bytes, PrimitiveStruct], _typing.Mapping[str, float], _typing.Mapping[int, float], _typing.Sequence[_typing.Mapping[int, int]], _typing.Mapping[int, _typing.Sequence[int]], _typing.Mapping[int, _typing.Sequence[float]]]]]: ...
    def _to_python(self) -> MapStruct: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MapStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MapStruct": ...  # type: ignore


class ComposeStruct(_fbthrift_python_types.Struct):
    enum_: _typing.Final[MyEnum] = ...
    renamed_: _typing.Final[AnnoyingEnum] = ...
    primitive: _typing.Final[PrimitiveStruct] = ...
    aliased: _typing.Final[ListStruct] = ...
    xenum: _typing.Final[thrift.test.python_capi.thrift_dep.thrift_types.DepEnum] = ...
    xstruct: _typing.Final[thrift.test.python_capi.thrift_dep.thrift_types.DepStruct] = ...
    friends: _typing.Final[_typing.Sequence[thrift.test.python_capi.thrift_dep.thrift_types.DepStruct]] = ...
    def __init__(
        self, *,
        enum_: _typing.Optional[MyEnum]=...,
        renamed_: _typing.Optional[AnnoyingEnum]=...,
        primitive: _typing.Optional[PrimitiveStruct]=...,
        aliased: _typing.Optional[ListStruct]=...,
        xenum: _typing.Optional[thrift.test.python_capi.thrift_dep.thrift_types.DepEnum]=...,
        xstruct: _typing.Optional[thrift.test.python_capi.thrift_dep.thrift_types.DepStruct]=...,
        friends: _typing.Optional[_typing.Sequence[thrift.test.python_capi.thrift_dep.thrift_types.DepStruct]]=...
    ) -> None: ...

    def __call__(
        self, *,
        enum_: _typing.Optional[MyEnum]=...,
        renamed_: _typing.Optional[AnnoyingEnum]=...,
        primitive: _typing.Optional[PrimitiveStruct]=...,
        aliased: _typing.Optional[ListStruct]=...,
        xenum: _typing.Optional[thrift.test.python_capi.thrift_dep.thrift_types.DepEnum]=...,
        xstruct: _typing.Optional[thrift.test.python_capi.thrift_dep.thrift_types.DepStruct]=...,
        friends: _typing.Optional[_typing.Sequence[thrift.test.python_capi.thrift_dep.thrift_types.DepStruct]]=...
    ) -> ComposeStruct: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[MyEnum, AnnoyingEnum, PrimitiveStruct, ListStruct, thrift.test.python_capi.thrift_dep.thrift_types.DepEnum, thrift.test.python_capi.thrift_dep.thrift_types.DepStruct, _typing.Sequence[thrift.test.python_capi.thrift_dep.thrift_types.DepStruct]]]]: ...
    def _to_python(self) -> ComposeStruct: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.ComposeStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.ComposeStruct": ...  # type: ignore


class Onion(_fbthrift_python_types.Union):
    myEnum: _typing.Final[MyEnum] = ...
    myStruct: _typing.Final[PrimitiveStruct] = ...
    myString: _typing.Final[str] = ...
    intSet: _typing.Final[_typing.AbstractSet[int]] = ...
    doubleList: _typing.Final[_typing.Sequence[float]] = ...
    strMap: _typing.Final[_typing.Mapping[bytes, str]] = ...
    def __init__(
        self, *,
        myEnum: _typing.Optional[MyEnum]=...,
        myStruct: _typing.Optional[PrimitiveStruct]=...,
        myString: _typing.Optional[str]=...,
        intSet: _typing.Optional[_typing.AbstractSet[int]]=...,
        doubleList: _typing.Optional[_typing.Sequence[float]]=...,
        strMap: _typing.Optional[_typing.Mapping[bytes, str]]=...
    ) -> None: ...


    class Type(enum.Enum):
        EMPTY: Onion.Type = ...
        myEnum: Onion.Type = ...
        myStruct: Onion.Type = ...
        myString: Onion.Type = ...
        intSet: Onion.Type = ...
        doubleList: Onion.Type = ...
        strMap: Onion.Type = ...

    @classmethod
    def fromValue(cls, value: _typing.Union[None, MyEnum, PrimitiveStruct, str, _typing.AbstractSet[int], _typing.Sequence[float], _typing.Mapping[bytes, str]]) -> Onion: ...
    value: _typing.Final[_typing.Union[None, MyEnum, PrimitiveStruct, str, _typing.AbstractSet[int], _typing.Sequence[float], _typing.Mapping[bytes, str]]]
    type: Type
    def get_type(self) -> Type:...
    def _to_python(self) -> Onion: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.Onion": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.Onion": ...  # type: ignore


class MyStructPatch(_fbthrift_python_types.Struct):
    assign: _typing.Final[_typing.Optional[MyStruct]] = ...
    clear: _typing.Final[bool] = ...
    patchPrior: _typing.Final[MyStructFieldPatch] = ...
    ensure: _typing.Final[MyStructEnsureStruct] = ...
    patch: _typing.Final[MyStructFieldPatch] = ...
    remove: _typing.Final[_typing.Sequence[int]] = ...
    def __init__(
        self, *,
        assign: _typing.Optional[MyStruct]=...,
        clear: _typing.Optional[bool]=...,
        patchPrior: _typing.Optional[MyStructFieldPatch]=...,
        ensure: _typing.Optional[MyStructEnsureStruct]=...,
        patch: _typing.Optional[MyStructFieldPatch]=...,
        remove: _typing.Optional[_typing.Sequence[int]]=...
    ) -> None: ...

    def __call__(
        self, *,
        assign: _typing.Optional[MyStruct]=...,
        clear: _typing.Optional[bool]=...,
        patchPrior: _typing.Optional[MyStructFieldPatch]=...,
        ensure: _typing.Optional[MyStructEnsureStruct]=...,
        patch: _typing.Optional[MyStructFieldPatch]=...,
        remove: _typing.Optional[_typing.Sequence[int]]=...
    ) -> MyStructPatch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[MyStruct, bool, MyStructFieldPatch, MyStructEnsureStruct, MyStructFieldPatch, _typing.Sequence[int]]]]: ...
    def _to_python(self) -> MyStructPatch: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyStructPatch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStructPatch": ...  # type: ignore


class MyStructField4Patch(_fbthrift_python_types.Struct):
    assign: _typing.Final[_typing.Optional[MyEnum]] = ...
    clear: _typing.Final[bool] = ...
    def __init__(
        self, *,
        assign: _typing.Optional[MyEnum]=...,
        clear: _typing.Optional[bool]=...
    ) -> None: ...

    def __call__(
        self, *,
        assign: _typing.Optional[MyEnum]=...,
        clear: _typing.Optional[bool]=...
    ) -> MyStructField4Patch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[MyEnum, bool]]]: ...
    def _to_python(self) -> MyStructField4Patch: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyStructField4Patch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStructField4Patch": ...  # type: ignore


class MyStructField6Patch(_fbthrift_python_types.Struct):
    assign: _typing.Final[_typing.Optional[_typing.Sequence[float]]] = ...
    clear: _typing.Final[bool] = ...
    prepend: _typing.Final[_typing.Sequence[float]] = ...
    append: _typing.Final[_typing.Sequence[float]] = ...
    def __init__(
        self, *,
        assign: _typing.Optional[_typing.Sequence[float]]=...,
        clear: _typing.Optional[bool]=...,
        prepend: _typing.Optional[_typing.Sequence[float]]=...,
        append: _typing.Optional[_typing.Sequence[float]]=...
    ) -> None: ...

    def __call__(
        self, *,
        assign: _typing.Optional[_typing.Sequence[float]]=...,
        clear: _typing.Optional[bool]=...,
        prepend: _typing.Optional[_typing.Sequence[float]]=...,
        append: _typing.Optional[_typing.Sequence[float]]=...
    ) -> MyStructField6Patch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.Sequence[float], bool, _typing.Sequence[float], _typing.Sequence[float]]]]: ...
    def _to_python(self) -> MyStructField6Patch: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyStructField6Patch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStructField6Patch": ...  # type: ignore


class MyStructField7Patch(_fbthrift_python_types.Struct):
    assign: _typing.Final[_typing.Optional[_typing.Mapping[bytes, str]]] = ...
    clear: _typing.Final[bool] = ...
    patchPrior: _typing.Final[_typing.Mapping[bytes, apache.thrift.op.patch.thrift_types.StringPatch]] = ...
    add: _typing.Final[_typing.Mapping[bytes, str]] = ...
    patch: _typing.Final[_typing.Mapping[bytes, apache.thrift.op.patch.thrift_types.StringPatch]] = ...
    remove: _typing.Final[_typing.AbstractSet[bytes]] = ...
    put: _typing.Final[_typing.Mapping[bytes, str]] = ...
    def __init__(
        self, *,
        assign: _typing.Optional[_typing.Mapping[bytes, str]]=...,
        clear: _typing.Optional[bool]=...,
        patchPrior: _typing.Optional[_typing.Mapping[bytes, apache.thrift.op.patch.thrift_types.StringPatch]]=...,
        add: _typing.Optional[_typing.Mapping[bytes, str]]=...,
        patch: _typing.Optional[_typing.Mapping[bytes, apache.thrift.op.patch.thrift_types.StringPatch]]=...,
        remove: _typing.Optional[_typing.AbstractSet[bytes]]=...,
        put: _typing.Optional[_typing.Mapping[bytes, str]]=...
    ) -> None: ...

    def __call__(
        self, *,
        assign: _typing.Optional[_typing.Mapping[bytes, str]]=...,
        clear: _typing.Optional[bool]=...,
        patchPrior: _typing.Optional[_typing.Mapping[bytes, apache.thrift.op.patch.thrift_types.StringPatch]]=...,
        add: _typing.Optional[_typing.Mapping[bytes, str]]=...,
        patch: _typing.Optional[_typing.Mapping[bytes, apache.thrift.op.patch.thrift_types.StringPatch]]=...,
        remove: _typing.Optional[_typing.AbstractSet[bytes]]=...,
        put: _typing.Optional[_typing.Mapping[bytes, str]]=...
    ) -> MyStructField7Patch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.Mapping[bytes, str], bool, _typing.Mapping[bytes, apache.thrift.op.patch.thrift_types.StringPatch], _typing.Mapping[bytes, str], _typing.Mapping[bytes, apache.thrift.op.patch.thrift_types.StringPatch], _typing.AbstractSet[bytes], _typing.Mapping[bytes, str]]]]: ...
    def _to_python(self) -> MyStructField7Patch: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyStructField7Patch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStructField7Patch": ...  # type: ignore


class MyStructField8Patch(_fbthrift_python_types.Struct):
    assign: _typing.Final[_typing.Optional[_typing.AbstractSet[int]]] = ...
    clear: _typing.Final[bool] = ...
    remove: _typing.Final[_typing.AbstractSet[int]] = ...
    add: _typing.Final[_typing.AbstractSet[int]] = ...
    def __init__(
        self, *,
        assign: _typing.Optional[_typing.AbstractSet[int]]=...,
        clear: _typing.Optional[bool]=...,
        remove: _typing.Optional[_typing.AbstractSet[int]]=...,
        add: _typing.Optional[_typing.AbstractSet[int]]=...
    ) -> None: ...

    def __call__(
        self, *,
        assign: _typing.Optional[_typing.AbstractSet[int]]=...,
        clear: _typing.Optional[bool]=...,
        remove: _typing.Optional[_typing.AbstractSet[int]]=...,
        add: _typing.Optional[_typing.AbstractSet[int]]=...
    ) -> MyStructField8Patch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.AbstractSet[int], bool, _typing.AbstractSet[int], _typing.AbstractSet[int]]]]: ...
    def _to_python(self) -> MyStructField8Patch: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyStructField8Patch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStructField8Patch": ...  # type: ignore


class MyStructFieldPatch(_fbthrift_python_types.Struct):
    inty: _typing.Final[apache.thrift.op.patch.thrift_types.I64Patch] = ...
    stringy: _typing.Final[apache.thrift.op.patch.thrift_types.StringPatch] = ...
    myItemy: _typing.Final[MyDataItemPatch] = ...
    myEnumy: _typing.Final[MyStructField4Patch] = ...
    booly: _typing.Final[apache.thrift.op.patch.thrift_types.BoolPatch] = ...
    floatListy: _typing.Final[MyStructField6Patch] = ...
    strMappy: _typing.Final[MyStructField7Patch] = ...
    intSetty: _typing.Final[MyStructField8Patch] = ...
    def __init__(
        self, *,
        inty: _typing.Optional[apache.thrift.op.patch.thrift_types.I64Patch]=...,
        stringy: _typing.Optional[apache.thrift.op.patch.thrift_types.StringPatch]=...,
        myItemy: _typing.Optional[MyDataItemPatch]=...,
        myEnumy: _typing.Optional[MyStructField4Patch]=...,
        booly: _typing.Optional[apache.thrift.op.patch.thrift_types.BoolPatch]=...,
        floatListy: _typing.Optional[MyStructField6Patch]=...,
        strMappy: _typing.Optional[MyStructField7Patch]=...,
        intSetty: _typing.Optional[MyStructField8Patch]=...
    ) -> None: ...

    def __call__(
        self, *,
        inty: _typing.Optional[apache.thrift.op.patch.thrift_types.I64Patch]=...,
        stringy: _typing.Optional[apache.thrift.op.patch.thrift_types.StringPatch]=...,
        myItemy: _typing.Optional[MyDataItemPatch]=...,
        myEnumy: _typing.Optional[MyStructField4Patch]=...,
        booly: _typing.Optional[apache.thrift.op.patch.thrift_types.BoolPatch]=...,
        floatListy: _typing.Optional[MyStructField6Patch]=...,
        strMappy: _typing.Optional[MyStructField7Patch]=...,
        intSetty: _typing.Optional[MyStructField8Patch]=...
    ) -> MyStructFieldPatch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[apache.thrift.op.patch.thrift_types.I64Patch, apache.thrift.op.patch.thrift_types.StringPatch, MyDataItemPatch, MyStructField4Patch, apache.thrift.op.patch.thrift_types.BoolPatch, MyStructField6Patch, MyStructField7Patch, MyStructField8Patch]]]: ...
    def _to_python(self) -> MyStructFieldPatch: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyStructFieldPatch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStructFieldPatch": ...  # type: ignore


class MyStructEnsureStruct(_fbthrift_python_types.Struct):
    inty: _typing.Final[_typing.Optional[int]] = ...
    stringy: _typing.Final[_typing.Optional[str]] = ...
    myItemy: _typing.Final[_typing.Optional[MyDataItem]] = ...
    myEnumy: _typing.Final[_typing.Optional[MyEnum]] = ...
    booly: _typing.Final[_typing.Optional[bool]] = ...
    floatListy: _typing.Final[_typing.Optional[_typing.Sequence[float]]] = ...
    strMappy: _typing.Final[_typing.Optional[_typing.Mapping[bytes, str]]] = ...
    intSetty: _typing.Final[_typing.Optional[_typing.AbstractSet[int]]] = ...
    def __init__(
        self, *,
        inty: _typing.Optional[int]=...,
        stringy: _typing.Optional[str]=...,
        myItemy: _typing.Optional[MyDataItem]=...,
        myEnumy: _typing.Optional[MyEnum]=...,
        booly: _typing.Optional[bool]=...,
        floatListy: _typing.Optional[_typing.Sequence[float]]=...,
        strMappy: _typing.Optional[_typing.Mapping[bytes, str]]=...,
        intSetty: _typing.Optional[_typing.AbstractSet[int]]=...
    ) -> None: ...

    def __call__(
        self, *,
        inty: _typing.Optional[int]=...,
        stringy: _typing.Optional[str]=...,
        myItemy: _typing.Optional[MyDataItem]=...,
        myEnumy: _typing.Optional[MyEnum]=...,
        booly: _typing.Optional[bool]=...,
        floatListy: _typing.Optional[_typing.Sequence[float]]=...,
        strMappy: _typing.Optional[_typing.Mapping[bytes, str]]=...,
        intSetty: _typing.Optional[_typing.AbstractSet[int]]=...
    ) -> MyStructEnsureStruct: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, str, MyDataItem, MyEnum, bool, _typing.Sequence[float], _typing.Mapping[bytes, str], _typing.AbstractSet[int]]]]: ...
    def _to_python(self) -> MyStructEnsureStruct: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyStructEnsureStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStructEnsureStruct": ...  # type: ignore


class MyDataItemPatch(_fbthrift_python_types.Struct):
    assign: _typing.Final[_typing.Optional[MyDataItem]] = ...
    clear: _typing.Final[bool] = ...
    patchPrior: _typing.Final[MyDataItemFieldPatch] = ...
    ensure: _typing.Final[MyDataItemEnsureStruct] = ...
    patch: _typing.Final[MyDataItemFieldPatch] = ...
    remove: _typing.Final[_typing.Sequence[int]] = ...
    def __init__(
        self, *,
        assign: _typing.Optional[MyDataItem]=...,
        clear: _typing.Optional[bool]=...,
        patchPrior: _typing.Optional[MyDataItemFieldPatch]=...,
        ensure: _typing.Optional[MyDataItemEnsureStruct]=...,
        patch: _typing.Optional[MyDataItemFieldPatch]=...,
        remove: _typing.Optional[_typing.Sequence[int]]=...
    ) -> None: ...

    def __call__(
        self, *,
        assign: _typing.Optional[MyDataItem]=...,
        clear: _typing.Optional[bool]=...,
        patchPrior: _typing.Optional[MyDataItemFieldPatch]=...,
        ensure: _typing.Optional[MyDataItemEnsureStruct]=...,
        patch: _typing.Optional[MyDataItemFieldPatch]=...,
        remove: _typing.Optional[_typing.Sequence[int]]=...
    ) -> MyDataItemPatch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[MyDataItem, bool, MyDataItemFieldPatch, MyDataItemEnsureStruct, MyDataItemFieldPatch, _typing.Sequence[int]]]]: ...
    def _to_python(self) -> MyDataItemPatch: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyDataItemPatch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyDataItemPatch": ...  # type: ignore


class MyDataItemFieldPatch(_fbthrift_python_types.Struct):
    s: _typing.Final[apache.thrift.op.patch.thrift_types.StringPatch] = ...
    def __init__(
        self, *,
        s: _typing.Optional[apache.thrift.op.patch.thrift_types.StringPatch]=...
    ) -> None: ...

    def __call__(
        self, *,
        s: _typing.Optional[apache.thrift.op.patch.thrift_types.StringPatch]=...
    ) -> MyDataItemFieldPatch: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[apache.thrift.op.patch.thrift_types.StringPatch]]]: ...
    def _to_python(self) -> MyDataItemFieldPatch: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyDataItemFieldPatch": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyDataItemFieldPatch": ...  # type: ignore


class MyDataItemEnsureStruct(_fbthrift_python_types.Struct):
    s: _typing.Final[_typing.Optional[str]] = ...
    def __init__(
        self, *,
        s: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        s: _typing.Optional[str]=...
    ) -> MyDataItemEnsureStruct: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    def _to_python(self) -> MyDataItemEnsureStruct: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyDataItemEnsureStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyDataItemEnsureStruct": ...  # type: ignore

signed_byte = int
ListAlias = ListStruct

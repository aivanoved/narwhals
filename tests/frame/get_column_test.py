from typing import Any

import pandas as pd
import pytest

import narwhals as nw


def test_get_column(constructor: Any) -> None:
    df = nw.from_native(constructor({"a": [1, 2], "b": [3, 4]}), eager_only=True)
    result = df.get_column("a")
    assert result.to_list() == [1, 2]
    assert result.name == "a"
    with pytest.raises(
        (KeyError, TypeError), match="Expected str|'int' object cannot be converted|0"
    ):
        # Check that trying to get a column by position is disallowed here.
        nw.from_native(df, eager_only=True).get_column(0)  # type: ignore[arg-type]


def test_non_string_name() -> None:
    df = pd.DataFrame({0: [1, 2]})
    result = nw.from_native(df, eager_only=True).get_column(0)  # type: ignore[arg-type]
    assert result.to_list() == [1, 2]
    assert result.name == 0  # type: ignore[comparison-overlap]
    with pytest.raises(TypeError, match="Expected str or slice"):
        # Check that getitem would have raised
        nw.from_native(df, eager_only=True)[0]  # type: ignore[call-overload]

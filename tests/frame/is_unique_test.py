from __future__ import annotations

from typing import Any

import numpy as np
import pytest

import narwhals.stable.v1 as nw


def test_is_unique(request: Any, constructor: Any) -> None:
    if "pyarrow_table" in str(constructor):
        request.applymarker(pytest.mark.xfail)
    data = {"a": [1, 3, 2], "b": [4, 4, 6], "z": [7.0, 8, 9]}
    df_raw = constructor(data)
    df = nw.from_native(df_raw, eager_only=True)
    result = nw.concat([df, df.head(1)]).is_unique()
    expected = np.array([False, True, True, False])
    assert (result.to_numpy() == expected).all()

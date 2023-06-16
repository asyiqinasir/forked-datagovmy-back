from typing import Dict, List, TypedDict, Any
from pydantic import BaseModel, validator, ValidationError, root_validator

## TODO: GeneralChartVariable - common fields for all variables, e.g. keys, null_vals


class GeneralChartVariables(BaseModel):
    """
    Commonly shared properties for all charts
    keys: used as keys in the resulted nested dictionary data
    values: columns that contain the actual values of chart data, e.g. y-values
    rename: dict
    """

    keys: list[str] = []
    value_columns: list[str] = None
    rename_cols: dict[str, str] = {}
    null_vals: str | int | None = None
    replace_vals: dict[str, str | int] = {}


class TimeseriesChartVariables(TypedDict):
    keys: List[str]
    values: List[str]


class TimeseriesChartVariables(GeneralChartVariables):
    DATE_RANGE: Any


class BarChartVariables(GeneralChartVariables):
    x: str
    y: list[str] | dict[str, str]


class LineChartVariables(GeneralChartVariables):
    x: str
    y: list[str]


class BarMeterVariables(GeneralChartVariables):
    axis_values: list[dict[str, str]]
    sub_keys: bool = False

    # FIXME: why not just dict[str,str]? why is list required?
    @validator("axis_values")
    def axis_values_pair_length(cls, v):
        for pair in v:
            if len(pair) != 1:
                raise ValueError(
                    f"Each dictionary in axis_values should only 1 key (not {len(pair)})"
                )
        return v


class SnapshotChartVariables(GeneralChartVariables):
    main_key: str
    replace_word: str
    data: Dict[str, list[str]]


class CustomChartVariables(GeneralChartVariables):
    pass


class ChoroplethChartVariables(TypedDict):
    x: str
    y: List[str]  # alow multiple y columns
    keys: List[str]  # filters


class MetricsTableVariables(TypedDict):
    keys: List[str]
    obj_attr: Dict[str, str]


class PyramidChartVariables(TypedDict):
    col_range: Dict[str, str]
    suffix: Dict[str, str]
    keys: str


class JitterChartVariables(TypedDict):
    keys: str
    id: str
    columns: Dict[str, List[str]]
    tooltip: bool


class HeatmapChartVariables(TypedDict):
    cols: List[str]
    id: str
    keys: List[str]
    null_values: str | int | None
    replace_vals: Dict[str, str | int]
    dict_rename: Dict[str, str]
    row_format: str
    operation: str


class HeatmapChartVariables(GeneralChartVariables):
    # id: str
    pass


class WaffleChartVariables(GeneralChartVariables):
    wanted: list[str]
    # groups: list[str] # replaced by keys for consistency
    dict_keys: list[str]
    data_arr: dict[str, dict | str]

    @validator("dict_keys")
    def dict_keys_length(cls, v):
        if len(v) != 2:
            raise ValueError(
                f"dict_keys must have exactly 2 elements, key col & val col (not {len(v)})"
            )
        return v


class LatLonVariables(TypedDict):
    keys: List[str]
    values: List[str]
    null_vals: str | int | None


class _SortValues(BaseModel):
    by: list[str]
    ascending: list[bool]

    @root_validator
    def sort_values_length(cls, values):
        by, asc = values.get("by", []), values.get("ascending", [])
        if len(by) != len(asc):
            raise ValueError(f"'by' and 'ascending' must be the same length")
        return values


class QueryValuesVariables(GeneralChartVariables):
    flat: bool = False
    columns: list[str] = []  # similar to keys
    sort_values: _SortValues = {}

import sys

import pytest

from ...wordcount import parse_args


def test_parse_args_uses_defaults(monkeypatch):
    # Simulate running “python -m homework” with no extra flags:
    monkeypatch.setattr(sys, "argv", ["homework"])
    input_folder, output_folder = parse_args()
    assert input_folder == "data/input/"
    assert output_folder == "data/output/"


@pytest.mark.parametrize(
    ("args", "expected"),
    [
        (["-i", "in/", "-o", "out/"], ("in/", "out/")),
        (["--input", "foo", "--output", "bar"], ("foo", "bar")),
    ],
)
def test_parse_args_custom_values(monkeypatch, args, expected):
    # Prepend the “program name” placeholder
    monkeypatch.setattr(sys, "argv", ["homework", *args])
    input_folder, output_folder = parse_args()
    assert (input_folder, output_folder) == expected

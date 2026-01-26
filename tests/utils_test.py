import importlib.metadata

import pytest
import typer

from typer_utils.utils import (
    error,
    get_project_name,
    get_project_version,
    get_pyproject_data,
    is_cmd_exists,
    version_callback,
)


def test_error():
    msg = error("hello world")
    assert isinstance(msg, str)
    typer.echo(msg)


def test_get_pyproject_data():
    data = get_pyproject_data()
    assert data
    assert data["project"]["name"] == "typer-utils"
    assert data["tool"]["hatch"]["build"]["targets"]["wheel"]["packages"][0] == "typer_utils"


def test_get_project_name():
    assert get_project_name() == "typer-utils"


def test_get_project_version():
    assert get_project_version()


def test_is_cmd_exists():
    assert is_cmd_exists("pwd")
    assert is_cmd_exists("ppwd") is False


def test_version_callback():
    with pytest.raises(TypeError):
        version_callback(True)  # type: ignore
    with pytest.raises(importlib.metadata.PackageNotFoundError):
        version_callback(True, module_name="example")
    try:
        version_callback(True, module_name="typer_utils")
    except typer.Exit as e:
        assert e.exit_code == 0

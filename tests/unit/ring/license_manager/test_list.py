# This file is part of HYDRA - cross-platform remote administration
# system for 1C:Enterprise (https://github.com/vbondarevsky/hydra_agent).
# Copyright (C) 2017  Vladimir Bondarevskiy.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import subprocess

import pytest

from tests.unit import success_result, fail_result


@pytest.mark.parametrize(
    "out, expected",
    [
        ("\n",
         []),
        ("332588056123456-8100123456\n",
         ["332588056123456-8100123456"]),
        ("332588056123456-8100123456\n173211456654321-800654321\n",
         ["332588056123456-8100123456", "173211456654321-800654321"])
    ],
    ids=["empty", "one", "few"]
)
def test_success(monkeypatch, license_manager, out, expected):
    monkeypatch.setattr(subprocess, "run", lambda args, **kwargs: success_result(args, out))
    assert license_manager.list() == expected


@pytest.mark.parametrize(
    "out, return_code, path",
    [
        (("Ошибка получения списка лицензий.\nПо причине: Ошибка при работе с хранилищем лицензий.\n"
          " По причине: Директория не найдена: \"/var/lic\".\n"), 1, "/var/lic"),
    ],
    ids=["wrong_path"]
)
def test_fail(monkeypatch, license_manager, out, return_code, path):
    monkeypatch.setattr(subprocess, "run", lambda args, **kwargs: fail_result(args, return_code, out))
    with pytest.raises(subprocess.CalledProcessError):
        license_manager.list(path=path)

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


import aiohttp.web

from hydra_agent import config
from hydra_agent.api.middleware.basic_auth import basic_auth
from hydra_agent.api.routes import build_route
from hydra_agent.api.routes import setup_routes


def run_server():
    app = aiohttp.web.Application(debug=config.api.debug, middlewares=[basic_auth([build_route("/registry")])])
    setup_routes(app)
    aiohttp.web.run_app(app, host=config.api.host, port=config.api.port)

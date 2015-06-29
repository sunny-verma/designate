# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# Author: Endre Karlson <endre.karlson@hp.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from oslo_config import cfg

CONF = cfg.CONF

CONF.register_group(cfg.OptGroup(
    name='service:zone_manager', title="Configuration for Zone Manager Service"
))

OPTS = [
    cfg.IntOpt('workers', default=None,
               help='Number of Zone Manager worker processes to spawn'),
    cfg.IntOpt('threads', default=1000,
               help='Number of Zone Manager greenthreads to spawn'),
]

CONF.register_opts(OPTS, group='service:zone_manager')
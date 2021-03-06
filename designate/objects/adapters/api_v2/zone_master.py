# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from oslo_log import log as logging

from designate.objects.adapters.api_v2 import base
from designate import objects
from designate import utils
LOG = logging.getLogger(__name__)


class ZoneMasterAPIv2Adapter(base.APIv2Adapter):

    ADAPTER_OBJECT = objects.ZoneMaster

    MODIFICATIONS = {
        'fields': {
            'value': {
                'read_only': False
            }
        },
        'options': {
            'links': False,
            'resource_name': 'domain_master',
            'collection_name': 'domain_masters',
        }
    }

    @classmethod
    def _render_object(cls, object, *arg, **kwargs):
        if object.port is 53:
            return object.host
        else:
            return "%(host)s:%(port)d" % object.to_dict()

    @classmethod
    def _parse_object(cls, value, object, *args, **kwargs):
        object.host, object.port = utils.split_host_port(value)
        return object


class ZoneMasterListAPIv2Adapter(base.APIv2Adapter):

    ADAPTER_OBJECT = objects.ZoneMasterList

    MODIFICATIONS = {
        'options': {
            'links': False,
            'resource_name': 'domain_master',
            'collection_name': 'domain_masters',
        }
    }

    @classmethod
    def _render_list(cls, list_object, *args, **kwargs):

        r_list = []

        for object in list_object:
            r_list.append(cls.get_object_adapter(
                cls.ADAPTER_FORMAT,
                object).render(cls.ADAPTER_FORMAT, object, *args, **kwargs))

        return r_list

    @classmethod
    def _parse_list(cls, values, output_object, *args, **kwargs):

        for value in values:
            # Add the object to the list
            output_object.append(
                # Get the right Adapter
                cls.get_object_adapter(
                    cls.ADAPTER_FORMAT,
                    # This gets the internal type of the list, and parses it
                    # We need to do `get_object_adapter` as we need a new
                    # instance of the Adapter
                    output_object.LIST_ITEM_TYPE()).parse(
                        value, output_object.LIST_ITEM_TYPE()))

        # Return the filled list
        return output_object

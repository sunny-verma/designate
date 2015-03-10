# Copyright (c) 2014 Rackspace Hosting
# All Rights Reserved.
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
from designate.objects import base


class Domain(base.DictObjectMixin, base.SoftDeleteObjectMixin,
             base.PersistentObjectMixin, base.DesignateObject):
    FIELDS = {
        'tenant_id': {
            'schema': {
                'type': 'string',
            },
            'immutable': True
        },
        'name': {
            'schema': {
                'type': 'string',
                'description': 'Zone name',
                'format': 'domainname',
                'maxLength': 255,
            },
            'immutable': True,
            'required': True
        },
        'email': {
            'schema': {
                'type': 'string',
                'description': 'Hostmaster email address',
                'format': 'email',
                'maxLength': 255
            },
            'required': True
        },
        'ttl': {
            'schema': {
                'type': ['integer', 'null'],
                'minimum': 0,
                'maximum': 2147483647
            },
        },
        'refresh': {
            'schema': {
                'type': 'integer',
                'minimum': 0,
                'maximum': 2147483647
            },
            'read_only': True
        },
        'retry': {
            'schema': {
                'type': 'integer',
                'minimum': 0,
                'maximum': 2147483647
            },
            'read_only': True
        },
        'expire': {
            'schema': {
                'type': 'integer',
                'minimum': 0,
                'maximum': 2147483647
            },
            'read_only': True
        },
        'minimum': {
            'schema': {
                'type': 'integer',
                'minimum': 0,
                'maximum': 2147483647
            },
            'read_only': True
        },
        'parent_domain_id': {
            'schema': {
                'type': 'string',
                'format': 'uuid'
            },
            'read_only': True
        },
        'serial': {
            'schema': {
                'type': 'integer',
                'minimum': 1,
                'maximum': 4294967295,
            },
            'read_only': True
        },
        'description': {
            'schema': {
                'type': ['string', 'null'],
                'maxLength': 160
            },
        },
        'status': {
            'schema': {
                'type': 'string',
                'enum': ['ACTIVE', 'PENDING', 'ERROR'],
            },
            'read_only': True,
        },
        'action': {
            'schema': {
                'type': 'string',
                'enum': ['CREATE', 'DELETE', 'UPDATE', 'NONE'],
            },
            'read_only': True
        },
        'pool_id': {
            'schema': {
                'type': 'string',
                'format': 'uuid',
            },
            'immutable': True,
        },
        'recordsets': {
            'relation': True,
            'relation_cls': 'RecordSetList'
        },
    }


class DomainList(base.ListObjectMixin, base.DesignateObject,
                 base.PagedListObjectMixin):
    LIST_ITEM_TYPE = Domain

===========
FloatingIPs
===========

In order to use the FloatingIPs functionality you will need to have a FloatingIP
associated to your project in Neutron.

Set  FloatingIP's PTR record
============================

.. rest_method::  POST /v2/reverse/floatingips/{region}:{floatingip_id}

Set a PTR record for the given FloatingIP. The domain if it does not exist
will be provisioned automatically.

Normal response codes: 202

Error response codes: 405,404,403,401,400,503


Request
-------

.. rest_parameters:: parameters.yaml

   - x-auth-token: x-auth-token
   - x-auth-all-projects: x-auth-all-projects
   - x-auth-sudo-project-id: x-auth-sudo-project-id
   - ptrdname: fptrd_name
   - description: fptr_description
   - ttl: fptr_ttl
   - region: region
   - floatingip_id: floatingip_id

Request Example
---------------

.. literalinclude:: samples/reverse_floatingips/set-ptr-record-request.json
   :language: javascript


Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id
   - id: fptr_id
   - ptrdname: fptrd_name
   - description: fptr_description
   - ttl: fptr_ttl
   - address: floatingip_address
   - status: status
   - action: action
   - links: links


Response Example
----------------

.. literalinclude:: samples/reverse_floatingips/ptr-record-response.json
   :language: javascript


Show FloatingIP's PTR record
============================

.. rest_method::  GET /v2/reverse/floatingips/{region}:{floatingip_id}

Shows a particular FloatingIP PTR

Normal response codes: 200

Error response codes: 405,404,403,401,400,503


Request
-------

.. rest_parameters:: parameters.yaml

   - x-auth-token: x-auth-token
   - x-auth-all-projects: x-auth-all-projects
   - x-auth-sudo-project-id: x-auth-sudo-project-id
   - region: region
   - floatingip_id: floatingip_id

Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id
   - id: fptr_id
   - ptrdname: fptrd_name
   - description: fptr_description
   - ttl: fptr_ttl
   - address: floatingip_address
   - status: status
   - action: action
   - links: links


Response Example
----------------

.. literalinclude:: samples/reverse_floatingips/ptr-record-response.json
   :language: javascript


List FloatingIP's PTR record
============================

.. rest_method::  GET /v2/reverse/floatingips

List FloatingIP PTR records

Normal response codes: 200

Error response codes: 405,404,403,401,400,503


Request
-------

.. rest_parameters:: parameters.yaml

   - x-auth-token: x-auth-token
   - x-auth-all-projects: x-auth-all-projects
   - x-auth-sudo-project-id: x-auth-sudo-project-id


Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id
   - id: fptr_id
   - ptrdname: fptrd_name
   - description: fptr_description
   - ttl: fptr_ttl
   - address: floatingip_address
   - status: status
   - action: action
   - links: links


Response Example
----------------

.. literalinclude:: samples/reverse_floatingips/list-ptr-record-response.json
   :language: javascript


Unset FloatingIP's PTR record
=============================

.. rest_method::  PATCH /v2/reverse/floatingips/{region}:{floatingip_id}

Unset the PTR record for a FloatingIP

Normal response codes: 202

Error response codes: 405,404,403,401,400,503


Request
-------

.. rest_parameters:: parameters.yaml

   - x-auth-token: x-auth-token
   - x-auth-all-projects: x-auth-all-projects
   - x-auth-sudo-project-id: x-auth-sudo-project-id
   - region: region
   - floatingip_id: floatingip_id


Request Example
---------------

.. literalinclude:: samples/reverse_floatingips/unset-ptr-record-request.json
   :language: javascript


Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id

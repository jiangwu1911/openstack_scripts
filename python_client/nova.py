import settings as settings
import utils as utils

import novaclient.v1_1.client as nvclient

nova = nvclient.Client(auth_url=settings.OPENSTACK_KEYSTONE_URL,
                       username=settings.OPENSTACK_USER,
                       api_key=settings.OPENSTACK_PASSWORD,
                       project_id=settings.OPENSTACK_TENANT_NAME,
                      )

print utils.dumpObj(nova)

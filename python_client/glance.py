import keystoneclient.v2_0.client as ksclient
import glanceclient.v2.client as glclient
import settings as settings
import utils as utils

keystone = ksclient.Client(auth_url = settings.OPENSTACK_KEYSTONE_URL,
                           username = settings.OPENSTACK_USER,
                           password = settings.OPENSTACK_PASSWORD,
                           tenant_name = settings.OPENSTACK_TENANT_NAME,
                           )
glance_endpoint = keystone.service_catalog.url_for(service_type='image')
glance = glclient.Client(glance_endpoint, token=keystone.auth_token)
print utils.dumpObj(glance)

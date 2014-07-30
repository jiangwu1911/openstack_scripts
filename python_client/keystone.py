import keystoneclient.v2_0.client as ksclient
import settings as settings

keystone = ksclient.Client(auth_url = settings.OPENSTACK_KEYSTONE_URL,
                           username = settings.OPENSTACK_USER,
                           password = settings.OPENSTACK_PASSWORD,
                           tenant_name = settings.OPENSTACK_TENANT_NAME,
                           )
print keystone.auth_token

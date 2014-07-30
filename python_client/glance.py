import keystoneclient.v2_0.client as ksclient
import glanceclient.v2.client as glclient
import novaclient.v1_1.client as nvclient
import settings as settings
from utils import dump


def list_image(glance):
    images = glance.images.list()
    return images


def get_image(glance, image_id):
    image = glance.images.get(image_id)
    return image


def upload_image(glance, image_file):
    image_name = "my_image_2"
    with open(image_file, 'rb') as fimage:
        image = glance.images.create(name=image_name, 
                                     #is_public="False", 
                                     disk_format="qcow2",
                                     container_format="bare",
                                    )
        glance.images.upload(image.id, fimage)
        return image


keystone = ksclient.Client(auth_url = settings.OPENSTACK_KEYSTONE_URL,
                           username = settings.OPENSTACK_USER,
                           password = settings.OPENSTACK_PASSWORD,
                           tenant_name = settings.OPENSTACK_TENANT_NAME,
                           )
glance_endpoint = keystone.service_catalog.url_for(service_type='image')
glance = glclient.Client(glance_endpoint, token=keystone.auth_token)

#images = list_image(glance)
#dump.dumpObjList(images)

#image_id = "91585914-e76a-463e-9502-3e8b5275ff63"
#image = show_image(glance, image_id)
#dump.dumpObj(image)

image_file = "/home/openstack/cirros-0.3.2-x86_64-disk.img"
image = upload_image(glance, image_file)
dump.dumpObj(image)


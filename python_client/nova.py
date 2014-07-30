import settings as settings
from utils import dump

import novaclient.v1_1.client as nvclient


def get_image_by_name(nova, image_name):
    image = nova.images.find(name=image_name)
    return image


def start_server(nova):
    image = nova.images.find(name='cirros')
    flavor = nova.flavors.find(name='m1.tiny')
    instance = nova.servers.create(name='vm1',
                                   image=image,
                                   flavor=flavor)
    return instance


def list_server(nova):
    servers = nova.servers.list()
    for server in servers:
        print_server(server)


def print_server(server):
    print("-"*35)
    print("server id: %s" % server.id)
    print("server name: %s" % server.name)
    print("server image: %s" % server.image)
    print("server flavour: %s" % server.flavor)
    print("server key name: %s" % server.key_name)
    print("user_id: %s" % server.user_id)
    print("-"*35)

    
#nova = nvclient.Client(auth_url=settings.OPENSTACK_KEYSTONE_URL,
##                       username=settings.OPENSTACK_USER,
#                       api_key=settings.OPENSTACK_PASSWORD,
#                       project_id=settings.OPENSTACK_TENANT_NAME,
#                      )

#print dump.dumpObj(nova)

#image = get_image_by_name(nova, "cirros")
#utils.dumpObj(image)

#instance = start_server(nova)
#utils.dumpObj(instance)

#list_server(nova)

from utils import pool
import threading
import time

def func1():
    nc = pool.get()
    time.sleep(2)
    pool.free(nc)  
    return

pool = pool.NovaConnectionPool()
t = [0 for i in range(10)]
for i in range(5):
    t[i] = threading.Thread(target=func1)
    t[i].start()

for i in range(5):
    t[i].join()

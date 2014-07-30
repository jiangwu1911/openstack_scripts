import time
import Queue
from abc import ABCMeta, abstractmethod


class PoolException(Exception):
    pass


class Pool(object):
    def __init__(self, max_active=5, init_size=0, conn_type='nova', **config):
        self.__freeConns = Queue.Queue(max_active)
        self.conn_type = conn_type
        self.config = config

        if init_size > max_active:
            init_size = max_active

        for i in range(init_size):
            self.free(self._create_conn())


    def __del__(self):
        print("__del__ Pool...")
        self.release()


    def release(self):
        print("release Pool...")
        while self.__freeConns and not self.__freeConns.empty():
            conn = self.get()
            conn = None
        self.__freeConns = None


    @abstractmethod  
    def _create_conn(self):
        pass


    def get(self, timeout=None):
        conn = None
        if self.__freeConns.empty():
            conn = self._create_conn()
        else:
            conn = self.__freeConns.get()
        return conn 

          
    def free(self, conn):
        if(self.__freeConns.full()):
            conn = None
            return
        self.__freeConns.put_nowait(conn) 
        print self.__freeConns.qsize() 


    def size(self):
        return self.__freeConns.qsize()


class NovaConnectionPool(Pool):
    def _create_conn(self):
        import novaclient.v1_1.client as nvclient
        import settings
        nova = nvclient.Client(auth_url=settings.OPENSTACK_KEYSTONE_URL,
                               username=settings.OPENSTACK_USER,
                               api_key=settings.OPENSTACK_PASSWORD,
                               project_id=settings.OPENSTACK_TENANT_NAME,
                              )
        return nova

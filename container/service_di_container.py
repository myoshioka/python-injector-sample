from injector import Module
from domain.engine import Engine


class ServiceDiContainer(Module):

    def __init__(self, service_name):
        self.service_class = service_name['class']

    def configure(self, binder):
        cls = self.import_cls(self.service_class)
        binder.bind(Engine, to=cls)

    def import_cls(self, cls_name):
        path_components = cls_name.split('.')
        module = __import__('.'.join(path_components[:-1]),
                            locals(),
                            globals(),
                            fromlist=path_components[-1:])
        return getattr(module, path_components[-1])

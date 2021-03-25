from injector import Injector, inject, Module
from domain.engine import Engine


class Car(object):

    @inject
    def __init__(self, engine: Engine):
        self._engine = engine

    def run(self):
        str_engine = self._engine.exec()
        return f'This is {str_engine}'

from abc import ABCMeta, abstractmethod


class Engine(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def exec(self) -> str:
        pass

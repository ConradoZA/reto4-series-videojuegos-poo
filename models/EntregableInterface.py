from abc import ABCMeta, abstractmethod


class EntregableInterface(metaclass=ABCMeta):

    @abstractmethod
    def entregar(self) -> None:
        pass

    @abstractmethod
    def prestar(self) -> None:
        pass

    @abstractmethod
    def estaPrestado(self) -> bool:
        pass

    @abstractmethod
    def compararCon(self, one_object: object) -> str:
        pass

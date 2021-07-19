from __future__ import annotations

from models.EntregableInterface import EntregableInterface
from models.ObjetoAlquilable import ObjetoAlquilable


class Serie(ObjetoAlquilable, EntregableInterface):
    _nr_temporadas = 0
    _creador = ""

    @property
    def temporadas(self) -> int:
        return self._nr_temporadas

    @property
    def creador(self) -> str:
        return self._creador

    @temporadas.setter
    def temporadas(self, seasons_nr: int) -> None:
        self._nr_temporadas = seasons_nr

    @creador.setter
    def creador(self, creator: str) -> None:
        self._creador = creator

    def __init__(self, title: str, genre: str, creator: str, seasons=3):
        super().__init__(title, genre)
        self._creador = creator
        self._nr_temporadas = seasons

    def __str__(self) -> str:
        print_all = f'Título: {self.titulo}\n' \
                    f'Creador: {self._creador}\n' \
                    f'Género: {self.genero}\n' \
                    f'Temporadas:{self._nr_temporadas}\n' \
                    f'Prestado?: {"sí" if self._prestado else "no"}'
        return print_all

    def entregar(self) -> None:
        self._prestado = False

    def prestar(self) -> None:
        self._prestado = True

    def estaPrestado(self) -> bool:
        return self._prestado

    def compararCon(self, serie: Serie) -> str:
        return "Mayor" if self._nr_temporadas > serie._nr_temporadas else "Iguales" \
            if self._nr_temporadas == serie._nr_temporadas else "Menor"

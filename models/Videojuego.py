from __future__ import annotations

from models.EntregableInterface import EntregableInterface
from models.ObjetoAlquilable import ObjetoAlquilable


class Videojuego(ObjetoAlquilable, EntregableInterface):
    _companya = ""
    _horas_estimadas = 0

    @property
    def company(self) -> str:
        return self._companya

    @property
    def horas(self) -> int:
        return self._horas_estimadas

    @company.setter
    def company(self, company: str) -> None:
        self._companya = company

    @horas.setter
    def horas(self, estimated_hours: int) -> None:
        self._horas_estimadas = estimated_hours

    def __init__(self, title: str, genre: str, company: str, estimated_hours=10):
        super().__init__(title, genre)
        self._companya = company
        self._horas_estimadas = estimated_hours

    def __str__(self) -> str:
        print_all = f'Título: {self.titulo}\n' \
                    f'Compañía: {self._companya}\n' \
                    f'Género: {self.genero}\n' \
                    f'Horas estimadas de juego:{self._horas_estimadas}\n' \
                    f'Prestado?: {"sí" if self._prestado else "no"}'
        return print_all

    def entregar(self) -> None:
        self._prestado = False

    def prestar(self) -> None:
        self._prestado = True

    def estaPrestado(self) -> bool:
        return self._prestado

    def compararCon(self, game: Videojuego) -> str:
        return "Mayor" if self._horas_estimadas > game._horas_estimadas else "Iguales" \
            if self._horas_estimadas == game._horas_estimadas else "Menor"

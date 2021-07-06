from __future__ import annotations

import random


class EntregableInterface:
    _titulo = ""
    _genero = ""
    _prestado = False

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def genero(self) -> str:
        return self.__genero

    @titulo.setter
    def titulo(self, title: str) -> None:
        self.__titulo = title

    @genero.setter
    def genero(self, genre: str) -> None:
        self.__genero = genre

    def __init__(self, title: str, genre: str) -> None:
        self.__titulo = title
        self.__genero = genre

    def entregar(self) -> None:
        self._prestado = False

    def prestar(self) -> None:
        self._prestado = True

    def isentregado(self) -> bool:
        return self._prestado

    def compareto(self, one_object: object) -> str:
        pass


class Serie(EntregableInterface):
    __nr_temporadas = 0
    __creador = ""

    @property
    def temporadas(self) -> int:
        return self.__nr_temporadas

    @property
    def creador(self) -> str:
        return self.__creador

    @temporadas.setter
    def temporadas(self, seasons_nr: int) -> None:
        self.__nr_temporadas = seasons_nr

    @creador.setter
    def creador(self, creator: str) -> None:
        self.__creador = creator

    def __init__(self, title: str, genre: str, creator: str, seasons=3):
        super().__init__(title, genre)
        self.__creador = creator
        self.__nr_temporadas = seasons

    def __str__(self) -> str:
        print_all = f'Título: {self.titulo}\n' \
                    f'Creador: {self.__creador}\n' \
                    f'Género: {self.genero}\n' \
                    f'Temporadas:{self.__nr_temporadas}\n' \
                    f'Prestado?: {"sí" if self._prestado else "no"}'
        return print_all

    def compareto(self, serie: Serie) -> str:
        return "Mayor" if self.__nr_temporadas > serie.__nr_temporadas else "Iguales" \
            if self.__nr_temporadas == serie.__nr_temporadas else "Menor"


class Videojuego(EntregableInterface):
    __companya = ""
    __horas_estimadas = 0

    @property
    def company(self) -> str:
        return self.__companya

    @property
    def horas(self) -> int:
        return self.__horas_estimadas

    @company.setter
    def company(self, company: str) -> None:
        self.__companya = company

    @horas.setter
    def horas(self, estimated_hours: int) -> None:
        self.__horas_estimadas = estimated_hours

    def __init__(self, title: str, genre: str, company: str, estimated_hours=10):
        super().__init__(title, genre)
        self.__companya = company
        self.__horas_estimadas = estimated_hours

    def __str__(self) -> str:
        print_all = f'Título: {self.titulo}\n' \
                    f'Compañía: {self.__companya}\n' \
                    f'Género: {self.genero}\n' \
                    f'Horas estimadas de juego:{self.__horas_estimadas}\n' \
                    f'Prestado?: {"sí" if self._prestado else "no"}'
        return print_all

    def compareto(self, game: Videojuego) -> str:
        return "Mayor" if self.__horas_estimadas > game.__horas_estimadas else "Iguales" \
            if self.__horas_estimadas == game.__horas_estimadas else "Menor"


if __name__ == '__main__':
    series = [Serie("The Good Place", "Comedy", "Michael Schur", 4), Serie("Cobra Kai", "Action", "Josh Heald", 3),
              Serie("Firefly", "Adventure", "Joss Whedon", 1), Serie("The IT Crowd", "Comedy", "Graham Linehan", 5),
              Serie("Mononoke", "Ghost Stories", "Kenji Nakamura", 1)]
    videojuegos = [Videojuego("TowerFal Ascension", "Local Multiplayer", "Matt Makes Games Inc.", 5),
                   Videojuego("The Battle of Polytopia", "4x", "Midjiwan AB", 12),
                   Videojuego("BattleTech", "Turn-Strategy", "Paradox Interactive", 50),
                   Videojuego("Space Invaders Extreme", "Arcade", "TAITO CORP.", 10),
                   Videojuego("Stoneshard", "Roguelike", "HypeTrain Digital", 30)]

    series[random.randint(0, 4)].prestar()
    series[random.randint(0, 4)].prestar()
    series[random.randint(0, 4)].prestar()

    videojuegos[random.randint(0, 4)].prestar()
    videojuegos[random.randint(0, 4)].prestar()
    videojuegos[random.randint(0, 4)].prestar()

    # Cuenta cuantos Series y Videojuegos hay entregados. Al contarlos, devuélvelos.


    def make_compare(array: list) -> object:
        longest: object = None
        for item in array:
            i = 0
            while i < len(array):
                compare = item.compareto(array[i])
                if compare == "Mayor":
                    longest = item
                elif compare == "Menor":
                    longest = array[i]
                i += 1
        return longest

    print("Esta es la serie con más temporadas:")
    print(make_compare(series))
    print()
    print("Este es el videojuego más largo:")
    print(make_compare(videojuegos))

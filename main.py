from __future__ import annotations

import random

from models.Serie import Serie
from models.Videojuego import Videojuego

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

    print(f"Series prestadas:")
    for serie in series:
        if serie.estaPrestado(): print(f"- {serie.titulo}")

    print()
    print("Videojuegos prestados:")
    for game in videojuegos:
        if game.estaPrestado(): print(f"- {game.titulo}")


    def make_compare(array: list) -> object:
        longest: object = None
        for item in array:
            i = 0
            while i < len(array):
                compare = item.compararCon(array[i])
                if compare == "Mayor":
                    longest = item
                elif compare == "Menor":
                    longest = array[i]
                i += 1
        return longest

    print()
    print("Esta es la serie con más temporadas:")
    print(make_compare(series))
    print()
    print("Este es el videojuego más largo:")
    print(make_compare(videojuegos))

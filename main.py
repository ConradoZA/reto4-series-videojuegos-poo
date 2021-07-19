from __future__ import annotations

import random

from functions.count_and_compare import make_compare, count_and_list
from models.Serie import Serie
from models.Videojuego import Videojuego

if __name__ == '__main__':
    series = [Serie("The Good Place", "Comedy", "Michael Schur", 4), Serie("Cobra Kai", "Action", "Josh Heald", 3),
              Serie("Firefly", "Adventure", "Joss Whedon", 1), Serie("The IT Crowd", "Comedy", "Graham Linehan", 5),
              Serie("Mononoke", "Ghost Stories", "Kenji Nakamura", 1)]
    videojuegos = [Videojuego("TowerFall Ascension", "Local Multiplayer", "Matt Makes Games Inc.", 5),
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

    rented_series: list = count_and_list(series)
    rented_games: list = count_and_list(videojuegos)

    print(f"Series prestadas({len(rented_series)}):")
    for serie in rented_series: print(serie, "\n")
    print()
    print(f"Videojuegos prestados({len(rented_games)}):")
    for game in rented_games: print(game, "\n")
    print()
    print("Esta es la serie con más temporadas:")
    print(make_compare(series))
    print()
    print("Este es el videojuego más largo:")
    print(make_compare(videojuegos))

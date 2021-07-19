class ObjetoAlquilable:
    _titulo = ""
    _genero = ""
    _prestado = False

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def genero(self) -> str:
        return self._genero

    @titulo.setter
    def titulo(self, title: str) -> None:
        self._titulo = title

    @genero.setter
    def genero(self, genre: str) -> None:
        self._genero = genre

    def __init__(self, title: str, genre: str) -> None:
        self._titulo = title
        self._genero = genre

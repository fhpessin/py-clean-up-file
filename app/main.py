import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self):
        # O método enter inicia o contexto de tempo de execução
        # Neste caso, apenas retornamos a própria instância
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        # O método exit limpa o ambiente ao final do bloco with
        # Verificamos se o arquivo existe antes de tentar removê-lo
        if os.path.exists(self.filename):
            os.remove(self.filename)

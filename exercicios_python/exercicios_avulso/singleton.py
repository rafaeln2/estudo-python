class Singleton:
    _instancia = None
    def __new__(cls):
        if not cls._instancia:
            cls._instancia = super().__new__(cls)
        return cls._instancia

Singleton()
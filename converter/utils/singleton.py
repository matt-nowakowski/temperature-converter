class Singleton(type):
    """
    This is a singleton metaclass that ensures that only one instance of the class exists.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

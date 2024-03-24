class DataShelter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            
            cls._instance.uniterm_1 = None
            cls._instance.uniterm_2 = None

        return cls._instance
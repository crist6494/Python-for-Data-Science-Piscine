class calculator:
    """A class to represent a calculator"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Method to calculate the dot product of two vectors"""
        result = sum(int(V1[i] * V2[i]) for i in range(len(V1)))
        print(f"Dot Product is : {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Method to add two vectors"""
        result = list(float(V1[i] + V2[i]) for i in range(len(V1)))
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Method to subtract two vectors"""
        arr = list(float(V1[i] - V2[i]) for i in range(len(V1)))
        print(f"Sous Vector is : {arr}")

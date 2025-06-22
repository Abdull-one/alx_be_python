class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Performs addition without needing class/instance context."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Performs multiplication and accesses class-level attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

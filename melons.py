"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract class base for melon orders to inherit from."""

    shipped = False
    is_christmas = False

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return (1.5 * total if self.is_christmas else total)

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def mark_is_christmas():

        self.is_christmas = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(self, species, qty)
        self.order_type = "domestic"
        self.tax = 0.08

    
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price, including tax"""

        return (super().get_total() 
                if self.qty >= 10 
                else (super().get_total() + 3.00))


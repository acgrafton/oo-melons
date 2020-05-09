"""Classes for melon orders."""

from random import randint
from datetime import datetime

class AbstractMelonOrder():
    """An abstract class base for melon orders to inherit from."""

    shipped = False
    is_christmas = False
    tax = 0.00
    order_datetime = datetime.now()

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        self.species = species
        self.qty = qty

    def get_base_price(self):
        """Generate base price randomly between 5-9"""

        current_hour = self.order_datetime.hour-6 #Current hour in MST
        current_dow = self.order_datetime.isoweekday() #Current DOW in MST

        rush_hour_surcharge = 4

        return (randint(5,9) + rush_hour_surcharge 
                if 8 < current_hour < 11 and current_dow < 6
                else  randint(5,9)
                )

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        total = (1 + self.tax) * self.qty * base_price

        return (1.5 * total if self.is_christmas else total)

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def mark_is_christmas():

        self.is_christmas = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08
        
    
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17       
    
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.country_code = country_code

        
    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price, including tax"""

        return (super().get_total() 
                if self.qty >= 10 
                else (super().get_total() + 3.00))

class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order """

    order_type = "government"
    passed_inspection = False

    def mark_inspection(self, passed):

        self.passed_inspection = passed
        


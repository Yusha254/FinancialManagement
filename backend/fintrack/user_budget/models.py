from django.db import models

# Create your models here.
from django.db import models

class Expenses(models.Model):
    housing = models.DecimalField(max_digits=10, decimal_places=2)
    transportation = models.DecimalField(max_digits=10, decimal_places=2)
    food = models.DecimalField(max_digits=10, decimal_places=2)
    entertainment = models.DecimalField(max_digits=10, decimal_places=2)
    personal_care = models.DecimalField(max_digits=10, decimal_places=2)
    debt_payment = models.DecimalField(max_digits=10, decimal_places=2)
    savings = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.housing} {self.transportation} {self.food} {self.entertainment} {self.personal_care} {self.debt_payment} {self.savings}"
    
    def total(self):
        return self.housing + self.transportation + self.food + self.entertainment + self.personal_care + self.debt_payment + self.savings
    
class Expenditures(models.Model):
    Date = models.DateField()
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Expenses, on_delete=models.CASCADE)

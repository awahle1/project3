from django.db import models

# Create your models here.
class Pizza(models.Model):
    type = models.CharField(
    max_length = 8,
    choices = [('Sicilian', 'Sicilian'), ('Regular', 'Regular')],
    default='Regular',
    )
    TOPPINGS = (
    ('Pepperoni', 'Pepperoni'),
    ('Sausage', 'Sausage'),
    ('Mushrooms', 'Mushrooms'),
    ('Onions','Onions'),
    ('Ham','Ham'),
    ('Canadian Bacon','Canadian Bacon'),
    ('Pineapple','Pineapple'),
    ('Eggplant','Eggplant'),
    ('Tomato & Basil','Tomato & Basil'),
    ('Green Peppers','Green Peppers'),
    ('Hamburger','Hamburger'),
    ('Spinach','Spinach'),
    ('Artichoke', 'Artichoke'),
    ('Buffalo Chicken','Buffalo Chicken'),
    ('Barbecue Chicken','Barbecue Chicken'),
    ('Anchovies','Anchovies'),
    ('Black Olives','Black Olives'),
    ('Fresh Garlic','Fresh Garlic'),
    ('Zucchini','Zucchini'),
    ('None', 'None'),
    )

    topping1= models.CharField(
    max_length = 25,
    choices = TOPPINGS,
    default=' ',
    )

    topping2= models.CharField(
    max_length = 25,
    choices = TOPPINGS,
    default=' ',
    )

    topping3= models.CharField(
    max_length = 25,
    choices = TOPPINGS,
    default=' ',
    )

    topping4= models.CharField(
    max_length = 25,
    choices = TOPPINGS,
    default=' ',
    )

    topping5= models.CharField(
    max_length = 25,
    choices = TOPPINGS,
    default=' ',
    )

    size = models.CharField(
    max_length = 5,
    choices = [('Small', 'Small'), ('Large', 'Large')],
    default = 'Small',
    )
    def __str__(self):
        return("{} {} with {}, {}, {}, {}, {}").format(self.size, self.type, self.topping1, self.topping2, self.topping3, self.topping4, self.topping5)

class Sub(models.Model):
    SUBOPTIONS=(
    ('Cheese', 'Cheese'),
    ('Italian', 'Italian'),
    ('Ham + Cheese', 'Ham + Cheese'),
    ('Meatball', 'Meatball'),
    ('Tuna', 'Tuna'),
    ('Turkey', 'Turkey'),
    ('Chicken Parmigiana', 'Chicken Parmigiana'),
    ('Eggplant Parmigiana', 'Eggplant Parmigiana'),
    ('Steak', 'Steak'),
    ('Steak + Cheese', 'Steak + Cheese'),
    ('Sausage, Peppers & Onions', 'Sausage, Peppers & Onions'),
    ('Hamburger', 'Hamburger'),
    ('Cheeseburger', 'Cheeseburger'),
    ('Fried Chicken', 'Fried Chicken'),
    ('Veggie', 'Veggie'),
    )
    size = models.CharField(
    max_length = 5,
    choices = [('Small', 'Small'), ('Large', 'Large')],
    default = 'Small',
    )

    sub = models.CharField(
    max_length = 30,
    choices = SUBOPTIONS,
    default='Cheese',
    )

    addmushrooms = models.CharField(
    max_length = 3,
    choices = [('Yes', 'Yes'), ('No', 'No')],
    default='No',
    )

    addgreenpeppers = models.CharField(
    max_length = 3,
    choices = [('Yes', 'Yes'), ('No', 'No')],
    default='No',
    )

    addonions = models.CharField(
    max_length = 3,
    choices = [('Yes', 'Yes'), ('No', 'No')],
    default='No',
    )

    extracheese = models.CharField(
    max_length = 3,
    choices = [('Yes', 'Yes'), ('No', 'No')],
    default='No',
    )
    def __str__(self):
        return("{} {} Sub Mushrooms: {}, Green Peppers: {}, Onions: {}, Extra Cheese: {}").format(self.size, self.sub, self.addmushrooms, self.addgreenpeppers, self.addonions, self.extracheese)

class Salad(models.Model):
    SALADOPTIONS = (
    ('Garden Salad', 'Garden Salad'),
    ('Greek Salad', 'Greek Salad'),
    ('Antipasto', 'Antipasto'),
    ('Salad w/Tuna', 'Salad w/Tuna'),
    )

    salad = models.CharField(
    max_length = 15,
    choices=SALADOPTIONS,
    default='Garden Salad',
    )
    def __str__(self):
        return("{}").format(self.salad)

class Pasta(models.Model):
    PASTAOPTIONS = (
    ('Baked Ziti w/Mozzarella', 'Baked Ziti w/Mozzarella'),
    ('Baked Ziti w/Meatballs', 'Baked Ziti w/Meatballs'),
    ('Baked Ziti w/Chicken', 'Baked Ziti w/Chicken'),
    )

    pasta = models.CharField(
    max_length = 25,
    choices=PASTAOPTIONS,
    default='Baked Ziti w/Mozzarella',
    )
    def __str__(self):
        return("{}").format(self.pasta)

class DinnerPlatter(models.Model):
    PLATTEROPTIONS = (
    ('Garden Salad', 'Garden Salad'),
    ('Greek Salad', 'Greek Salad'),
    ('Antipasto', 'Antipasto'),
    ('Baked Ziti', 'Baked Ziti'),
    ('Meatball Parm', 'Meatball Parm'),
    ('Chicken Parm', 'Chicken Parm'),
    )

    platter = models.CharField(
    max_length = 20,
    choices=PLATTEROPTIONS,
    default='Baked Ziti',
    )

    size = models.CharField(
    max_length = 5,
    choices = [('Small', 'Small'), ('Large', 'Large')],
    default = 'Small',
    )
    def __str__(self):
        return("{} {}").format(self.size, self.platter)

class Order(models.Model):
    pizza = models.ManyToManyField(Pizza, related_name="orders")
    salads = models.ManyToManyField(Salad, related_name="orders")
    subs = models.ManyToManyField(Sub, related_name="orders")
    platters = models.ManyToManyField(DinnerPlatter, related_name="orders")
    pasta = models.ManyToManyField(Pasta, related_name="orders")
    def __str__(self):
        return("Order {}").format(self.id)

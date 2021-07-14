'''
class Product(models.Model):
    title = models.CharField(max_length=64)
    price = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='category/images')

    def __str__(self):
        return self.title
'''

products = [
            'Product(1)', 'Product(2)', 'Product(3)', 'Product(4)',
            'Product(5)', 'Product(6)', 'Product(7)', 'Product(8)',
            'Product(9)', 'Product(10)', 'Product(11)', 'Product(12)',
            'Product(13)',
            ]

'''
# views.py

from .models import Product

def index(request):
    products = Product.objects.all()     # products
'''

'''
Excersise: Dump last five product
'''
print(products[-5:])

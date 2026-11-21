from django.core.management.base import BaseCommand
from store.models import Category, Product

DATA = {
    'Electronics': [
        ('Wireless Earbuds', 1999, 25, 'Bluetooth earbuds with charging case and 20-hour battery.'),
        ('Smart Watch', 3499, 12, 'Fitness tracking, heart-rate monitor and notifications.'),
        ('Power Bank 10000mAh', 1299, 40, 'Compact fast-charging power bank.'),
    ],
    'Fashion': [
        ('Cotton T-Shirt', 499, 60, 'Soft everyday cotton t-shirt.'),
        ('Denim Jacket', 2199, 15, 'Classic fit denim jacket.'),
        ('Canvas Sneakers', 1499, 30, 'Lightweight sneakers for daily wear.'),
    ],
    'Home': [
        ('Ceramic Mug Set', 699, 35, 'Set of 4 ceramic mugs.'),
        ('LED Desk Lamp', 899, 20, 'Adjustable brightness desk lamp.'),
        ('Wall Clock', 799, 18, 'Minimal silent wall clock.'),
    ],
    'Books': [
        ('Python Crash Course', 999, 22, 'Hands-on introduction to Python programming.'),
        ('Clean Code', 1199, 14, 'A handbook of agile software craftsmanship.'),
    ],
}


class Command(BaseCommand):
    help = 'Load sample categories and products'

    def handle(self, *args, **options):
        from django.utils.text import slugify
        count = 0
        for cat_name, items in DATA.items():
            cat, _ = Category.objects.get_or_create(name=cat_name, defaults={'slug': slugify(cat_name)})
            for name, price, stock, desc in items:
                _, created = Product.objects.get_or_create(
                    slug=slugify(name),
                    defaults={'category': cat, 'name': name, 'price': price, 'stock': stock, 'description': desc},
                )
                count += created
        self.stdout.write(self.style.SUCCESS(f'Seeded {count} new products.'))

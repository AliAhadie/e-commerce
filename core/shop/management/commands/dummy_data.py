from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
import random
from decimal import Decimal

from shop.models import Product, ProductCategory
from django.contrib.auth import get_user_model
from shop.models import ProductStatus

fake = Faker()
User = get_user_model()


class Command(BaseCommand):
    help = "Seed the database with 10 fake products and 10 categories"

    def handle(self, *args, **kwargs):
        users = list(User.objects.all())
        if not users:
            self.stdout.write(
                self.style.ERROR("❌ No users found. Please create a user first.")
            )
            return

        categories = list(ProductCategory.objects.all())
        if not categories:
            self.stdout.write(
                self.style.ERROR("❌ No categories found. Please create a category first.")
            )
            return

        self.stdout.write("🛒 Creating 10 products...")
        

        self.stdout.write(self.style.SUCCESS("✅ Seeding completed successfully!"))


        for _ in range(10):
            user = random.choice(users)
            title = fake.sentence(nb_words=3).rstrip(".")
            slug = slugify(title)
            description = fake.paragraph(nb_sentences=3)
            stock = random.randint(1, 100)
            status = random.choice([status.value for status in ProductStatus])
            price = Decimal(random.uniform(10.0, 1000.0)).quantize(Decimal("0.01"))
            discount = random.randint(0, 50)

            product = Product.objects.create(
                user=user,
                title=title,
                slug=slug,
                description=description,
                stock=stock,
                status=status,
                price=price,
                discount_percnete=discount,
            )

            # Assign random categories to the product
            selected_categories = random.sample(categories, random.randint(1, len(categories)))
            product.category.set(selected_categories)
            product.save()

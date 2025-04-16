from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
import random
from decimal import Decimal

from shop.models import Product, ProductCategory, ProductStatus
from django.contrib.auth import get_user_model

fake = Faker("fa_IR")
User = get_user_model()


def unique_slugify(model, title, index=0):
    """FOR UNIQE SLUG"""

    base_slug = slugify(title, allow_unicode=True)
    if not base_slug:
        base_slug = "item"
    slug = f"{base_slug}-{index}" if index else base_slug
    while model.objects.filter(slug=slug).exists():
        index += 1
        slug = f"{base_slug}-{index}"
    return slug


class Command(BaseCommand):
    help = "Genaret fake data with faker"

    def handle(self, *args, **kwargs):
        users = list(User.objects.all())
        if not users:
            self.stdout.write(
                self.style.ERROR("❌ USER DOSENT FIND PLEASE FRIST CREATE USER!")
            )
            return

        self.stdout.write("📂 CREATING CATEGORIES ...")
        categories = []
        for _ in range(10):
            title = fake.word()
            slug = unique_slugify(ProductCategory, title)
            category = ProductCategory.objects.create(title=title, slug=slug)
            categories.append(category)
        self.stdout.write(self.style.SUCCESS("✅ CREATED 10 CATEGORIES."))

        self.stdout.write("🛒 CREATING PRODUCTS ...")
        for _ in range(10):
            title = fake.sentence(nb_words=3).rstrip(".")
            slug = unique_slugify(Product, title)
            description = fake.paragraph(nb_sentences=3)
            stock = random.randint(1, 100)
            status = random.choice([status.value for status in ProductStatus])
            price = Decimal(random.uniform(10.0, 1000.0)).quantize(Decimal("0.01"))
            discount = random.randint(0, 50)
            user = random.choice(users)

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

            selected_categories = random.sample(
                categories, random.randint(1, len(categories))
            )
            product.category.set(selected_categories)
            product.save()

        self.stdout.write(self.style.SUCCESS("✅ CREATED 10 PRODUCTS."))

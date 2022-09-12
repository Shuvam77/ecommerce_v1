from django.forms import ImageField
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Product, ProductImage


@registry.register_document
class ProductDocument(Document):
    category = fields.ObjectField(properties={"name": fields.TextField()})

    product_type = fields.ObjectField(properties={"name": fields.TextField()})

    class Index:
        name = "product"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Product
        fields = ["id", "title", "description", "slug", "regular_price", "discount_price"]


@registry.register_document
class ProductImageDocument(Document):
    product = fields.ObjectField(
        properties={
            "title": fields.TextField(),
            "id": fields.IntegerField(),
            "description": fields.TextField(),
            "slug": fields.TextField(),
            "regular_price": fields.FloatField(),
        }
    )

    class Index:
        name = "productimage"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ProductImage
        fields = ["image", "alt_text"]

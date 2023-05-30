from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Slider)
admin.site.register(Ad)
admin.site.register(Brand)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "discounted_price", "category", "subcategory", "label", "stock")
    list_filter = ("category", "subcategory", "label", "stock")
    search_fields = ("name", "description")

admin.site.register(ProductImage)
admin.site.register(ProductReview)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("username", "quantity", "checkout",)
    list_filter = ("checkout",)
    search_fields = ("username",)

admin.site.register(Contact)
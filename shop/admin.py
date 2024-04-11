from django.contrib import admin
from .models import GeneralCategory,Category,Campaign,Product,ProductImage,PlayStation3,PlayStation4,PlayStation5,childGamesPs3,childGamesPs4,childGamesPs5
from customer.models import Review
# Register your models here.


class ProductImageInline(admin.TabularInline):
    model=ProductImage
    readonly_fields=['image_tag']
    extra=1

class ReviewInline(admin.TabularInline):
    model=Review
    readonly_fields=['customer','star_count','comment']
    extra=0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImageInline,ReviewInline]
    readonly_fields = ['slug']
    list_filter=['general']

# admin.site.register(Size)
# admin.site.register(Color)
admin.site.register(GeneralCategory)
admin.site.register(Category)
admin.site.register(Campaign)
admin.site.register(ProductImage)
admin.site.register(PlayStation3)
admin.site.register(PlayStation4)
admin.site.register(PlayStation5)
admin.site.register(childGamesPs3)
admin.site.register(childGamesPs4)
admin.site.register(childGamesPs5)
# admin.site.register(warGamesPs3)
# admin.site.register(warGamesPs4)
# admin.site.register(warGamesPs5)
# admin.site.register(sportGamesPs3)
# admin.site.register(sportGamesPs4)
# admin.site.register(sportGamesPs5)
# admin.site.register(carGamesPs3)
# admin.site.register(carGamesPs4)
# admin.site.register(carGamesPs5)

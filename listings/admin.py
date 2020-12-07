from django.contrib import admin


from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','address', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links=('id','price','realtor')
    list_filter=('realtor',)
    list_editable=('is_published',)
    search_fields = ('address', 'city', 'state', 'zipcode', 'price', 'realtor',)
    list_per_page=25
    

admin.site.register(Listing,ListingAdmin)
# Register your models here.

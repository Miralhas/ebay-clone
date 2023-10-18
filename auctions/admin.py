from django.contrib import admin
from .models import AuctionListing, User, Bid, Comment, Watchlist, Categories

# Register your models here.

admin.site.register(AuctionListing)
admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Watchlist)
admin.site.register(Categories)
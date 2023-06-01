from django.urls import path

from . import views

urlpatterns = [
    path("", views.active_listings, name="active_listings"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add_listing", views.add_listing, name="add_listing"),
    path("listing/<str:id>", views.listing_page, name="listing_page"),
    path("listing/watchlist/<str:id>", views.watchlist, name="watchlist"),
]

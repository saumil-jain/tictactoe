from django.conf.urls import url

from .views import game_detail, make_move


urlpatterns = [
    url(r"^game_details/(?P<id>\d+)/$", game_detail, name="gameplay_detail"),
    url(r"^make_move/(?P<id>\d+)", make_move, name="gameplay_make_move")
]

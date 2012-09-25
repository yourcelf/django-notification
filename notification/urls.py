from django.conf.urls.defaults import *

from notification.views import notices, mark_all_seen, single, notice_settings


urlpatterns = patterns("",
    url(r"^$", notices, name="notification_notices"),
    url(r"^settings/$", notice_settings, name="notification_notice_settings"),
    url(r"^(\d+)/$", single, name="notification_notice"),
    url(r"^mark_all_seen/$", mark_all_seen, name="notification_mark_all_seen"),
)

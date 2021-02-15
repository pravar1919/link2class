import datetime
from django.core.cache import cache
from accounts.models import CustomUser
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone



# class ActiveUserMiddleware(MiddlewareMixin):

#     def process_request(self, request):
#         current_user = request.user
#         if request.user.is_authenticated:
#             now = datetime.datetime.now()
#             cache.set('seen_%s' % (current_user.first_name), now, 
#                            settings.USER_LASTSEEN_TIMEOUT)

from django.core.cache import cache
from django.conf import settings
# from django.contrib.auth.models import User

ONLINE_THRESHOLD = getattr(settings, 'ONLINE_THRESHOLD', 60 * 15)
ONLINE_MAX = getattr(settings, 'ONLINE_MAX', 50)

def get_online_now(self):
    return CustomUser.objects.filter(id__in=self.online_now_ids or [])


class OnlineNowMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # First get the index
        uids = cache.get('online-now', [])
        
        # Perform the multiget on the individual online uid keys
        online_keys = ['online-%s' % (u,) for u in uids]
        fresh = cache.get_many(online_keys).keys()
        online_now_ids = [int(k.replace('online-', '')) for k in fresh]
        
        # If the user is authenticated, add their id to the list
        if request.user.is_authenticated:
            uid = request.user.id
            # If their uid is already in the list, we want to bump it
            # to the top, so we remove the earlier entry.
            if uid in online_now_ids:
                online_now_ids.remove(uid)
            online_now_ids.append(uid)
            if len(online_now_ids) > ONLINE_MAX:
                del online_now_ids[0]
        
        # Attach our modifications to the request object
        request.__class__.online_now_ids = online_now_ids
        request.__class__.online_now = property(get_online_now)
        
        # Set the new cache
        cache.set('online-%s' % (request.user.pk,), True, ONLINE_THRESHOLD)
        cache.set('online-now', online_now_ids, ONLINE_THRESHOLD)

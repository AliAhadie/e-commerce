from django.contrib.auth.mixins import UserPassesTestMixin
from accounts.models import UserType

class IsCustomer(UserPassesTestMixin):

    def test_func(self):
        if self.request.user.is_authenticated:
            if self.request.user.type==UserType.customer.value:
                return True
        return False
    
class IsAdmin(UserPassesTestMixin):

    def test_func(self):
        if self.request.user.is_authenticated:
            if self.request.user.type==UserType.admin.value:
                return True
        return False   
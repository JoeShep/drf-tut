from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer

# Rather than write multiple views we're grouping together all the common behavior into classes called ViewSets.
# We can easily break these down into individual views if we need to, but using viewsets keeps the view logic nicely organized as well as being very concise.
class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited
  """
  queryset = User.objects.all().order_by('-date_joined') #this is a query to the users table
  serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited
  """
  queryset = Group.objects.all()
  serializer_class = GroupSerializer

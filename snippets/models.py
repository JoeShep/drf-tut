from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# list comprehension in action
LEXERS = [item for item in get_all_lexers() if item[1]]
# this comprehension is kind of doing destructuring, kinda maybe
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES =sorted((item, item) for item in get_all_styles())

# make a new class that inherits from the basic Model prototype
class Snippet(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  # Note that this blank is different than null. null is purely database-related, whereas blank is validation-related.
  title = models.CharField(max_length=100, blank=True, default='')
  code = models.TextField()
  linenos = models.BooleanField(default=False)
  # choices= is An iterable (e.g., a list or tuple) consisting itself of iterables of exactly two items (e.g. [(A, B), (A, B) ...]) to use as choices for this field. If this is given, the default form widget will be a select box with these choices instead of the standard text field.
  language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
  style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

  # In Django the attributes of a class (for those that inherit from Model) are expect to be fields that correspond to their counterparts in the database. How then to add attributes that aren't database fields? The Meta class is the container for these non-field attributes.
  class Meta:
    ordering = ('created',)

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# class SnippetSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#   # The {'base_template': 'textarea.html'} flag below is equivalent to using widget=widgets.Textarea on a Django Form class. This is particularly useful for controlling how the browsable API should be displayed
#   code = serializers.CharField(style={'base_template': 'textarea.html'})
#   linenos = serializers.BooleanField(required=False)
#   language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#   style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

  # The create() and update() methods define how fully fledged instances are created or modified when calling serializer.save()

  # def create(self, validated_data):
  #   """
  #   Create and return a new Snippet instance, given the validated data
  #   """
  #   # ** indicates kwargs, which captures all keyword arguments, except for those corresponding to a formal parameter, as a dictionary.
  #   return Snippet.objects.create(**validated_data)

  # def update(self, instance, validated_data):
  #   """
  #   Update and return an existing `Snippet` instance, given the validated data.
  #   """
  #   instance.title = validated_data.get('title', instance.title)
  #   instance.code = validated_data.get('code', instance.code)
  #   instance.linenos = validated_data.get('linenos', instance.linenos)
  #   instance.language = validated_data.get('language', instance.language)
  #   instance.style = validated_data.get('style', instance.style)
  #   instance.save()
  #   return instance

# You can serialize querysets instead of model instances. Use 'serializers.ModelSerializer' instead of 'serializers.Serializer'
#  A `ModelSerializer` is just a regular `Serializer`, except that:

#     * A set of default fields are automatically populated.
#     * A set of default validators are automatically populated.
#     * Default `.create()` and `.update()` implementations are provided.
class SnippetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Snippet
    fields = ('id', 'title', 'code', 'linenos', 'language', 'style') # or '__all__'

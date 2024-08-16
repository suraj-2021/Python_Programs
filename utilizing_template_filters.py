from django import template

register = template.Library()

@register.filter(name='starts_with')
def starts_with(value, letter):
   
    if not isinstance(value, list):
        return [] 
    
    if not isinstance(letter, str) or len(letter) != 1:
        return value 

    return [item for item in value if item.startswith(letter)]


#mytemplate.html

{% load your_template_tags_file %}

<h2>Items Starting with '{{ filter_letter }}'</h2>
<ul>
    {% for item in items|starts_with:filter_letter %}
        <li>{{ item }}</li>
    {% empty %}
        <li>No items found starting with '{{ filter_letter }}'.</li>
    {% endfor %}
</ul>

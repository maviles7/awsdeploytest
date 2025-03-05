from django import template

register = template.Library()

@register.filter
def format_phone_number(value):
    """Format the phone number with parentheses around the first three digits, spaces after the 3rd and 6th digits, and a hyphen between the 6th and 7th digits."""
    if len(value) == 10:
        return f"({value[:3]}){value[3:6]}-{value[6:]}"
    return value

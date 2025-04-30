def escape_tags(value, valid_tags):
    """
    Strips text from the given HTML string, leaving only valid tags.
    """
    value = conditional_escape(value)
    if valid_tags:
        tag_re = re.compile(r'&lt;(\s*/?\s*(%s))(.*?\s*)&gt;' %
                            u'|'.join(re.escape(tag) for tag in valid_tags))
        value = tag_re.sub(_replace_quot, value)
    value = value.replace("&lt;!--", "<!--").replace("--&gt;", "-->")
    return mark_safe(value)

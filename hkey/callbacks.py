# modelled after /mama_cas/callbacks.py user_model_attributes
def user_model_attributes(user, service):
    """
    Return all fields on the user object that are not in the list
    of fields to ignore.
    """
    ignore_fields = ["id", "password"]
    attributes = {}
    for field in user._meta.fields:
        if field.name not in ignore_fields:
            attributes[field.name] = getattr(user, field.name)
    for field in ["givenName", "sn", "mail"]:
        attributes[field] = getattr(user, field)
    return attributes

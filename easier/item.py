class Item(object):
    """
    Item is a simple container class that sets its attributes from constructor
    kwargs.  It supports both object and dictionary access to its attributes.
    So, for example, all of the following statements are supported.

    .. code-block:: python

       item = Item(a=1, b=2)
       item['c'] = 2
       a = item['a']

    An instance of this class is created when you ask to show local variables
    with a `Behold` object. The local variables you want to show are attached as
    attributes to an `Item` object.
    """
    # I'm using unconventional "_item_self_" name here to avoid
    # conflicts when kwargs actually contain a "self" arg.

    def __init__(_item_self, **kwargs):
        for key, val in kwargs.items():
            _item_self[key] = val

    def __str__(_item_self):
        quoted_keys = [
            '\'{}\''.format(k) for k in sorted(vars(_item_self).keys())]
        att_string = ', '.join(quoted_keys)
        return 'Item({})'.format(att_string)

    def __repr__(_item_self):
        return _item_self.__str__()

    def __setitem__(_item_self, key, value):
        setattr(_item_self, key, value)

    def __getitem__(_item_self, key):
        return getattr(_item_self, key)
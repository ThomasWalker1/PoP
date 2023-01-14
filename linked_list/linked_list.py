"""A simple implementation of a linked list."""


class Link:
    """A link in a linked list.

    Parameters
    ----------
    value :
        The value to be stored in the link.
    link : Link
        The next link in the list.

    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def insert(self, link):
        """Insert a new link after this one."""
        link.next = self.next
        self.next = link

    def __iter__(self):
        return LinkIterator(self)


class LinkIterator:
    def __init__(self, link):
        self.link = link

    def __iter__(self):
        return self

    def __next__(self):
        if not self.link:
            raise StopIteration

        value = self.link.value
        self.link = self.link.next
        return value

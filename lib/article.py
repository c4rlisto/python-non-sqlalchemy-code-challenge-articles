# lib/article.py
class Article:
    _all = []

    def __init__(self, author, magazine, title):
        # use the property setters (they'll validate types/ranges)
        self._title = None
        self._author = None
        self._magazine = None

        # validate and assign title (immutable after init)
        self._set_title(title)

        # author and magazine can be changed after init, so call the setters
        self.author = author
        self.magazine = magazine

        # remember this article
        Article._all.append(self)

    # Title property: read-only (no setter)
    @property
    def title(self):
        return self._title

    def _set_title(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters inclusive")
        # set only if not already set (immutability)
        if hasattr(self, "_title") and self._title is not None:
            raise Exception("Title is immutable and already set")
        self._title = title

    # Author property (read/write, must be Author instance)
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        # lazy import to avoid circular imports in some setups
        from lib.author import Author
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        self._author = author

    # Magazine property (read/write, must be Magazine instance)
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        from lib.magazine import Magazine
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        self._magazine = magazine

    # Class helper to access all articles
    @classmethod
    def all(cls):
        return cls._all[:]

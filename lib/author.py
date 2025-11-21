# lib/author.py
class Author:
    _all = []

    def __init__(self, name):
        # validate name type / length
        if not isinstance(name, str):
            raise Exception("Author name must be a string")
        if len(name) == 0:
            raise Exception("Author name must be longer than 0 characters")
        # store as private attribute; no setter -> immutable
        self._name = name
        Author._all.append(self)

    @property
    def name(self):
        return self._name

    # returns list of Article objects the author has written
    def articles(self):
        from lib.article import Article
        return [a for a in Article.all() if a.author is self]

    # returns unique list of Magazine objects the author has contributed to
    def magazines(self):
        mags = []
        for article in self.articles():
            m = article.magazine
            if m not in mags:
                mags.append(m)
        return mags

    # create an article associated to this author and a given magazine
    def add_article(self, magazine, title):
        from lib.article import Article
        # magazine must be Magazine instance; Article.__init__ will validate
        new_article = Article(self, magazine, title)
        return new_article

    # returns unique list of magazine category strings this author has contributed to
    # or None if no articles
    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        # collect unique categories
        categories = []
        for m in mags:
            cat = m.category
            if cat not in categories:
                categories.append(cat)
        return categories

    @classmethod
    def all(cls):
        return cls._all[:]

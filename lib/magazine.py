# lib/magazine.py
class Magazine:
    _all = []

    def __init__(self, name, category):
        # name validations
        if not isinstance(name, str):
            raise Exception("Magazine name must be a string")
        if not (2 <= len(name) <= 16):
            raise Exception("Magazine name must be between 2 and 16 characters inclusive")
        # category validations
        if not isinstance(category, str):
            raise Exception("Magazine category must be a string")
        if len(category) == 0:
            raise Exception("Magazine category must be longer than 0 characters")

        # store as private attributes; both writable via properties
        self._name = name
        self._category = category

        Magazine._all.append(self)

    # name property (read/write)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Magazine name must be a string")
        if not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be between 2 and 16 characters inclusive")
        self._name = value

    # category property (read/write)
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Magazine category must be a string")
        if len(value) == 0:
            raise Exception("Magazine category must be longer than 0 characters")
        self._category = value

    # returns list of Article objects published by this magazine
    def articles(self):
        from lib.article import Article
        return [a for a in Article.all() if a.magazine is self]

    # returns unique list of Author objects who have written for this magazine
    def contributors(self):
        authors = []
        for article in self.articles():
            a = article.author
            if a not in authors:
                authors.append(a)
        return authors

    # returns list of titles (strings) of all articles for this magazine, or None if none
    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [a.title for a in arts]

    # returns list of authors who have written more than 2 articles for this magazine
    # or None if none meet the criteria
    def contributing_authors(self):
        arts = self.articles()
        if not arts:
            return None
        # count articles per author for this magazine
        counts = {}
        for a in arts:
            author = a.author
            counts[author] = counts.get(author, 0) + 1
        result = [author for author, cnt in counts.items() if cnt > 2]
        if not result:
            return None
        return result

    # classmethod to return the Magazine instance with the most articles
    @classmethod
    def top_publisher(cls):
        from lib.article import Article
        # if there are no articles at all, return None
        if len(Article.all()) == 0:
            return None

        best = None
        best_count = -1
        for mag in cls._all:
            count = len([a for a in Article.all() if a.magazine is mag])
            if count > best_count:
                best = mag
                best_count = count
        return best

    @classmethod
    def all(cls):
        return cls._all[:]

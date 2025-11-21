class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = None
        self._magazine = None
        self._title = None

        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

    # ---- TITLE (immutable) ----
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # ignore changes AFTER initialization
        if self._title is not None:
            return

        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value


    # ---- AUTHOR ----
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value


    # ---- MAGAZINE ----
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value



class Author:
    def __init__(self, name):
        self._name = None
        self.name = name

    # ---- NAME (immutable) ----
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # ignore reassignment
        if self._name is not None:
            return

        if isinstance(value, str) and len(value) > 0:
            self._name = value

    # RELATIONSHIPS
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        areas = {article.magazine.category for article in self.articles()}
        return list(areas) if areas else None



class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None

        self.name = name
        self.category = category

    # ---- NAME (mutable, but validated) ----
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    # ---- CATEGORY (mutable, but validated) ----
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    # RELATIONSHIPS
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        # authors with > 2 articles for this magazine
        counts = {}
        for article in self.articles():
            counts[article.author] = counts.get(article.author, 0) + 1

        authors = [a for a, count in counts.items() if count > 2]
        return authors if authors else None

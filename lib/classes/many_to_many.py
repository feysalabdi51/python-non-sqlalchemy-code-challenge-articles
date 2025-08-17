class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if hasattr(self, '_title'):
            return
        self._title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            return
        self._title = value
        
class Author:
    def __init__(self, name):
        if hasattr(self, '_name'):
            return
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            return

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set([magazine.category for magazine in self.magazines()]))

class Magazine:
    all = []
    
    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        contributing = [author for author, count in author_counts.items() if count > 2]
        return contributing if contributing else None
    
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        
        magazine_counts = {}
        for article in Article.all:
            magazine = article.magazine
            magazine_counts[magazine] = magazine_counts.get(magazine, 0) + 1
        
        if not magazine_counts:
            return None
            
        return max(magazine_counts, key=magazine_counts.get)
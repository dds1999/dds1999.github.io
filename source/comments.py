from google.appengine.ext import ndb

class Comments(ndb.Model):
    text = ndb.StringProperty()
    pageId = ndb.IntegerProperty()


commentList = []

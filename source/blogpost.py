class Blogpost:
    def __init__(self, id, title, content, comments):
        self.id = int(id)
        self.title = title
        self.content = content
        self.commentSection = comments
    def toDictionary(self):
        dictionary = {
            "title" : self.title,
            "postId" : self.id,
            "content" : self.content,
            "commentSection" : self.commentSection
        }
        return dictionary

    def commentsAsHTML(self, commentList):
        final = ""
        for text in commentList:
            if text == None:
                final = final
            else:
              final = ("<hr><p>"+text+"</p>\n") + final
        return final

home = Blogpost(0, "Home",  open("template/id0content.html").read(), [])
page1 = Blogpost(1, "About Me", open("template/id1content.html").read(), [])
page2 = Blogpost(2, "First Post", open("template/id2content.html").read(), [])
blogpages = { 0 : home,
              1 : page1,
              2 : page2
             }

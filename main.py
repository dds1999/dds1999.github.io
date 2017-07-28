#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import sys
import json

sys.path.append('source/')
from blogpost import Blogpost
from blogpost import blogpages
from blogpost import home
from comments import Comments
from comments import commentList


env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))

def constructHome(page):
    pageDict = page.toDictionary()
    pageTemp = env.get_template("main.html")
    pageFinal = pageTemp.render(pageDict)
    return pageFinal

class MainHandler(webapp2.RequestHandler):
    def get(self):
        home = blogpages[0]
        self.response.out.write(constructHome(home))

class PostHandler(webapp2.RequestHandler):
    def get(self):
        page = blogpages[int(self.request.get('id'))]
        self.response.out.write(self.constructComments(page, page.id))

    def constructBlogPost(self, page):
        pageDict = page.toDictionary()
        pageTemp = env.get_template("page.html")
        pageFinal = pageTemp.render(pageDict)
        return pageFinal

    def constructComments(self, comment, page_id):
        thisPageComments_query = Comments.query(Comments.pageId == page_id)
        thisPageComments = thisPageComments_query.fetch()
        commentList = []
        for comment in thisPageComments:
            if (comment.text != None):
                commentList.append(comment.text)
        this = blogpages[page_id]
        commentHTML = this.commentsAsHTML(commentList)
        this.commentSection = commentHTML
        return self.constructBlogPost(this)

    def post(self):
        page_id = int(self.request.get('id'))
        commentText = self.request.get('commentBox')
        print "############"
        print commentText
        comment = Comments(text = commentText,pageId = page_id)
        comment.key = comment.put()
        commentList.append(comment)
        page = blogpages[page_id]
        #self.response.out.write(constructBlogPost(page))
        self.response.out.write(self.constructComments(comment, page_id))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/view-post', PostHandler)
], debug=True)

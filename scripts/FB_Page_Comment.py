#! /usr/bin/python3

import fb
from facepy import GraphAPI

access_token = ""  # your access token which you can get at developer.facebook.com
fb_graph = GraphAPI (access_token)
fbc = fb.graph.api (access_token)
page_id = input ("Enter the facebook id of the page : ")
comment = input ("Enter the comment to be posted : ")
request = fb_graph.get (page_id + "/feed?fields=id")
posts = [p['id'] for p in request['data']]
for post in posts :
    fbc.publish (cat = 'comments', id = post, message = comment)
    print ("Posted!")



# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
import scraperwiki
   html = scraperwiki.scrape('http://inmo.ie/6022')
   import lxml.html
   root = lxml.html.fromstring(html) # turn our HTML into an lxml object
   tds = root.cssselect('td') # get all the <td> tags
   for td in tds:
      record = { "td" : td.text } # column name and value
      try:
           scraperwiki.sqlite.save(["td"], record) # save the records one by one
      except:
           record = { "td" : "NO ENTRY" } # column name and value
           scraperwiki.sqlite.save(["td"], record) # save the records one by one

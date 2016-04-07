Title: Using Travis CI
Date: 2016-04-06
Category: 
Tags: Blog, Automate
Slug: Automate-with-Travis-CI
Author: Ben Healy
Summary: Simplifying the blog one step further with the help of a new tool.

Static site generators like Pelican are great for their simplicity. But my current workflow still requires several steps:

	1. Write the blog post in Markdown
	2. Run the python script to turn the Markdown files into HTML
	3. Use GitHub to upload the newest version of both the source blog files (written in markdown) and the published website files.

Travis helps eliminate the later steps by watching the GitHub repo with the blog source files, and when there is a noticeable change -- it automatically runs the python script to turn the Markdown to HTML and push the new files to the published repo.

Thanks to the helpful instructions from sites like Kevin Yap's it was pretty straighforward to set up too: [http://kevinyap.ca/2014/06/deploying-pelican-sites-using-travis-ci/](http://kevinyap.ca/2014/06/deploying-pelican-sites-using-travis-ci/).


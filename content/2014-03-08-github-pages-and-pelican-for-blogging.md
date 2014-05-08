Title: GitHub Pages and Pelican for Blogging
Date: 2014-03-26
Category: Blog
Tags: github pages, pelican, git, blogging
Slug: github-pages-and-pelican-for-blogging
Author: Ben Healy
Summary: Blogging with Pelican and Python, HELLO WORLD. Not much to see here.

Hello, world. This website is brought to you using a combination of GitHub Pages and Pelican, a Python-based static site generator. 
Not so long ago I built a website from scratch with the intention of gaining some web-development skills. I read up on HTML, CSS and JavaScript and even dove into some fairly simple D3.js to try
and bring some data-analysis to life on the site. As it turns out, I'm just not all that interested in being responsible for every little piece of web development necessary to carry on that kind
of operation. Unfortunately, it became a humongous time-suck that took away from what I am actually interested in: playing with data. 

While I am not forever swearing off turning my findings into interactive web-applications,  I don't have the time to... wait, let me rephrase that... I'm not interested (at least at the current moment) 
in having to slave over the web-development that's necessary for each and every post I write. Having to wade through my poorly written CSS, HTML, and most of all JavaScript really sucks. So, instead I
looked for a way to still have more control over my site than I would on a standard Google Blogger or Wordpress site but also have a built-in safety net that could do a bunch of the work for me when I 
just want to write something, and post some results of whatever I'm working on. It will likely come as no surprise to anyone that there are seemingly an unlimited 
number of ways with which one could create a site that fits the bill. But after doing some research I settled on using GitHub [Pages](http://pages.github.com/) (because it's free! no more monthly
site hosting bills) and [Pelican](http://blog.getpelican.com/). Pelican is a static site generator that turns markdown text documents into static html for you, has a great online community that is
helpful when in search of help, and has lots of cool built in features that you can take advantage of but don't have to. You can use a pre-made theme for your site, but then still get at all of the
HTML and CSS if you want to modify it to your liking. If you're interested in learning more, check it out: [Pelican Blog](http://blog.getpelican.com/)

Pelican lets users write things in Markdown, which is a language I've never used myself, but is praised in coding communities all over the place. After using it for about an hour, I can see why.
It's intuitive and it is fairly low-brow in terms of complexity. Sure beats the hell out of trying to remember to close out all the brackets in an HTML doc. But Markdown still has its own syntax that
allows users to easily format things. Just for the sake of me learning, let's take a look:

Headers of varying levels:

#Header 1
##Header 2
###Header 3

Quotes:

>This is an example of a block quote,
>you're able to insert these very easily
>into any given document
>>You can even nest block quotes!

Lists:

* one
* two
* three

Ok, so I think this is the best part. Because I will be discussing some of my coding projects here, it is nice to be able to show users some snippets of code while walking through
examples. I've always wondered how people did this on their respective blogs, I guess I always thought that they just took screen shots and embedded the image into a post. But no! It is
far simpler than that if you are using Markdown. You just indicate what language/environment you are writing in (Python, R, command prompt, etc) and it will create all of the syntax highlighting
for you. Here is an example of something being committed to GitHub in bash:

    :::bash
    $ cd blog/      # root directory for my blog
    $ make devserver    # automatically re-generates site and hosts site locally
    # change something in content or settings
    $ git add --all
    $ git commit -m "committing blog source"
    $ git push origin master    # pushes to my blog-source repo on GitHub
    $ cd output/    # pelican-generated output folder
    $ git commit -am "committing pelican-generated site content"
    $ git push origin master    # pushes to my bheal521.github.io repo

And here is something in Python:

	:::python
	def hello()
		print 'Hello World, Markdown is great!'
		

Ok, so this was a lame first post. So be it. But I'm psyched to start using Pelican with Markdown in order to document some of my analytical explorations here. I'm currently working on
scraping the Pitchfork music review website of the most recent ~10k reviews in order to do some text analysis. Stay tuned for what will hopefully be something more interesting.
Title: GitHub Pages and Pelican for Blogging
Date: 2014-03-26
Category: Blog
Tags: github pages, pelican, git, blogging
Slug: github-pages-and-pelican-for-blogging
Author: Ben Healy

Hello, world. This blog is brought to you by a combination of GitHub [pages](http://pages.github.com/) and [Pelican](http://blog.getpelican.com/). Not so long ago I came to you
on a website that I developed from scratch. I bought a web-address, and jumped right into the HTML. Turns out, I'm just not all that interested in developing HTML, CSS, and Java from scratch.
Unfortunately, it became a humongous time-suck that took away from what I am actually interested in: playing with data. 

While I would love for someone else to turn my experiments into interactive web-applications,  I don't have the time... Let me rephrase that. I'm not interested (at least at the current moment) in
taking the time to wade through my poorly written CSS and HTML, much less Javascript... in order to make a home-made solution from scratch. It comes as no surprise to anyone that there are seemingly an unlimited 
number of ways with which one could create a less-customizable blogging platform. The trouble is, I really do want to have more control of the site if I choose to dive deeper. I just don't want to HAVE
to do everything. So shortly after I stopped working on my old site, I stumbled across an simple blogging site from a fellow data scientist. [Greg Reda](http://www.gregreda.com/) shot to the top of some subReddits
that I follow, as well as [Hacker News](https://news.ycombinator.com/). His article on the principles of good data analysis caught my eye, and the eyes of many, many others. But his simple website was 
pretty much exactly what I was looking to do. I reached out to him, and he suggested Pelican, a Python based static site generator. Once set up, Pelican will turn textual documents written in [Markdown](https://daringfireball.net/projects/markdown/)
into HTML. What's more, there are pre-made CSS formats that users can tweak to their hearts delight. It seemed like a great combination.

I'm new to the world of Markdown text, but as I write to you now I am already getting the hang of it. It is far more like regular written text than, say, HTML. No need to worry about closing off brackets.
But Markdown still has built in syntax to address formatting:

#Header 1
##Header 2
###Header 3

Quotes:

>This is an example of a block quote,
>you're able to insert these very easily
>into any given document
>>You can even nest block quotes!
>

Lists are also easy in Markdown:

* one
* two
* three

Finally, you are able to easily indicate code within a paragraph. For example, `foo()`. Amazing right!!?!?!!?
Ok and one last thing for now, blocks of code are also easily written in Markdown:

    :::bash
    $ cd blog/      # root directory for my blog
    $ make devserver    # automatically re-generates site and hosts site locally
    # change something in content or settings
    $ git add --all
    $ git commit -m "committing blog source"
    $ git push origin master    # pushes to my blog-source repo on GitHub
    $ cd output/    # pelican-generated output folder
    $ git commit -am "committing pelican-generated site content"
    $ git push origin master    # pushes to my amygdalama.github.io repo

	
Ok, so this was a lame first post. So be it. But I'm psyched to start using Pelican with Markdown in order to blog here. Stay tuned for some more interesting revelations.
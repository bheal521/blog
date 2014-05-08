Title: Continued Analysis of Pitchfork Reviews
Date: 2014-04-06
Category: Projects
Tags: R, music, Pitchfork
Slug: Continued-Analysis-of-Pitchfork-Reviews
Author: Ben Healy
Summary: Does Pitchfork penalize bands that aren't new?

The last few days I've looked over a lot of great information on natural language processing and sentiment analysis. There are plenty of really great examples 
of how this has been done. Many of the [examples](http://www.sjwhitworth.com/sentiment-analysis-in-python-using-nltk/) I found dealt with classifying tweets 
as negative or positive. But this same classification of text and machine learning is how something like spam-email works. Ultimately, what I'd like to do is build 
a model that learns to predict the score given to a Pitchfork review by analyzing its text. I've started working on it, but think that it's going to take some 
serious effort to figure out how to best train the model on the ~10,000 reviews I have in my database in order to look at new reviews and correctly classify 
the score.

But before really diving into some more serious natural language processing and machine learning, I thought I'd look for an answer to a question I've had 
about Pitchfork for a while. That is, if a band that has been reviewed by Pitchfork before comes out with additional albums, are those albums penalized in score
for not being new enough? For example, there is a band called [Sleigh Bells](http://pitchfork.com/artists/28390-sleigh-bells/) that have had three of their
albums reviewed by Pitchfork. Their first album, [Treats](http://pitchfork.com/reviews/albums/14251-treats/), was released in 2010 and brought this new 
*BIG* sound that was described by the reviewer as music that,

 >>>just seemed bigger than it had before, 
 >>>like it took up more space and hit  
 >>>with more force and went further than 
 >>>once seemed possible.
 
 The writer reviewed the album very favorably and awarded it an 8.7, enough to get it on the [Best New Music](http://pitchfork.com/reviews/best/albums/) portion of the website, which I'm sure
 had lots of benefits in terms of gaining new listeners. I know that is where I first saw them. But Sleigh Bells released two more albums in the three years that
 followed and received an 8.2 and then a 5.9. Now, just because a band created a great album does not mean that all albums after it will also be great. I realize
 this and also understand that the reviewing of music is about as subjective as it gets... But I believe that a band that creates a first album worthy of a 
 high Pitchfork rating is more likely to do so again in future work. In this specific example, I don't even disagree on the order in which
 the albums are ranked. As a Sleigh Bells fan, I think they got progressively worse. But I have a tough time rationalizing a drop from 8.2 on their 
 [second album](http://pitchfork.com/reviews/albums/16297-reign-of-terror/) to a 5.9 on their 
 [third](http://pitchfork.com/reviews/albums/18594-sleigh-bells-bitter-rivals/). The big change over this three year period was Sleigh Bell's steady 
 climb into main steam music. My hypothesis was that Pitchfork penalizes bands with abnormally low scores after their initial releases due to the fact those
 bands become known and *so0o0o mainstream bro*.
 
To test my hypothesis, I first looked at the bands that had been reviewed the most on Pitchfork. Why, you ask? Well -- it doesn't really provide any useful
information in answering my question but I was sorta wondering... and it's my blog post so I'll do what I want! The table below has the bands that have
had at least 10 albums reviewed by Pitchfork along with their average score and average word length of the reviews written on them.

| Artist          |# Albums Reviewed| Average Score|Average Review Word Count|
|----------------:|:----------------|:-------------|:------------------------| 
|Animal Collective| 10              |7.9           |769                      |
| Guided By Voices| 10              |6.8           |836                      |
| Lil Wayne       | 10              |6.6           |807                      |
| Mogwai          | 10              |6.9           |670                      |
| R.E.M.          | 11              |8.2           |883                      |
| Xiu Xiu         | 11              |7.1           |709                      |
| Four Tet        | 12              |7.5           |748                      |
| Robert Pollard  | 15              |5.9           |615                      |
| The Beatles     | 19              |9.1           |978                      |

Xiu Xiu was definitely a surprise for me, I didn't realize they had so much music out... Also, remember that this is just the most recent 10,000 music reviews
on the site so it is entirely possible that some of these bands have additional albums that were reviewed very early on in Pitchfork's history that I did not
scrape. It is clear that R.E.M. is given lots of respect, but nobody touches The Beatles, cuz duh.

But back to my question. In order to see whether or not bands got progressively worse scores the more albums they came out with, I plotted albums by their
release number (a band's n*th* album) and the score it received. As is expected, the number of data points drops off as you get to higher numbered album releases.
This is because, by definition, every band that has a review on Pitchfork has a first album, but fewer have a second album. Even fewer have a third album that was
reviewed, and so on. By the time we get out past ten, the only bands for which there are data points are the ones included in the table above. With that in mind,
take a look:

<img src="https://raw2.github.com/bheal521/bheal521.github.io/master/images/pitchfork_bias.png" alt="Pitchfork-bias" width="100%", height="110%">

The dots plotted in black represent all of the album reviews, and the larger blue dots represent the average score given to that album number. For example,
the average score given to a band's 9th album reviewed on Pitchfork was just shy of 8. While it's hard to be confident in any findings to the right half of 
the graph, it's interesting to see that the average score is actually increasing slightly as we go from a band's first album, to their second, all the 
way through their 6th. Looks like I was wrong. 

## Does Pitchfork Give More Words to Higher Rated Bands?##

While looking at the word count of the various writers at Pitchfork, I began to wonder if Pitchfork reviews were longer for bands they rated highly
and shorter for others. The graph below plots all of the bands reviewed by Pitchfork by their average review score versus the average word count for their
reviews. The line in blue running through the graph is a sample regression model to help visualize the relationship. 

<img src="https://raw2.github.com/bheal521/bheal521.github.io/master/images/pitchfork_scoreVSlength.png" alt="Pitchfork-score-vs-length" width="100%", height="110%">

You can see that the bands that are rated the highest definitely seem to get some extra attention. What is most striking, is the cluster of bands hovering
right around a rating of 7 and a word count of about 600. It seems that Pitchfork likely has a suggested length for its reviews, and that the vast majority
of bands are getting scores near 7. This could be for a number of reasons, but I'd imagine that what might seem like a high average for scores is because only
albums and bands that are pre-screened to some extent get selected for a review. Pitchfork isn't just reviewing every album they can get their hands on.

See something interesting here? Any questions or suggestions on further exploration of this data? All feedback is welcome below in the comments, or feel free to 
get in touch with me using the method of your preference on my [contacts page](http://bheal521.github.io/pages/contact.html).
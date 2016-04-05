Title: Hometown Heros
Date: 2016-04-04
Category: Data Visualization
Tags: R, Data viz
Slug: Hometown-Heros
Author: Ben Healy
Summary: Where are college bball players from?

After watching too many hours of college basketball the past few weeks I started
wondering where all these kids were from. And they really are kids -- it's shocking how
young some of them are even though I look like I could be some of their children.

Being somewhat familiar with the recent recruiting strategy for the UMass basketball team,
I started wondering if all colleges had focus areas for recruiting. Or were most successful
schools recruiting in their own back yard? Success being the distinction -- UMass hasn't seen much
of that recently. Or maybe there's a region of the country where all the top talent is coming from?
Are all of the top schools fighting over the talent being produced in one area?

For each of the 68 (64 + play in teams...) that made this year's March Madness tournament, I scraped roster
data from [Sports Reference](http://www.sports-reference.com/cbb/). Then using the ggmaps R package, I geocoded
the hometowns of all of the players and plopped them on a map.

So... what's the deal? Here's a map with all of the players from the US that were in the tournament, shaded by their position:

<img src="https://raw.githubusercontent.com/bheal521/bheal521.github.io/master/images/All-Players-Map.png" alt="All-Players-Map.png" width="100%", height="100%">

Lots of players from the urban areas across the US, not very surprising. Maybe a slight concentration of guards in the Northeast
running through NYC, Philly, and DC -- but overall nothing jumped out at me as being surprising. But this is a map of all of the playersin the 
tournament, not just the good teams. Maybe better players, defined as players from the top seeded teams, were from particular areas of the country?

<img src="https://raw.githubusercontent.com/bheal521/bheal521.github.io/master/images/seed-map.png" alt="Seeded-NCAA-Map" width="100%", height="100%">

Looks like a group of solid players, or at least players on solid teams, are from the midwest. Wisconsin, Indiana, Illinois, Michigan, don't have very high
population density but have quite a few players in the tournament this year. The majority of them seem to be from 8 seeds or better.

Lastly, I started wondering about individual teams and how widely spread their player's hometowns were. You always hear about the kid that's from the school's 
backyard, grew up a fan, and now is leading them to the Final Four. To get at what I'll call the "Team Spread" metric, I calculated the distance between each possible
pair of a team's American-born players and took the average. This gives the average distance players grew up from each other.

Here are the 68 teams by their average distance between player hometowns....


| College                   |           Team Spread (Miles) |
|---------------------------|-------------------------------|
| northern-iowa             |           156                 |
| villanova                 |           173                 |
| purdue                    |           235                 |
| xavier                    |           353                 |
| middle-tennessee          |           363                 |
| green-bay                 |           363                 |
| chattanooga               |           365                 |
| west-virginia             |           397                 |
| dayton                    |           401                 |
| indiana                   |           426                 |
| fairleigh-dickinson       |           430                 |
| north-carolina            |           454                 |
| syracuse                  |           458                 |
| holy-cross                |           522                 |
| butler                    |           560                 |
| michigan-state            |           573                 |
| pittsburgh                |           598                 |
| cincinnati                |           640                 |
| texas-tech                |           655                 |
| south-dakota-state        |           667                 |
| iowa-state                |           691                 |
| southern                  |           712                 |
| oklahoma                  |           715                 |
| texas                     |           727                 |
| fresno-state              |           762                 |
| vanderbilt                |           763                 |
| iowa                      |           765                 |
| hampton                   |           775                 |
| texas-am                  |           793                 |
| north-carolina-asheville  |           844                 |
| wisconsin                 |           894                 |
| north-carolina-wilmington |        1,006                  |
| arkansas-little-rock      |        1,112                  |
| yale                      |        1,171                  |
| virginia-commonwealth     |        1,261                  |
| iona                      |        1,285                  |
| notre-dame                |        1,319                  |
| florida-gulf-coast        |        1,337                  |
| providence                |        1,340                  |
| buffalo                   |        1,350                  |
| stephen-f-austin          |        1,368                  |
| connecticut               |        1,387                  |
| baylor                    |        1,416                  |
| kansas                    |        1,449                  |
| austin-peay               |        1,467                  |
| weber-state               |        1,510                  |
| temple                    |        1,513                  |
| stony-brook               |        1,518                  |
| tulsa                     |        1,521                  |
| michigan                  |        1,523                  |
| miami-fl                  |        1,533                  |
| arizona                   |        1,551                  |
| maryland                  |        1,567                  |
| saint-josephs             |        1,594                  |
| colorado                  |        1,802                  |
| cal-state-bakersfield     |        1,830                  |
| wichita-state             |        1,836                  |
| seton-hall                |        1,838                  |
| duke                      |        1,908                  |
| utah                      |        1,921                  |
| oregon                    |        1,958                  |
| gonzaga                   |        2,067                  |
| virginia                  |        2,174                  |
| kentucky                  |        2,273                  |
| california                |        2,279                  |
| southern-california       |        2,426                  |
| oregon-state              |        2,752                  |
| hawaii                    |        3,704                  |


Northern Iowa! Basically each of these kids slept in the bunkbeds above another teammate... But some top teams are right there at the top of the Team Spread list. All of the 
Final Four teams have a Team Spread of less than 1,000 miles. Villanova is right there in second with a whopping 173 miles. All West Coast teams at the other end of the spectrum, with 
Hawaii coming logically in last. But pretty nuts they have, on average, an additional 1,000 miles between players' hometowns.  

One last set of maps for good measure -- take a look at where the kids are from on the two teams in the finals: 'Nova and UNC (can you tell which is which? ha). If closeness is any indicator of success, I better hurry and 
get some money on the boys from Philly.

<img src="https://raw.githubusercontent.com/bheal521/bheal521.github.io/master/images/Villanova.png" alt="NCAA-Villanova" width="100%", height="100%">


<img src="https://raw.githubusercontent.com/bheal521/bheal521.github.io/master/images/North-Carolina.png" alt="NCAA-UNC" width="100%", height="100%">


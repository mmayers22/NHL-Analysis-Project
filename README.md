# NHL-Analysis-Project
##Goal of project

The goal of this project was to look at how players from different countries tend to play differently in the National Hockey League. Data was extracted for the 2022 season using the undocumented NHL API and transferred to a csv using Python. Data was then visualized using Tableau to draw insights as to how play style differs between nationalities.
## Using the NHL API to extract data
Data was pulled from the API using two separate calls, one for player bio information and one for 2022 stats. The JSON outputs were converted into two pandas dataframes and then joined on player ID. 
## Using Tableau
Tableau was used to look at the average statistics per nationality, mainly focusing on the six most prominent nationalities in the NHL (Finland, Sweden, USA, Canada, Russia, Czech Republic).
## Results
From the visualizations in Tableau, we can see that Russian players tend to be the most prolific scorers, average substantially more goals per game than any other nationality, as well as a higher shooting percentage. Canadian players tend to be the most physical, leading the way in hits and penalty minutes. One note about the tendency for Russian players to score at a higher rate is that only the most talented Russians come to the NHL, as they have a very competitive league in Russia where many of them stay. 
## Insights
These insights can be helpful to a team looking to scout a specific type of player, and can allow them to focus their scouting on certain regions. Although there are outliers in every country, a team looking for a physical player will have the best chance of finding them in Canada, and a team looking for a prolific scorer will have a high chance of finding one in Russia. 

# NBA Player Analysis Project
## This project focuses on analyzing and visualizing NBA player performance data using various key performance indicators (KPIs) and creating insightful visualizations. The following instructions outline the steps required to filter, analyze, and visualize the data effectively.

Data Requirements
NBA player statistics dataset including metrics such as Points per Game (PPG), True Shooting Percentage (TS%), Usage Rate (USG%), Versatility Index (VI), 3-point attempts (3PA), Offensive Rating (ORTG), and Defensive Rating (DRTG).
KPI Definitions
USG% (Usage Rate): Estimate of the percentage of team plays used by a player while on the floor.
TO% (Turnover Percentage): Number of turnovers committed by a player per 100 possessions.
eFG% (Effective Field Goal Percentage): Adjusts for the fact that three-point shots are worth more than two-point shots.
Formula: (FGM + (0.5 x 3PM)) / FGA
TS% (True Shooting Percentage): Measures shooting efficiency, taking into account field goals, 3-point field goals, and free throws.
PPG (Points per Game): Average points scored by a player per game.
VI (Versatility Index): Measures a player’s ability to produce in points, assists, and rebounds.
ORTG (Offensive Rating): Points produced by a player per 100 individual possessions.
DRTG (Defensive Rating): Points allowed by a player per 100 possessions.
Steps and Visualizations
Step 1: Top 10 Players by PPG
Filter Criteria:
Top 10 players with the highest PPG.
Further filter by TS% ≥ 0.61.
Visualization:
Bar chart showing Player, Club, PPG, and TS%.
Step 2: Boston Celtics Player Usage
Filter Criteria:
Players from Boston Celtics (BOS).
New Parameter:
High USG%: > 25
Normal USG%: < 25
Visualization:
Bar chart showing Player, USG%, and VI.
Highlight player(s) with the highest USG%.
Step 3: 3PA vs PPG Scatter Chart
Filter Criteria:
Top 5 players with the highest 3PA.
Visualization:
Scatter chart with Club as the x-axis, 3PA as the y-axis, and PPG as the data point size.
Identify top-ranking players.
Step 4: OFFDEF Analysis
New Column:
OFFDEF = ORTG + DRTG.
Data Cleaning:
Ensure accuracy and consistency of the data.
Average Calculation:
Calculate the average OFFDEF.
New Column:
OFFDEF Status:
High Performer: OFFDEF > average
Low Performer: OFFDEF ≤ average
Visualization:
Bar chart showing the number of High Performers and Low Performers.
Explanation of the distribution.
Conclusion
This project provides a structured approach to analyzing NBA player performance data, focusing on key metrics and visualizations to uncover valuable insights.

# DASHBOARD

![Sales_Dashboard](https://github.com/EsraaAh00/My_Projects/assets/159416426/3a036952-6b4a-40be-8251-47f2b07f07a8)



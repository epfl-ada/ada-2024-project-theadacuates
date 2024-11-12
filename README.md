# ada-2024-project-theadacuates
# Pepito vs Cajal: A battle to prove Wikispeedia's Cognitive Fatigue


## Abstract
Recent research suggests that attention spans are decreasing, with cognitive fatigue occurring within minutes of sustained focus [(1)](https://doi.org/10.1111/psyp.12339). Such rapid onset of fatigue is linked to cognitive load theory, which proposes that complex information processing can overwhelm working memory, reducing engagement and performance. This project investigates **Wikispeedia game** engagement from a neuroscientific perspective, focusing on how article complexity, structure, and article network connectivity influence player navigation and performance.
Through this analysis, we aim to develop metrics for assessing cognitive load and mental fatigue. 
Insights from our study could help us understand human web-browsing behavior and information retrieval in networked data, such as Wikipedia, offering a deeper look into the cognitive processes involved in these human information-seeking patterns [(2)](https://dl.acm.org/doi/10.1145/2187836.2187920).

Our data story follows the journey of Pepito, a neuroscience student struggling 
with the Wikispeedia game, and his skeptical supervisor Dr. Cajal. Pepito claims that his poor performance in the game stems from the game's cognitive complexity, which causes mental fatigue. To support his claim, Pepito sets out to analyze gameplay data, hoping to show the impact of cognitive load on players' performance.
However, Dr.Cajal is not buying Pepito's explanation, thinking Pepito 
is simply not good at playing the game. Our narrative will present the 
contrasting views, looking into whether the game 
truly causes a significant cognitive strain, or if Pepito's struggle reflects individual factors.

Can Pepito’s brain handle the game, or will he need a "cognitive reset"?

## Main Questions and Methods

We would like to tackle the following questions in our analysis and use the relevant methods:

- **How do simple metrics influence gameplay and mental fatigue in the game?**
    - We hypothesize that simple metrics like *time per path* and *path length* could serve as proxies for mental fatigue. Repeated tasks over extended periods (time) or increasingly complex paths (length) can lead to confusion, which may negatively impact engagement and flow in the game.

- **How does article complexity impact user gameplay, particularly regarding whether the player will abandon or continue toward the target link?**
    - In this case, *Readability metrics*—which assess the ease with which a text can be read and understood by evaluating factors like sentence structure and word difficulty—will be used to measure how well the player comprehends the article. We are specifically looking at the *Flesch-Kincaid Grade Level, Gunning Fog Index, Automated Readability Index, Simple Measure of Gobbledygook,* and *Coleman-Liau Index*.

- **Can we measure player confusion and indecision during the game and use this measure to predict game abandonment?**
    - We propose that a reasonable measure of confusion and indecision is *Entropy*. We are calculating *Shannon Entropy*, which measures the unpredictability or randomness in user transitions from one article to another. We assume that high entropy can indicate mental fatigue due to unclear path choices. The analysis will be performed first at the individual article level and then averaged across the entire path to assess the entropy of the articles that constitute the path.
    - Since entropy could be biased by the high number of connections an article may have, and thus not be a good proxy for indecision, we will also examine graph connectivity. Along with general connectivity analysis (in-degree, out-degree, closeness, centrality, etc.), we will study the evolution of path degree as the path progresses, to determine if hub articles play a role in guiding user navigation.

- **Switching between knowledge categories (e.g., science to arts) requires *cognitive shifting*, which can increase cognitive load. But is the level of shift high enough in the game to make this effect visible?**
    - We will first quantify cognitive shifting with a high-level approximation, i.e., how many times the category of articles switches between consecutive articles in the path.
    - Additionally, we will examine the evolution of semantic similarity throughout the paths, which we consider a more explanatory index. We will investigate whether players tend to take larger semantic similarity gaps or proceed in a more linear fashion.

- **Does page structure (e.g., headings, multimedia) affect time spent, back-clicks, or path abandonment?**
    - Humans are naturally inclined to conserve energy, a behavior that can be observed in their choice of where to click. We hypothesize that links at the beginning of a page will be clicked more often, reflecting a neurological bias toward selecting direct, less effortful paths rather than optimal ones.
    - Lastly, we will analyze the HTML structure to understand the distribution of clicked links across different webpage elements (e.g., tables, paragraphs). Since images and color naturally capture human attention, we suspect that players may be biased toward clicking on links within these elements, even if they are not the most optimal choices for reaching the target link.

## Additional Datasets
There are no direct additional datasets.

## Timeline and organisation:

- Week 1: Finalize the narrative. Work on Pepito and Carjal's dialogue to clearly present their arguments and justify each step of the analysis. (Homework2 week)
- Week 2: Work on data analysis, and get the first versions of the result and plots. Begin web page development.(Homework2 week)
- Week 3: Peer review the analysis, unify the plot styles and improve descriptions and visual appeal.
- Week 4: Finish web page.
- Week 5: He hope to be pretty much done and leave this week for minor details. Many members of the team are traveling the last week. 

We will work always together on the differt stemps, meeting once/twice weekly.

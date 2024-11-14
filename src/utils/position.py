from collections import Counter, defaultdict
import pandas as pd

def group_categories(parents_dict: dict):
    # group structural categories
    return {
        'heading': parents_dict.get('h1', 0) + parents_dict.get('h2', 0) + parents_dict.get('h3', 0),
        'paragraph': parents_dict.get('p', 0),
        'table': parents_dict.get('table', 0) + parents_dict.get('NavFrame', 0),
        'list': parents_dict.get('ul', 0) + parents_dict.get('ol', 0) + parents_dict.get('dl', 0),
        'infobox': parents_dict.get('thumbcaption', 0),
        'footer': parents_dict.get('footer', 0),
        'undefined': parents_dict.get('undefined', 0)
    }

def get_parents_distribution(df_position: pd.DataFrame):
    # count the number of all navigation links' parent
    count_all_nav_parents_group = defaultdict(int)

    for parents in df_position['all_nav_parents']:
        for nav_parents in parents:
            for k, v in nav_parents.items():
                count_all_nav_parents_group[k] += v
                # count_all_nav_parents_group[k] += v / len(nav_parents)

    # count the number of the target links' parent
    count_target_parents_group = defaultdict(int)
    for parents in df_position['target_parents']:
        for nav_parents in parents:
            for k, v in nav_parents.items():
                count_target_parents_group[k] += v
                # count_target_parents_group[k] += v / len(nav_parents)



    target_parents_group_categories = group_categories(count_target_parents_group)
    all_nav_parents_group_categories = group_categories(count_all_nav_parents_group)

    df_target_parents_group_categories = pd.DataFrame.from_dict(target_parents_group_categories, orient='index', columns=['count'])
    df_all_nav_parents_group_categories = pd.DataFrame.from_dict(all_nav_parents_group_categories, orient='index', columns=['count'])

    return df_target_parents_group_categories, df_all_nav_parents_group_categories

def get_position_distribution(df_position: pd.DataFrame):
    # flatten the number of navigation links
    num_nav_links_group = [num for navs in df_position['num_nav_links'] for num in navs]
    # flatten the number of positions
    positions_group = []

    for positions in df_position['path_positions']:
        for position in positions:
            if isinstance(position, list):
                positions_group.extend({'position': pos, 'count': 1 / len(position)} for pos in position)
                # positions_group.extend({'position': pos, 'count': 1 / len(position)} for pos in position)
            else:
                positions_group.append({'position': position, 'count': 1})
    # # count the frequency
    sr_num_nav_links = pd.Series(Counter(num_nav_links_group).values(), index=Counter(num_nav_links_group).keys())
    df_positions_group = pd.DataFrame(positions_group)

    # remove the position -1
    # sr_positions_group.drop(index=-1, inplace=True)
    df_positions_group = df_positions_group.groupby('position').agg({'count': 'sum'}).reset_index()

    # create cumulative sum of each navigation links position
    cum_nav_links = []
    for i in sr_num_nav_links.index:
        for position in range(1, i):
            cum_nav_links.append({'position': position, 'count': 1 / i})
        # sr_cum_nav_links.append(sr_num_nav_links[sr_num_nav_links.index >= i].sum())

    # sr_cum_nav_links = pd.Series(sr_cum_nav_links, index=range(1, max(sr_num_nav_links.index)+1))
    df_cum_nav_links = pd.DataFrame(cum_nav_links)
    df_cum_nav_links = df_cum_nav_links.groupby('position').agg({'count': 'sum'}).reset_index()

    return sr_num_nav_links, df_positions_group, df_cum_nav_links

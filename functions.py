import seaborn as sns


def sns_lineplot(markets, markets_names):
    """
    Function to create a line plot of the market data.
    markets: list of dataframes
    markets_names: list of market names
    """
    for i, v in enumerate(markets):
        # Plot volume of each pair
        
        plot = sns.lineplot(x=v.index, y=v['Volume'], label = markets_names[i], height=5, aspect=1.5)
        plot.set_xlabel('Index')
        plot.set_ylabel('Volume')
        plot.set_title('Most recent dates are towards the origin')
        # plot.set(rc={"figure.figsize":(10, 10)}) #width=3, #height=4
        # set size of plot
   

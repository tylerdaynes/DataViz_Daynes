if __name__ == '__main__':
    import pandas as pd
    from matplotlib import pyplot as plt
    import squarify as sq
    import dataimport  # module that collects data from the csv file

    color_list = ['#0082bb',
                  '#248dc6',
                  '#3797d1',
                  '#47a2dc',
                  '#56ade8',
                  '#64b8f3']

    color_list1 = ['#0082bb',
                   '#298fc9',
                   '#409dd7',
                   '#53aae5',
                   '#64b8f3']

    # Color scale from https://learnui.design/tools/data-color-picker.html#single

    # Volume Plot
    dictionary = dict(zip(dataimport.categories, dataimport.V_sum))
    df = pd.DataFrame.from_dict(dictionary, orient='index', columns=['Value'])
    df = df.sort_values(by=['Value'], ascending=False)
    df['Color'] = color_list

    plt.figure(figsize=(7.5, 5.5))
    plt.pie(df.Value, labels=df.index, autopct='%1.1f%%', startangle=18,
            colors=color_list, pctdistance=0.85)
    circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(circle)
    text = f'Total Water Used: {round(df.Value.sum(), 2):,} Gallons'
    plt.text(0, 0, text, ha='center', wrap=True)
    plt.axis('equal')
    plt.title('Total Water Use')

    plt.tight_layout()
    plt.savefig('./Plots/TotalVolume.png')
    plt.show()

    # Volume plot without Irrigation
    df = df.drop(labels='Irrigation')
    df.Color = color_list1

    plt.figure(figsize=(7.5, 5.5))
    plt.pie(df.Value, labels=df.index, autopct='%1.1f%%', startangle=60,
            colors=color_list1, pctdistance=0.85)
    circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(circle)
    plt.text(0, 0, text, ha='center', wrap=True)
    plt.axis('equal')
    plt.title('Total Water Use Excluding Irrigation')

    plt.tight_layout()
    plt.savefig('./Plots/TotalVolumeIrr.png')
    plt.show()

    # Duration plot
    dictionary = dict(zip(dataimport.categories, dataimport.D_sum))
    df = pd.DataFrame.from_dict(dictionary, orient='index', columns=['Value'])
    df = df.sort_values(by=['Value'], ascending=False)
    df['Color'] = color_list

    plt.figure(figsize=(7.5, 5.5))
    plt.pie(df.Value, labels=df.index, autopct='%1.1f%%', startangle=60,
            colors=color_list, pctdistance=0.85)
    circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(circle)
    text = f'Total Equipment Duration: {round(df.Value.sum() / 60, 2):,} Hours'
    plt.text(0, 0, text, ha='center', wrap=True)
    plt.axis('equal')
    plt.title('Equipment Duration')

    plt.tight_layout()
    plt.savefig('./Plots/Duration.png')
    plt.show()

    # Duration without irrigation plot
    df = df.drop(labels='Irrigation')
    df.Color = color_list1

    plt.figure(figsize=(7.5, 5.5))
    plt.pie(df.Value, labels=df.index, autopct='%1.1f%%', startangle=60,
            colors=color_list, pctdistance=0.85)
    circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(circle)
    text = f'Total Equipment Duration: {round(df.Value.sum() / 60, 2):,} Hours'
    plt.text(0, 0, text, ha='center', wrap=True)
    plt.axis('equal')
    plt.title('Equipment Duration Excluding Irrigation')

    plt.tight_layout()
    plt.savefig('./Plots/DurationIrr.png')
    plt.show()

    # Mean volume plot
    dictionary = dict(zip(dataimport.categories, dataimport.V_mean))
    df = pd.DataFrame.from_dict(dictionary, orient='index', columns=['Value'])
    df = df.sort_values(by=['Value'], ascending=False)
    df = df.drop(labels='Irrigation')
    df['Color'] = color_list1
    # labels = list(zip(df.index, df.Value.round(decimals=2)))
    labels = ['%s\n %.1f Gallons' % label for label in zip(df.index, df.Value.round(decimals=1))]

    sq.plot(sizes=df.Value, label=labels, color=color_list, pad=True)
    plt.axis('off')
    plt.title('Average Water Volume Used by Equipment')

    plt.tight_layout()
    plt.savefig('./Plots/VolumeAVG.png')
    plt.show()

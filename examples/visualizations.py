import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


# Part 1 - Methods for visualization for basic usage of PyREPO library
# bar chart for basic version
def plot_barplot(df_plot):
    """Visualization method to display column chart of alternatives rankings obtained with 
    different methods.

    Parameters
    ----------
        df_plot : DataFrame
            DataFrame containing rankings of alternatives obtained with different methods.
            The particular rankings are contained in subsequent columns of DataFrame.
    """
    step = 1
    list_rank = np.arange(1, len(df_plot) + 1, step)

    ax = df_plot.plot(kind='bar', width = 0.8, stacked=False, edgecolor = 'black', figsize = (9,4))
    ax.set_xlabel('Alternatives', fontsize = 12)
    ax.set_ylabel('Rank', fontsize = 12)
    ax.set_yticks(list_rank)

    ax.set_xticklabels(df_plot.index, rotation = 'horizontal')
    ax.tick_params(axis = 'both', labelsize = 12)
    y_ticks = ax.yaxis.get_major_ticks()
    ax.set_ylim(0, len(df_plot) + 1)

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
    ncol=4, mode="expand", borderaxespad=0., edgecolor = 'black', title = 'Methods', fontsize = 12)

    ax.grid(True, linestyle = ':')
    ax.set_axisbelow(True)
    plt.tight_layout()
    plt.savefig('./output/' + 'bar_chart' + '.png')
    plt.show()


# bar chart for sensitivity analysis in basic version
def plot_barplot_sensitivity(df_plot, method_name, criterion_name):
    """Visualization method to display column chart of alternatives rankings obtained with 
    modification of weight of given criterion.

    Parameters
    ----------
        df_plot : DataFrame
            DataFrame containing rankings of alternatives obtained with different weight of
            selected criterion. The particular rankings are contained in subsequent columns of 
            DataFrame.
    """
    step = 1
    list_rank = np.arange(1, len(df_plot) + 1, step)

    ax = df_plot.plot(kind='bar', width = 0.8, stacked=False, edgecolor = 'black', figsize = (9,4))
    ax.set_xlabel('Alternatives', fontsize = 12)
    ax.set_ylabel('Rank', fontsize = 12)
    ax.set_yticks(list_rank)

    ax.set_xticklabels(df_plot.index, rotation = 'horizontal')
    ax.tick_params(axis='both', labelsize=12)
    y_ticks = ax.yaxis.get_major_ticks()
    ax.set_ylim(0, len(df_plot) + 1)
    ax.set_title(method_name + ', modification of ' + criterion_name + ' weights')

    plt.legend(bbox_to_anchor=(1.0, 0.82, 0.3, 0.2), loc='upper left', title = 'Weights change', edgecolor = 'black', fontsize = 12)

    ax.grid(True, linestyle = ':')
    ax.set_axisbelow(True)
    plt.tight_layout()
    plt.savefig('./output/sensitivity_analysis_results/' + 'sens_' + 'hist_' + method_name + '_' + criterion_name + '.png')
    plt.show()


# plot line chart for sensitivity analysis in basic version
def plot_lineplot_sensitivity(data_sens, method_name, criterion_name):
    """Visualization method to display line chart of alternatives rankings obtained with 
    modification of weight of given criterion.

    Parameters
    ----------
        df_plot : DataFrame
            DataFrame containing rankings of alternatives obtained with different weight of
            selected criterion. The particular rankings are contained in subsequent columns of 
            DataFrame.
    """
    plt.figure(figsize = (6, 3))
    for j in range(data_sens.shape[0]):
        
        plt.plot(data_sens.iloc[j, :], linewidth = 2)
        ax = plt.gca()
        y_min, y_max = ax.get_ylim()
        x_min, x_max = ax.get_xlim()
        plt.annotate(data_sens.index[j], (x_max, data_sens.iloc[j, -1]),
                        fontsize = 12, style='italic',
                        horizontalalignment='left')

    plt.xlabel("Weight modification", fontsize = 12)
    plt.ylabel("Rank", fontsize = 12)
    plt.yticks(fontsize = 12)
    plt.xticks(fontsize = 12)
    plt.title(method_name + ', modification of ' + criterion_name + ' weights')
    plt.grid(True, linestyle = ':')
    plt.tight_layout()
    plt.savefig('./output/sensitivity_analysis_results/' + 'sens_' + 'lineplot_' + method_name + '_' + criterion_name + '.png')
    plt.show()


# heat maps with correlations for basic version
def draw_heatmap(df_new_heatmap, title):
    """
    Visualization method to display heatmap with correlations of compared rankings generated using different methods
    
    Parameters
    ----------
        data : DataFrame
            DataFrame with correlation values between compared rankings
        title : str
            title of chart containing name of used correlation coefficient
    """
    plt.figure(figsize = (8,5))
    sns.set(font_scale=1.4)
    heatmap = sns.heatmap(df_new_heatmap, annot=True, fmt=".2f", cmap="PuBu",
                          linewidth=0.5, linecolor='w')
    plt.yticks(va="center")
    plt.xlabel('Methods')
    plt.title('Correlation: ' + title)
    plt.tight_layout()
    plt.savefig('./output/' + 'correlations_' + title + '.png')
    plt.show()


# radar plot for basic version
def plot_radar(data):
    """
    Visualization method to display rankings of alternatives obtained with different methods
    on the radar chart.

    Parameters
    -----------
        data : DataFrame
            DataFrame containing containing rankings of alternatives obtained with different 
            methods. The particular rankings are contained in subsequent columns of DataFrame.
    """
    fig=plt.figure()
    ax = fig.add_subplot(111, polar = True)

    for col in list(data.columns):
        labels=np.array(list(data.index))
        stats = data.loc[labels, col].values

        angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        # close the plot
        stats=np.concatenate((stats,[stats[0]]))
        angles=np.concatenate((angles,[angles[0]]))
    
        lista = list(data.index)
        lista.append(data.index[0])
        labels=np.array(lista)

        ax.plot(angles, stats, '-D', linewidth=1)
        ax.fill_between(angles, stats, alpha=0.05)
    
    ax.set_thetagrids(angles * 180/np.pi, labels)
    ax.grid(True)
    ax.set_axisbelow(True)
    plt.legend(data.columns, bbox_to_anchor=(1.0, 0.95, 0.4, 0.2), loc='upper left')
    plt.tight_layout()
    plt.savefig('./output/' + 'radar_chart' + '.png')
    plt.show()


def plot_boxplot(data):
    """
    Display boxplot showing distribution of criteria weights determined with different methods.
    Parameters
    ----------
    data : dataframe
        dataframe with correlation values between compared rankings
    """
    
    df_melted = pd.melt(data)
    plt.figure(figsize = (7, 4))
    ax = sns.boxplot(x = 'variable', y = 'value', data = df_melted, width = 0.6)
    ax.grid(True, linestyle = '--')
    ax.set_axisbelow(True)
    ax.set_xlabel('Criterion', fontsize = 12)
    ax.set_ylabel('Preference distribution', fontsize = 12)
    plt.tight_layout()
    plt.show()


def plot_boxplot_old(data, mcda_name):
    """
    Display boxplot showing distribution of criteria weights determined with different methods.
    Parameters
    ----------
        data : DataFrame
            DataFrame with correlation values between compared rankings

        mcda_name : str
            name of MCDA method applied with different distance metrics
    """

    fig, ax = plt.subplots(figsize = (7, 4))
    ax.boxplot(data)
    ax.set_xticklabels(data.columns)
    ax.grid(True, linestyle = '--')
    ax.set_axisbelow(True)
    ax.set_xlabel('Alternatives', fontsize = 12)
    ax.set_ylabel(mcda_name + ' preference distribution', fontsize = 12)
    plt.tight_layout()
    plt.show()


# Part 2 - Methods for visualization for simulations with PyREPO library

# plot box chart of results obtained in simulations
def plot_boxplot_simulation(data, x, y, xtitle, ytitle, title, filename, flag_rotation = True):
    """
    Visualization method to display box chart of results obtained in simulations performed for
    different methods.

    Parameters
    ----------
        data : DataFrame
            DataFrame containing results

        x : str
            Name of column in DataFrame with variable names in axis x on chart

        y : str
            Name of column in DataFrame with variable values in axis y on chart

        xtitle : str
            Name of axis x title

        ytitle : str
            Name of axis y title

        title : str
            Chart title

        filename : str
            Name of file in which chart will be saved

        flag_rotation : bool
            This parameter indicates if text of ticks in axis y has to be rotated (True) or not (False)

    """
    plt.figure(figsize = (9,5))
    ax = sns.boxplot(x = x, y = y, hue = 'Weight change', palette = 'Blues', data = data)
    if flag_rotation:
        ax.tick_params(axis = 'x', labelsize = 12, rotation = 90)
    else:
        ax.tick_params(axis = 'x', labelsize = 12)
    ax.set_xlabel(xtitle, fontsize = 12)
    ax.set_ylabel(ytitle, fontsize = 12)
    ax.grid(True, linestyle = ':')
    ax.set_axisbelow(True)

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
    ncol=4, mode="expand", borderaxespad=0., edgecolor = 'black', title = 'Weights change', fontsize = 12)

    plt.tight_layout()
    plt.savefig('./output/' + filename + '.png')
    plt.show()


# bar chart for simulations
def plot_barplot_simulations(df_plot, xtitle, ytitle, title, filename, wider = False, flag_rotation = True):
    """
    Visualization method to display bar chart of results obtained in simulations performed for
    different methods.

    Parameters
    ----------
        data : DataFrame
            DataFrame containing results

        x : str
            Name of column in DataFrame with variable names in axis x on chart

        y : str
            Name of column in DataFrame with variable values in axis y on chart

        xtitle : str
            Name of axis x title

        ytitle : str
            Name of axis y title

        title : str
            Chart title

        filename : str
            Name of file in which chart will be saved

        wider : bool
            Parameter for customizing location of text over bars on chart

        flag_rotation : bool
            This parameter indicates if text of ticks in axis y has to be rotated (True) or not (False)

    """
    ax = df_plot.plot(kind='bar', width = 0.6, stacked=False, edgecolor = 'black', figsize = (9,5), colormap = 'Blues')
    ax.set_xlabel(xtitle, fontsize = 12)
    ax.set_ylabel(ytitle, fontsize = 12)

    if flag_rotation == True:
        ax.set_xticklabels(df_plot.index, rotation = 90)
    else:
        ax.set_xticklabels(df_plot.index, rotation = 'horizontal')
    #ax.tick_params(axis = 'x', labelsize = 12, rotation = 90)
    ax.tick_params(axis='both', labelsize=12)
    y_ticks = ax.yaxis.get_major_ticks()

    if wider:
        x_offset = -0.115
    else:
        x_offset = -0.075
    y_offset = 0.04

    for p in ax.patches:
        b = p.get_bbox()
        val = "{:.1f}".format(b.y1 + b.y0)        
        ax.annotate(val, ((b.x0 + b.x1)/2 + x_offset, b.y1 + y_offset), fontsize = 8)

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
    ncol=4, mode="expand", borderaxespad=0., edgecolor = 'black', title = 'Weights change', fontsize = 12)

    ax.grid(True, linestyle = ':')
    ax.set_axisbelow(True)
    plt.tight_layout()
    plt.savefig('./output/' + filename + '.png')
    plt.show()

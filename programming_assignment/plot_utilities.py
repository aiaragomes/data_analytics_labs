import pandas as pd
import matplotlib.pylab as plt


def single_graph_layout(ax, ylim, df_train, df_test):
    ax.set_xlim('1980', '1995-7')
    ax.set_ylim(*ylim)
    ax.set_xlabel('Time')
    one_month = pd.Timedelta('31 days')
    xtrain = (min(df_train.index), max(df_train.index) - one_month)
    xtest = (min(df_test.index) + one_month, max(df_test.index) - one_month)
    xtv = xtrain[1] + 0.5 * (xtest[0] - xtrain[1])

    ypos = 0.9 * ylim[1] + 0.1 * ylim[0]
    ax.add_line(plt.Line2D(xtrain, (ypos, ypos), color='black', linewidth=0.5))
    ax.add_line(plt.Line2D(xtest, (ypos, ypos), color='black', linewidth=0.5))
    ax.axvline(x=xtv, ymin=0, ymax=1, color='black', linewidth=0.5)

    ypos = 0.925 * ylim[1] + 0.075 * ylim[0]
    ax.text('1985', ypos, 'Training')
    ax.text('1993', ypos, 'Validation')
    
    
def graph_layout(axes, df_train, df_test):
    
    miny = min( min(df_train.DryWhite.values), min(df_test.DryWhite.values) )*0.9
    maxy = max( max(df_train.DryWhite.values), max(df_test.DryWhite.values) )*1.1
    yrange = (maxy+miny)/4 if maxy > 10 else (miny+maxy)/20
    single_graph_layout(axes[0], [miny, maxy], df_train, df_test)
    single_graph_layout(axes[1], [-yrange, yrange], df_train, df_test)
    df_train.plot(y='DryWhite', ax=axes[0], color='C0', linewidth=0.75)
    df_test.plot(y='DryWhite', ax=axes[0], color='C0', linestyle='dashed', linewidth=0.75)
    axes[1].axhline(y=0, xmin=0, xmax=1, color='black', linewidth=0.5)
    axes[0].set_xlabel('')
    axes[0].set_ylabel('Sales')
    axes[1].set_ylabel('Forecast Errors')
    if axes[0].get_legend(): 
        axes[0].get_legend().remove()
    # ensure that both axes have the same x-range
    xlim = (min(axes[0].get_xlim()[0], axes[1].get_xlim()[0]), 
            max(axes[0].get_xlim()[1], axes[1].get_xlim()[1]))
    axes[0].set_xlim(*xlim)
    axes[1].set_xlim(*xlim)
    
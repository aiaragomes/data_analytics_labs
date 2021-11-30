import pandas as pd
import matplotlib.pylab as plt


def single_graph_layout(ax, ylim, df_train, df_test):
    ax.set_xlim('1990', '2004-6')
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
    ax.text('1995', ypos, 'Training')
    ax.text('2002-3', ypos, 'Validation')
    
    
def graph_layout(axes, df_train, df_test):
    
    single_graph_layout(axes[0], [1300, 2550], df_train, df_test)
    single_graph_layout(axes[1], [-550, 550], df_train, df_test)
    df_train.plot(y='Ridership', ax=axes[0], color='C0', linewidth=0.75)
    df_test.plot(y='Ridership', ax=axes[0], color='C0', linestyle='dashed', linewidth=0.75)
    axes[1].axhline(y=0, xmin=0, xmax=1, color='black', linewidth=0.5)
    axes[0].set_xlabel('')
    axes[0].set_ylabel('Ridership (in 000s)')
    axes[1].set_ylabel('Forecast Errors')
    if axes[0].get_legend(): 
        axes[0].get_legend().remove()
    # ensure that both axes have the same x-range
    xlim = (min(axes[0].get_xlim()[0], axes[1].get_xlim()[0]), 
            max(axes[0].get_xlim()[1], axes[1].get_xlim()[1]))
    axes[0].set_xlim(*xlim)
    axes[1].set_xlim(*xlim)
    
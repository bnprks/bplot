import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def distplot(a, ax=None, log=False, xlim=None, kde=True, hist=True, *args, **kwargs):
    if ax is None:
        ax = plt.gca()
    if log:
        a = np.log10(a)
        xlim = tuple(np.log10(l) if l is not None else None for l in xlim)
    if xlim is not None:
        clip = list(xlim)
        hist_range = list(xlim)
        
        if xlim[0] is None:
            clip[0] = -np.inf
            hist_range[0] = a.min()
        if xlim[1] is None:
            clip[1] = np.inf
            hist_range[1] = a.max()
        
        kwargs.setdefault("kde_kws",{})
        kwargs.setdefault("hist_kws",{})
        kwargs["kde_kws"]["clip"] = tuple(clip)
        kwargs["hist_kws"]["range"] = tuple(hist_range)

        
    orig_patch_end = len(ax.patches)
    ax = sns.distplot(a, kde=kde, hist=hist, *args, **kwargs)
    
    if log:
        if kde:
            x = ax.lines[-1].get_xdata()
            ax.lines[-1].set_xdata(10 ** x)
        if hist:
            for box in ax.patches[orig_patch_end:]:
                x, width = box.get_x(), box.get_width()
                box.set_x(10**x)
                box.set_width(abs(10**(x+width)-10**x))
        ax.set(xscale="log")
        ax.relim()
        ax.autoscale()
    return ax
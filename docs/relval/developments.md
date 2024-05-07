# Development

This page contains a list of development requests and ToDos.

## Ongoing

Ongoing items.

### Beatification of overlay plots

* 1D: Revise line colors and linestyles. Sometimes, especially in case of large error bars, the 
* 1D: Do not put the plot title again in the ratio plot.
* 2D: Can we tweak the plot and legend position so that things are better readable and visible? Currently, the legend sometimes lies on top of the data and the top-left of the plot cannot be seen.

### Take out certain objects

Some detectors have histograms that collect IDs, for instance for some detector sub-modules. Those IDs are not physics observables and subject to conventions. Another example could be track or particle IDs which can change due to randomness underlying the simulation.
If conventions change for any reason or seeds of random number generators differ, a RelVal comparison might assign `BAD` flags to those histograms, which would bias the overall RelVal towards a worse result.
We should think about a strategy of how we can identify those objects, either manually or even automatically.

## Requests

Topics that have been requested but whose development has not been scheduled yet.

## Done

The finished ToDos can be moved here once done.

# Development

This page contains a list of development requests and ToDos.

## Ongoing

Ongoing items.

### Allow annotations for metrics

#### Make it possible to add annotations

The idea is that during the calculation of metrics we can add annotations. The evaluation and computation of the metric happens [here](https://github.com/AliceO2Group/O2DPG/blob/491797a63739131c69cd3b9492942b01bc577350/RelVal/utils/ReleaseValidationMetrics.C#L133-L142).
This gets 2 histograms which are then forwarded to each singe metric (chi2, kolmogorov and num_entries). However, independent of single metrics we might annotations.
```c++
 void evaluate(TH1* hA, TH1* hB, NCCodes::CODE code)
  {
    std::vector<std::string> annotations;
    // check for instance the relative error of hA and hB. Say one has a high rel. errors.
    annotations.push_back("high relative errors");
    for (auto& metric : metricsEnabled) {
      if (!metric) {
        // here is a nullptr so it is not active
        continue;
      }
      metricResults.push_back(metric->evaluate(hA, hB, code));
      // each metric result should know about it
      metricResults.back().annotations = annotations;
    }
  }
```
Of course, the [`MetricResult`](https://github.com/AliceO2Group/O2DPG/blob/491797a63739131c69cd3b9492942b01bc577350/RelVal/utils/ReleaseValidationMetrics.C#L8-L16) struct would need a new member `annotations`.

In fact, once we have that, we can add any annotations anywhere else.

#### Write the annotations to the JSON from ROOT macros

A `json` file is the interface between the ROOT macros and the Python code. Hence, we need to write the annotations into the output of the ROOT macro. This needs to be done [here](https://github.com/AliceO2Group/O2DPG/blob/491797a63739131c69cd3b9492942b01bc577350/RelVal/utils/ReleaseValidation.C#L260-L274).

#### Do something with the annotations during the Python evaluation

Now, when we pick up the `json` file in Python, we can do something with it. What needs to be extended, is the [`Metric` class](https://github.com/AliceO2Group/O2DPG/blob/491797a63739131c69cd3b9492942b01bc577350/RelVal/utils/o2dpg_release_validation_utils.py#L85-L116).


### Beautification of overlay plots

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

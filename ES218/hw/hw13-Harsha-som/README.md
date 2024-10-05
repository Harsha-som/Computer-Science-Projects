## HW 13

> This assignment is graded and will contribute to half of your Friday lab grade.
 
> All data manipulations must be performed using piping operations and `dplyr` functions when possible.


Load the `allen_army_1945_2019.rds` file into your R session. Note that this is a native R data file that is loaded into an R session using the `readRDS()` function.

```r
dat <- readRDS("allen_army_1945_2019.rds")
```

The data file consists of a `POSIX` variable, `time`, and a temperature variable, `temp`, for the *Allen Army Airfield* in Alaska. The time variable is in the GMT timezone (which shares the same time as UTC). You will convert this date/time variable to an Alaskan timezone using the `with_tz()` function (see the [lecture notes](https://mgimond.github.io/ES218/date_objects.html#setting-and-modifying-timezones) on timezones for more details).

You will create a point plot showing **mean yearly temperature** vs. **year** using the `ggplot2` package. This will require some pre-processing of the data before generating the plot. The pre-processing will be appended to the timezone operation.  The plot will map the yearly mean temperature on the y-axis and the year on the x-axis. You will also fit a line to the plot using the `stat_smooth()` function as demonstrated in the first example of the [Combining geometries](https://mgimond.github.io/ES218/ggplot2.html#combining-geometries) section of the lecture notes (use the `lm` method).  

When complete, you will push your R script to this repo on GitHub.


------

In preparation for Friday, read through the [ggplot2 lecture notes](https://mgimond.github.io/ES218/ggplot2.html). Familiarize yourself with the faceting functions (`facet_wrap` and `facet_grid`).

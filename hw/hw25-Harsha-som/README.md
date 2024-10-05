## HW25 

------------

You will complete this assignment in an R Markdown document.

On Friday, you will explore the role that educational attainment plays in explaining the variability in median income values for the 2008-2012 US workforce. The data are aggregated at the county level.

But first, you will need to explore some of the assumptions that will be needed before addressing Friday's theme. In this assignment, you will generate a (spread-level plot)[https://mgimond.github.io/ES218/sl_plot.html#constructing-the-univariate-s-l-plot] of income across levels of educational attainment. You will also generate a pooled residual q-q plot of the data. In generating the latter, you will make use of axes formatting techniques covered in section (15.4.3)[https://mgimond.github.io/ES218/ggplot2.html#axes-labels] to prevent overlapping income values along the axes. A good approach in reducing "clutter" on the axes is to abbreviate the income values by adding the `k` suffix--for example `5k` instead of `5000`.

NOTE 1: The s-l plot maps a continuous variable to the x-axis. Recall that the `width` parameter in `geom_jitter` will adopt the same units as the variable being mapped to the x-axis.  This implies that the `width=` parameter will need to be modified based on the range of values along the x-axis.

NOTE 2: In the lecture notes (chapter 20). I add the `geom_text()` function to the plot. This takes, as a parameter, `y` which indicates the y-coordinate location on the plot where to place the text. This too adopts as units the variable being mapped to the y-axis. If you are struggling in placing the text, that's OK. Simply omit the `geom_text()` element in the plot.

You will add a narrative to your plots where you will:
*  Discuss if the data, as presented to you, is suitable for a proper comparison of mean values across the different levels of educational attainment.
*  Describe any point patterns of interest as one compares the different level of educational attainment in the pooled residual q-q plot. In other words, is there a systematic change in the point pattern with increasing levels of educational attainment? How does this pattern pair up with the s-l plot?


The dataset for this assignment can be found in the `education.csv` file. The `Education` column stores the maximum level of educational attained by those surveyed in the census data. `HS` = High school, `AD` = some college or associate's degree, `BD` = Bachelor's degree and `Grad` = Graduate Or Professional Degree.

For Friday's lab, you should be comfortable in generating the two different s-l plots covered in chapter 20 and the r-f spread plot covered in (19.4)[https://mgimond.github.io/ES218/rf.html#residual-fit-spread-plot]. You should also be prepared in using re-expression techniques (both Tukey and Box-Cox). You want to spend more time analyzing and less time coding. Proficiency is key in wrapping up an analysis by a given deadline.



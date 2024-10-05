## HW 19

> All data manipulation should be completed in a piping operation.

> Be thorough in your write-up. This will make up half of your grade. For example, describe the dataset, the way the data are manipulated for the analysis and the analysis results.

> You are free to use the eda_qq() method or the ggplot() method.

In this assignment, you will compare the temperature values for the city of Shanghai between the 19<sup>th</sup> and 21<sup>st</sup> centuries. For the former, you will include all temperature observations associated with the 1800s and the latter will include all temperature observations associated with the 2000s. You will read the data directly from this course's website via:

```r
dat <- read.csv("https://mgimond.github.io/ES218/Data/Shanghai.csv")
```

The Rmarkdown document should start with a boxplot of your choosing that summarizes temperature values for both centuries, and a discussion summarizing their distributions by highlighting their lower and upper quartiles as well as their median values. 

You will then follow up with a QQ plot (or a Tukey M-D plot if this proves helpful) with the 2000s data on the y-axis and the 1800s data on the x-axis. The goal will be to model the relationship between both batches of temperatures. Seek a parsimonious relationship if possible.

In your write-up, you will describe the overall relationship between both centuries (i.e. is the difference additive, multiplicative or both?). But, you will also address the question: Is the relationship uniform across the full range of values, or does there seem to be different patterns for cooler temperatures than for warmer temperatures? For example, was the jump in temperature between both centuries for colder days the same as was that for the hottest days? Note that addressing this question will strongly benefit from a Tukey M-D plot instead of a QQ plot. Be descriptive in the write-up.

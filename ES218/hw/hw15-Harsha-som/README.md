# HW 15

Next week, we'll be exploring techniques used to analyze univariate data. Many datasets can lend themselves to both multivariate analysis an univariate analysis. The question of interest  is usually what drives the type of analysis. For example, the [Allen Army Airfield](https://home.army.mil/alaska/fort-greely/garrison/directorate-plans-training-mobilization-security-dptms/allen-army-airfield) meteorological dataset used in last week's assignment and group project was explored in a multivariate context (e.g. how does temperature change as a function of some continuous variable such as year?). 

In a univariate analysis, we are focused on the **distribution** of a variable and how this distribution can vary as a function of one or many categories. One such example is how the temperature distributions can differ when explored across months.

In this assignment, you will generate side-by-side [boxplots](https://mgimond.github.io/ES218/ggplot2.html#geom_boxplot) of temperature distributions when grouped by month using `ggplot2`. The temperature values will be mapped to the y-axis and the month values will be mapped to the x-axis. 

In this assignment, you will generate the boxplots in an R Markdown document (Be sure to follow the *Guideline to good Rmarkdown plot layout practices* that you can find near the top of the course's [Moodle page](https://moodle.colby.edu/pluginfile.php/733775/mod_resource/content/12/Good_bad_examples.html)). You will also:

*  Add a third level heading describing the plot being generated (recall that heading orders are defined by one or more`#`)
*  Add a text briefly describing the data. This will include a description of the data (i.e. what does it measure? Where was it measured?) and the range of years it covers (for maximum points, you will use an [inline code chunk](https://mgimond.github.io/ES218/rmarkdown.html#inline-code-chunks) to define the range of years). 
*  Set the [*code folding*](https://mgimond.github.io/ES218/rmarkdown.html#code-folding) option to `hide`.

When you have completed this assignment, save and knit the final version of the Rmd file to an html file, then push this assignment (both the .Rmd file and output .html file) back to your GitHub repo.


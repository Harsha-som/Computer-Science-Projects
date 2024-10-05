## HW 11

-------

### Part A

You will continue working off of last week's Colby spring courses tidy data table.

```{r eval=FALSE}
library(dplyr)
library(tidyr)
library(stringr)
library(lubridate)

# Read data file
dat  <- read.csv("SP2022.csv")
div  <- read.csv("Divisions.csv")

# Create long table
datl <- dat %>% 
  mutate( M   = str_detect(Days, "M"),
          T    = str_detect(Days, "T"), 
          W    = str_detect(Days, "W"), 
          R    = str_detect(Days, "R"), 
          F    = str_detect(Days, "F"),
          Start = ymd_hm(paste("2019/1/1", StartTime))) %>% 
  filter(!is.na(Start)) %>% 
  pivot_longer(names_to = "Day", values_to = "Boolean", cols=c(M, T, W, R, F )) %>% 
  mutate(Day = factor(Day, levels = c("M", "T", "W", "R", "F"))) 
```

Using piping operations, and sticking to functions covered in class (or those available up on the course's website), you will create a table that summarizes the number of classes by day of the week and start hour of the day. You will round the class start time to the beginning of that hour (e.g. if the class starts at `9:30`, you will assign it to the 9 hour time block--note that this is the `hour()` function's default behavior). Your final table structure should look something like this:


| Day  | 8    | 9    | 10   | 11   | 12   | 13   |  ...  |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| M    |      |      |      |      |      |      |       |
| T    |      |      |      |      |      |      |       |
| W    |      |      |      |      |      |      |       |
| R    |      |      |      |      |      |      |       |
| F    |      |      |      |      |      |      |       |



### Part B (Advanced)

If you successfully complete part A, you will note that there are missing time blocks since no courses occur in these time slots. This may be information worth adding to the plot since one might expect to see all time blocks across the columns. A great function from the `tidyr` package that can help fill empty sets of values is `complete`. Using the example outlined in the [course page](https://mgimond.github.io/ES218/tidyr.html#expanding-table-with-missing-sets-of-values) as guidance, add the `complete` function to your piping workflow to fill the missing hour values in the output table.

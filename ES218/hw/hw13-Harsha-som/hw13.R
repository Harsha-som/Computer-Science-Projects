library(dplyr)
library(lubridate)
library(ggplot2)

#retrieve the data 
dat <- readRDS("allen_army_1945_2019.rds")

#change tie zone
dat$time <- with_tz(dat$time, tzone = "US/Alaska")

#extract Year and get mean temp for each year
dat2 <- dat %>% mutate ( "Year" = year(dat$time)) %>% 
  group_by(Year) %>% 
  summarise("mean_yearly_temperature" =  
              mean(temp, na.rm = TRUE))

#plot and fit             
ggplot(dat2, aes(x = Year, y = mean_yearly_temperature, color = )) + 
  geom_point() + ylab("Mean Yearly Temperature") +
  stat_smooth(method = "lm", se = FALSE)




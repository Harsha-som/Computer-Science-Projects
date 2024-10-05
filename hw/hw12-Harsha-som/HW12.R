library(dplyr)
library(tidyr)
dat  <- read.csv("http://mgimond.github.io/ES218/Data/ACS.csv")

#B23006023- Population 25 To 64 Years: Bachelor's Degree Or Higher
#B19013001- median household income 
#B23006001	Population 25 To 64 Years

#create Percent column and reorder in increaisng median income
datPercent <- dat %>% 
  mutate("Bachelor's degree or greater (Percent)" = 
           (B23006023 / B23006001) * 100,
  State = reorder(State, B19013001, median))
  

#boxplot all states 
  boxplot(B19013001 ~ State, datPercent,
            xlab = "State")
    

#scatterplot income versus percent bachelors
plot(B19013001~`Bachelor's degree or greater (Percent)`,
     datPercent , pch=16, ylab="median household income",
     col = rgb(1,0,1,.1))


#filter to only some states
dat2 <- datPercent %>% 
  filter(State %in% c("me", "nh", "vt", "ma", "ri", "ct","ny")) %>% 
  droplevels() 

#boxplot for specified states
boxplot(B19013001 ~ State, dat2)










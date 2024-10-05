library(dplyr)
library(tidyr)
library(stringr)
library(lubridate)

# Read data file
dat  <- read.csv("SP2024.csv")

datl <- dat %>% 
  mutate( M   = str_detect(Days, "M"),
          T    = str_detect(Days, "T"), 
          W    = str_detect(Days, "W"), 
          R    = str_detect(Days, "R"), 
          F    = str_detect(Days, "F"),
          StartTime= ymd_hm(paste("2019/1/1", StartTime)) ) %>% 
  filter(!is.na(StartTime)) %>% 
  pivot_longer(names_to = "Day", values_to = "Boolean", cols=c(M, T, W, R, F )) %>% 
  mutate(Day = factor(Day, levels = c("M", "T", "W", "R", "F"))) 
  select(c(M,T,W,R,F,StartTime)) %>% 
  
part_a <- datl %>% 
    mutate(Hour = hour(StartTime)) %>%  # Note 2
    group_by(Hour, Day) %>%                             
    summarise(Total = sum(Boolean, na.rm = TRUE)) %>%               
    pivot_wider(names_from = Hour, values_from = Total)



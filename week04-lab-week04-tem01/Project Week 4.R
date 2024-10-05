library(dplyr)
library(tidyr)
library(stringr)

data <- read.csv("rent_2015.csv")
data2 <- read.csv("rent_2020.csv")

converted_numeric <-  as.numeric(data$Geo_FIPS) 

#finding the character result in the geo_fips col then changing to double
data$Geo_FIPS[is.na(converted_numeric) ]
data$Geo_FIPS[is.na(converted_numeric) ] = NA
data$Geo_FIPS <- as.double(data$Geo_FIPS) 

#joining, pivoting and mutating the data to add year rooms and rent variables
dat.long <-  data %>%
  left_join(data2, by = "Geo_FIPS") %>%
  pivot_longer(cols = c("SE_T006_001.y","SE_T006_002.y","SE_T006_003.y",
                        "SE_T006_004.y","SE_T006_005.y","SE_T006_001.x","SE_T006_002.x",
                        "SE_T006_003.x", "SE_T006_004.x", "SE_T006_005.x"), 
               names_to = "tempRooms", values_to = "Rent") %>%
  mutate(Year = if_else(str_detect(tempRooms, ".x"), 2015, 2020) ) %>% 
  mutate(Rooms = case_when(str_detect(tempRooms, "001") ~ 1,
                           str_detect(tempRooms, ".002") ~ 2,
                           str_detect(tempRooms, ".003") ~ 3,
                           str_detect(tempRooms, ".004") ~ 4,
                           str_detect(tempRooms, ".005") ~ 5)) %>%
  separate_wider_delim(cols = Geo_QNAME.x,
                       delim = ", ",
                       names = c("County", "State")) %>%
  select(-tempRooms, -Geo_QNAME.y, -Geo_NAME.y, -Geo_NAME.x)



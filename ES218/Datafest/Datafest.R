library(dplyr)
library(tidyr)
library(stringr)
library(ggplot2)

dat  <- read.csv("checkpoints_pulse SRS.csv")
items <- read.csv("items SRS.csv")
responses <- read.csv ("responses SRS.csv")
questions_type_percent <- read.csv("Questions Prop 2.csv")
all.file <- read.csv ("W:o mcq.csv")
  
#students who did chapter 2-9
student_all_chp <- responses %>% 
  select(student_id,page, item_type, book, item_type, 
         points_possible, points_earned, review_flag,attempt ) %>% 
  filter (book == 'College / Statistics and Data Science (ABC)') %>% 
  filter(str_detect(page, "Review Questions"  ) ) %>% 
  filter(!str_detect(page, "Chapter 1 Review Questions"  ) ) %>% 
  group_by(student_id) %>% 
  summarise ( Number_Pages_per_student= n_distinct(page) ) %>% 
  filter(Number_Pages_per_student==14)


#chapter 2-9 and expectancy answer!=True
pulse_filtered <- dat %>% 
  filter (book == 'College / Statistics and Data Science (ABC)') %>% 
  filter(chapter_number != "1" ) %>% 
  filter(chapter_number != "2" ) %>% 
  filter (chapter_number <= 10) %>% 
  filter(construct == "Expectancy") %>% 
  filter (!is.na(response))   



#get confidence for students who did ch2-9
student_confidence <- inner_join(pulse_filtered, student_all_chp, 
                                 by="student_id") %>% 
  mutate( "Adjusted Chapter" = chapter_number-1)

average_confidence <- student_confidence %>% 
  group_by(`Adjusted Chapter`) %>% 
  summarise ('Average_Confidence' = mean(response))

final <- inner_join(questions_type_percent, average_confidence, 
                    by = c("chap_num" = "Adjusted Chapter") )

all.df <- inner_join(all.file, average_confidence, 
                        by = c("chap_num" = "Adjusted Chapter") )


plot_data <- data.frame(
  x = c(final$total_mcq_prop, final$plaintext_prop),
  y = c(final$Average_Confidence, final$Average_Confidence),
  group = c(rep("MCQ", length(final$total_mcq_prop)), rep("Plaintext", length(final$plaintext_prop)))
)

# Create funky plot using ggplot2 w/ MCQ and Plaintext
ggplot(plot_data, aes(x = x, y = y, color = group))+
  geom_point() +
  labs(title = "Confidence across Question Types",
       x = "Question Composition (Proportion)",
       y = "Average Confidence Level") +
  theme_minimal() +
  stat_smooth(method = "lm", se = FALSE) 


#plot all with msq
ggplot(all.df, aes(x = total_type, y = Average_Confidence,
                  color = type)) +
  geom_point() + ylab("Average Confidence Level ") +
  stat_smooth(method = "lm", se = FALSE)

no.msq.df <- all.df %>% 
  filter(type != "mcq")

only.mcq.df <- all.df %>% 
  filter(type == "mcq")


#plot all with/o msq
ggplot(no.msq.df, aes(x = total_prop, y = Average_Confidence,
                      color = type)) +
  geom_point() + ylab("Average Confidence Level ") +
  xlab("Proportion of Questions Excluding MCQ")+
  ggtitle("Average Confidence vs. Question Proportion") +
  stat_smooth(method = "lm", se = FALSE)

#plot only  msq
ggplot(only.mcq.df, aes(x = total_prop, y = Average_Confidence,
                      color = type)) +
  geom_point() + ylab("Average Confidence Level") +
  xlab("Proportion of Questions that are MCQ")+
  ggtitle("Average Confidence vs. MCQ proportion") +
  stat_smooth(method = "lm", se = FALSE) 
  



student_avg <- inner_join(student_all_chp, responses, by="student_id") %>%
  select(c("institution_id", "student_id", "chapter_number", "points_possible", "points_earned", "attempt")) %>%
  filter(chapter_number > 1) %>%
  filter(chapter_number<=9) %>%
  group_by(student_id) %>%
  summarise("avg_corr" = mean(points_earned, na.rm=TRUE))

confbystu <- student_confidence%>%
  group_by(student_id)%>%
  summarise("avg_conf"=mean(response))

corr_conf <-inner_join(student_avg, confbystu, by="student_id")
plot(corr_conf$avg_corr, corr_conf$avg_conf)

cor(corr_conf$avg_corr, corr_conf$avg_conf)

#plot student condicen by correctness
ggplot(corr_conf, aes(x = avg_corr, y = avg_conf)) +
  geom_point() + ylab("Average Confidence") +
  ggtitle("Average Confidence vs Proportion Correct")+
  xlab("Proportion Correct") +
  stat_smooth(method = "lm", se = FALSE)


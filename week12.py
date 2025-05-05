
 install.packages("tidyr")
 library(ggplot2)
 library(dplyr)
 library(tidyr)
 library(stringr)
 # Step 1: Read data from the text file
 data <- read.csv("socialmedia.txt", stringsAsFactors = FALSE)
 # Step 2: Split hash tags into individual rows
 hashtag_data <- data %>%
 separate_rows(Hashtags, sep = ",") %>%
 mutate(Hashtags = str_trim(Hashtags))
 # Step 3: Hash tag Frequency Bar Chart
 hashtag_freq <- hashtag_data %>%
 group_by(Hashtags) %>%
 summarise(Frequency = n())
 ggplot(hashtag_freq, aes(x = reorder(Hashtags, Frequency), y = Frequency, fill = Hashtags)) +
 geom_bar(stat = "identity") +
 coord_flip() +
 labs(title = "Hashtag Frequency", x = "Hashtag", y = "Count") +
 theme_minimal()
 # Step 4: Sentiment Pie Chart
 sentiment_freq <- data %>%
 count(Sentiment)
 ggplot(sentiment_freq, aes(x = "", y = n, fill = Sentiment)) +
 geom_col(width = 1) +
 coord_polar(theta = "y") +
 labs(title = "Tweet Sentiment Distribution") +
 theme_void()
 # Step 5: Scatter Plot of Likes vs. Retweets
 ggplot(data, aes(x = Likes, y = Retweets, color = Sentiment)) +
 geom_point(size = 4) +
 labs(title = "Engagement: Likes vs. Retweets", x = "Likes", y = "Retweets")+
 theme_minimal()

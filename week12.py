 # Install necessary packages
 install.packages(c("dplyr", "ggplot2", "gapminder"))
 library(dplyr)
 library(ggplot2)
 library(gapminder)
 #Load the Gapminder Dataset
 data(gapminder)
 head(gapminder) # View the first few rows
 # Exploring the Data
 summary(gapminder)
 # Filter for the year 2007 (the most recent in the dataset)
 gapminder_2007 <- filter(gapminder, year == 2007)
 # View the data for 2007
 head(gapminder_2007)
 #Statistical Analysis
 #Average Life Expectancy by Continent
 life_expectancy_by_continent <- gapminder %>%
 group_by(continent) %>%
 summarize(avg_lifeExp = mean(lifeExp, na.rm = TRUE))
 print(life_expectancy_by_continent)
 # GDPandLife Expectancy Correlation
 cor(gapminder$gdpPercap, gapminder$lifeExp, use = "complete.obs")
 #Linear Regression (Life Expectancy ~ GDP)
 model <- lm(lifeExp ~ gdpPercap, data = gapminder)
 summary(model)
 #Visualization
 #GDP vs. Life Expectancy
 ggplot(gapminder, aes(x = gdpPercap, y = lifeExp)) +
 geom_point(aes(color = continent), alpha = 0.7) +
 scale_x_log10() +
 labs(title = "GDP vs Life Expectancy") +
 theme_minimal()
 #Life Expectancy Over Time (by Continent)
 ggplot(gapminder, aes(x = year, y = lifeExp, color = continent)) +
 geom_line() +
 labs(title = "Life Expectancy Over Time") +
 theme_minimal()
 #GDP vs. Population (2007)
 gapminder_2007 <- filter(gapminder, year == 2007)
 ggplot(gapminder_2007, aes(x = gdpPercap, y = pop)) +
 geom_point(aes(color = continent), alpha = 0.7) +
 scale_x_log10() + scale_y_log10() +
 labs(title = "GDP vs Population (2007)") +
 theme_minimal()

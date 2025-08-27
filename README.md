**Introduction to topic and analysis**
The stock markets of the world are in a constant state of flux due to causes big and small, which
makes for an interesting data set to analyse. In particular, during the past 2 decades, there have
been two big crashes: The crash of 2008, which was due to a housing bubble that burst
amongst other growing factors, the very recent (but perhaps less devastating so far) crash
2020, primarily due to the onset of the COVID-19 pandemic. This makes the decades of 2001-
2010 and 2011-2020 an interesting focus for this report.

Analysis of the stock market is important for understand how regular world occurrences such as
natural disasters, world events such as the Olympics or FIFA, and perhaps more relevant at the
time of this report, pandemics, affect the stock market, which reflects the health of the world
economy as a whole. In its position as one of the strongest, most developed and most
influential countries in the world, the United States of America and the stock markets directly
related to it, such as the Dow Jones Industrial Average and S&P 500, make for good indications
of the overall world economy. Another country of interest would be Germany, which is why the
DAX is another focus of the report, and having hosted the 2010 FIFA World Cup, the JSE Index
under South Africa is another interesting dataset as well.

Before any analysis is done, a few traits that make stock market data a little unique must be laid
out. For one, the stock market is only open, and hence recorded, 5 days a week, so data on
Saturdays and Sundays are non-existent. In my analysis, I initially went about this by analysing
and plotting the data with respect to arbitrary days ranging from 0 to 2330 days (52 weeks * 5
days * 10 years + 2 leap year days = 2602 days, 2330 being the days after data being adjusted
for various factors mentioned later). The reason the data is separated into decades instead of
simply being consolidated into 2001-2020 is because the trends are better shown separately
due to the differences in the rate of increase of stock market value, and to better demonstrate
the crashes that occur in each data set.
The market is constantly updated throughout the day, but only the day closing data was taken
for this report.

**Coding and Data**
The stock market data used in this report was obtained from Yahoo Finance. As certain markets
have days during which data is not collected for various reasons such as public holidays, most
analysis here will occur between the same markets for different time periods (i.e. 2001-2010 vs.
2011-2020). As 2020 only goes up till April (April 7 in the case of the data used here),
comparisons with 2001-2010 data will also only go up to April 7, 2010, which is why the data
was shortened to ~2330 days.


The coding techniques used here involve Python 3, using the numpy and matplotlib modules to
assist with calculating the Fast Fourier transforms (FFTs) and convolutions used to analyse the
data sets. FFTs allow for specific analysis regarding the overall trend and stability of the stock
market. A Fourier transform of a data set represented by the function F(t) is given by:
𝐺(𝑤) = ∫ 𝐹(𝑡)
+∞
−∞
𝑒−𝑖𝑤𝑡𝑑𝑡

Where w is the frequency and t is the time. An FFT allows one to isolate frequencies within a
function and hence allows one to manipulate the data to clearly show trends (low frequency) or
instability (high frequency). In this case, both are important for stock market data. Taking the
real FFT (rFFT) worked better here as the imaginary values obtained from regular FFT didn’t
work as well for the analysis done here.

Convolutions are operations between two functions f(n) and g(m), such that:
𝑓(𝑛) ∗ 𝑔(𝑚) = ∑ 𝑓(𝑛 − 𝑚)𝑔(𝑚)
+∞
𝑚=−∞

Convolutions allow one to correlate data in a way that shows how one is affected by the other.
Since stock markets are very much interlinked in their performance, this is a convincing method
to demonstrate that fact.

A further extension of convolutions is cross-correlation, which allows one to demonstrate the
delay between the effect of one stock market on another. While I was eager to do this between
the DOW and DAX indexes, the differences in market parsing (due to different holidays and
such) made this difficult to achieve. As such, simply just using a convolution here didn’t provide
any additional information that the FFT plots didn’t already provide, but simply confirmed that
the DOW and DAX were indeed closely linked in their performances.
The datetime and Pandas modules were also used to better display the dates used for the stock
market, as using arbitrary days is too vague when analysing market data at different points in
time.

**Analysis and Discussion**
Dow Jones Industrial Average and DAX, trend and stability between 2001-2010
Starting with the decade of 2001-2010, there is a general increase between the years of 2001-
2008 for both the DOW and DAX indexes, but the financial collapse of 2008 severely hampered
the growth of these two markets (and by extension, most of the world’s economy), as can be
seen visually in Figures 1 and 3. Overall, the trend by the end of the decade for both figures
shows a recovering and increasing trend.


While the above is probably common knowledge, the most interesting thing that can be
gleaned from these plots is how interconnected these two economies are. At any point in time,
a sharp change in the DOW index can be noticed in the DAX index only a few days later, and the
converse is true as well, as changes in the DAX index are also reflected in the DOW index if they
occur earlier.

The stability of these two markets during 2001-2010 is also displayed in Figures 5 and 6. The
markets are relatively stable between the years 2003-2008, with the DAX index being relatively
more stable by a few values than the DOW index, but this is simply due to the difference in the
market size that these two indices represent, as the DAX index represents the top 30
companies in Germany, while the DOW index represents the top 30 companies in the United
States. As many of the world’s largest companies are based in the USA, the DOW is inherently
bound to be larger and fluctuate a little more.

Due to the crisis, the indices fluctuate wildly from the overall trend from 2008 onwards.
However, going into 2009 and 2010 onwards, the plots clearly show that the DOW index and
DAX index achieve similar levels of stability to what they had just before the crisis, perhaps due
to government stimulus packages to help recover the economy. While this crisis is known as the
“2008 recession” or similar names, it’s clear again from these plots that the crises has its roots
in 2007. While this is not clear from the trend figures (1,3) it’s clearer in figures 5 and 6 where
the plot starts deviating more and more from the centre as 2007 progressed.

**Dow Jones Industrial Average and DAX, trend and stability between 2011-2020**
The decade of 2011 to 2020, at first glance from any of the figures representing the DOW and
DAX indices during this period (Figures 2, 4, 7, 8), that this decade was overall more stable and
had a greater increase in stock market value, perhaps due to the onset of new technologies
such as the introduction the smartphone that propelled companies such as Apple to the top of
the scoreboard. During this time, the DOW index more than doubled its 2011 value by 2020,
and the DAX index almost doubled its 2011 value by 2020 as well.

The trend by the end of this decade for both markets is a downward trend, due to the onset of
the COVID19 pandemic. A key difference between this trend/crash and the one from 2008 can
be seen within Figures 7 and 8. Before the 2008 crises, both indices very clearly becoming more
unstable, but before the 2020 crash, there is no significant decrease in the stability/increase the
variance of the market. This can be attributed to the fact that the recent crash of 2020 was not
attribute to cumulative negative market effects that built up over the course of a few years, but
rather drastic measures taken to reduce the impact of the pandemic that have also impacted
the market.

Unfortunately, the 2008 crisis may not have been a good preparation for the ongoing pandemic
and its associated effects. The current crisis might last for much longer due to the necessity of
social distancing and preventative measures to halt the spread of the COVID19 virus. As the
circumstances behind the 2008 crisis and the current crisis are different, it isn’t necessarily clear
whether the better economic growth of 2011-2020 will allow the world to recover from the
effects of the pandemic in a relatively quick fashion. Even if the pandemic dies down quicker
than expected, lingering effects of the pandemic such as lost capital and increased
unemployment may still hamper a smooth economic recovery, which is something no recent
stock market data can accurately predict. The last time a pandemic affected the world greatly
was the Spanish Flu of 1919, which occurred in world recovering from a militarised economy
which still relied on heavy governmental influence and the gold standard, which would make
data from that period a poor basis for understanding the current economic situation.

Despite their stability, the markets were still affected by external factors such as the Scottish
Referendum of 2015, Brexit vote of 2016, and Presidential elections of 2012 and 2016. Both
elections see small but sharp increases around November 2012 and 2016, while the Brexit vote
of 2016 might be responsible for the increase in the stock prices of the DOW and DAX, as more
companies may have diverted their operations and purchases from British companies to
American and German ones.

While the DOW index continued its rise from 2015 onwards, the DAX index seems to grow
much slower during 2015-2020. During this time, however, the DAX index is also much less
impacted by the DOW index, as dips and increases in the DOW value don’t seem to affect the
DAX index as much as the years before it, especially compared to 2001-2010.

**JSE, trend and stability between 2007-2010**
While this specific range might seem a little odd, this index represents South Africa’s overall
economic performance, and data before this period was harder to obtain. As the 2010 FIFA
world cup occurred during this period, this allows for an observation on how such a global
event can affect the performance of regional economy.

The JSE index suffered from the 2008 crisis, but this is no different from the DOW and DAX
indices analysed earlier, as such a crisis is bound to affect most of the world in some capacity.
The FIFA world cup, perhaps demonstrated much better in Figure 10, played a part in improving
the state of the JSE index and by extension, South Africa’s economy, as the slope of the plot is
much more pronounced after the World cup begins.

While this is only one example and such events may not always contribute positively to a
country’s economy in the long run, this example does demonstrate how such events can help
boost an economy, and in this case, speed up recovery from market crashes. In this case,
looking at Figure 12 confirms the fact that this was only a temporary boost to the index, which
falls during 2011.

**Conclusion**
For a Physics lab report, analysing stock market data might seem like an odd choice, but it
clearly demonstrates the effectiveness of using Fourier Transforms even in non-Physics
applications. As Physical data tends of be of a similar nature (in that most data can be boiled
down to a combination of various sinusoidal functions), applying FFTs to stock market data
demonstrates how one can similarly apply FFTs to data more relevant to the field of Physics,
such as vibration or radioactive data. For example, the FFT method used to gauge the stability
of the stock market could be used on vibration data (such as earthquakes) to observe the
background vibrations not part of an earthquake, while the parameters used to smooth the
trend could be used to omit these background vibrations.

As for the data analysed here, this report has hopefully demonstrated in some capacity how
FFTs can be used to observe market trends and predict future booms or recessions (such as
how the increasing variance of the 2007 data led to the 2008 recession), and how market
indices are connected to each other in an increasing interconnected world.

**Improvements**
With a better understanding on how to quickly sort the data I used or had I manipulated the
data sets further to better work with each other (say, match the DAX data with the DOW data
so that their array sizes were the same by omitting German holidays from the DOW data, and
American holidays from the German data), I would’ve been able to perform a cross-correlation
on them to demonstrate clearly the time lag in days between these two data sets, as the stock
price plots below do show time lag between these two indices. Even if it’s just by a few days, it
would’ve been interesting to see how long, for example, changes in the Dow Jones index take
to reflect themselves in the DAX index.

In a more comprehensive report, I would’ve additionally done something similar to the JSE/FIFA
World Cup analysis, such as how the Olympics affects developed 1st world economies vs.
developing 3rd world economies when it’s hosted in countries falling under those two
categories, as this would better elaborate on how such a large event can affect economies of
different sizes, and by extension, whether hosting such events does indeed benefit developing
economies or not.

**References**
JSE Stock Index: Yahoo Finance, https://finance.yahoo.com/quote/JSEJF/news?p=JSEJF.
DOW Stock Index: Yahoo Finance, https://finance.yahoo.com/quote/%5EDJI.
DAX Stock Index: Yahoo Finance, https://finance.yahoo.com/quote/%5Egdaxi?ltr=1.
Cox, J. (2020) ‘Goldman says… “unprecedented recovery”’ 14 April. Available at: CNBC,
https://www.cnbc.com/2020/04/14/goldman-downturn-will-be-four-times-worse-than-the-
financial-crisis.html
Singh, M. (2019) ‘The 2007-2008 Financial Crisis in Review’ May 9. Available at:
https://www.investopedia.com/articles/economics/09/financial-crisis-review.asp

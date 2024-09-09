# SIP Analysis: Date vs. Daily Investment Strategies in Sensex-Based Mutual Funds

Welcome to the SIP (Systematic Investment Plan) Analysis repository! This project explores the differences in returns when an investor chooses to invest a fixed amount on a particular date each month versus distributing the investment equally across all market days in that month. The analysis covers historical data for the last 10 years, focusing on two primary examples: a 10-year period and a 5-year period.

## Project Overview

This repository contains Python code, written with assistance from ChatGPT, to compare investment strategies:

1. **Fixed Date Investment**: Investing ₹30,000 on a specific date of the month.
2. **Daily Investment**: Investing an equal amount daily whenever the market is open, such that the total investment in the month sums up to ₹30,000.

The analysis answers questions like:
- Which date of the month historically yields the best returns?
- How does daily investment compare to monthly investments on specific dates?
- And how much is the difference between the best & worst case scenario?

### Key Features

- **Historical Analysis**: Compare investment strategies over different periods, with a focus on 10-year and 5-year intervals.
- **Return Comparison**: Visualize the differences in returns between fixed date investments and daily investments.
- **Customizable**: Users can set any start date within the last 10 years to run their own comparisons.
- **Simplicity**: Assumptions are made to avoid unnecessary complexity, such as ignoring expense ratios, while maintaining fairness across comparisons.

## Results Summary

### 10-Year Analysis (Jan 2015 - Oct 2024)

| Strategy                                   | Total Investment (₹) | Best Return (₹) | Worst Return (₹) | Daily Average Return (₹) |
|--------------------------------------------|-----------------------|-----------------|------------------|--------------------------|
| Investing on Best Date (11th of the Month) | 35,40,000             | 76,00,192       |                  |                          |
| Investing on Worst Date (28th of the Month)| 35,40,000             |                 | 75,61,200        |                          |
| Daily Investment                           | 35,40,000             |                 |                  | 75,82,791                |


**Conclusion**: Over nearly 10 years, the difference in returns between the best and worst dates was less than ₹40,000. This suggests that while some dates perform slightly better, a daily investment strategy yields a return that is neither the best nor the worst. The marginal difference indicates that SIP on a particular date is a reliable strategy, but for those willing to manage the effort, daily investments can slightly optimize returns.

### 5-Year Analysis (Sept 2018 - Oct 2024)

| Strategy                                   | Total Investment (₹) | Best Return (₹) | Worst Return (₹) | Daily Average Return (₹) |
|--------------------------------------------|-----------------------|-----------------|------------------|--------------------------|
| Investing on Best Date (1st of the Month)  | 18,00,000             | 28,76,522       |                  |                          |
| Investing on Worst Date (9th of the Month) | 18,00,000             |                 | 28,44,642        |                          |
| Daily Investment                           | 18,00,000             |                 |                  | 28,54,534                |

**Conclusion**: Over 5 years, the difference in returns between the best and worst dates was less than ₹22,000. The daily investment strategy again falls between the best and worst, proving to be a solid alternative for those looking to spread their investment risk over the month.

## Assumptions

1. **Holiday Adjustments**: If the chosen date for monthly investment falls on a market holiday, the investment is made on the next open market day.
2. **No Expense Ratios Considered**: Expense ratios and other fees are ignored to focus on pure return comparisons.
3. **Equal Monthly Investment**: In the daily investment strategy, the total investment remains the same across all comparisons, ensuring fairness.

## Try It Yourself

You can experiment with different start dates within the last 10 years to analyze how the strategies would have performed in those periods. The code is fully customizable and allows for in-depth comparisons.

## Data (30,000 monthly investment)

### 10 year (9 year 10 month) comparision data

| File Name           | Total Invested    | Acquired Value     | Return %           |
|---------------------|-------------------|--------------------|--------------------|
| Monthly on 11th     |         3540000.0 | 7600192.5124782985 | 114.69470374232482 |
| Monthly on 12th     |         3540000.0 |  7600113.627764122 | 114.69247536056841 |
| Monthly on 24th     |         3540000.0 |  7599207.215813664 | 114.66687050321083 |
| Monthly on 7th      |         3540000.0 |  7598944.331352869 | 114.65944438849913 |
| Monthly on 6th      |         3540000.0 |  7596022.288395225 |   114.576900802125 |
| Monthly on 22th     |         3540000.0 |  7595489.943283245 | 114.56186280461144 |
| Monthly on 23th     |         3540000.0 |   7593587.84748658 | 114.50813128493164 |
| Monthly on 8th      |         3540000.0 |  7592468.601800423 |  114.4765141751532 |
| Monthly on 1th      |         3540000.0 |  7592440.381636972 | 114.47571699539469 |
| Monthly on 14th     |         3540000.0 |    7590378.8218131 | 114.41748084217797 |
| Monthly on 2th      |         3540000.0 |  7590351.021560917 | 114.41669552431969 |
| Monthly on 21th     |         3540000.0 |   7590341.93416433 | 114.41643881820143 |
| Monthly on 3th      |         3540000.0 | 7589718.0274345735 | 114.39881433430999 |
| Monthly on 10th     |         3540000.0 |   7586903.03665268 | 114.31929482069717 |
| Monthly on 5th      |         3540000.0 |   7586259.11531217 |  114.3011049523212 |
| Monthly on 15th     |         3540000.0 |  7586012.375406837 | 114.29413489849821 |
| Monthly on 25th     |         3540000.0 |  7585559.602961378 |  114.2813447164231 |
| Monthly on 4th      |         3540000.0 |  7585299.906089456 | 114.27400864659481 |
| Monthly on 13th     |         3540000.0 |  7585049.859302525 | 114.26694517803745 |
| Monthly on 19th     |         3540000.0 |   7584562.48053697 |  114.2531774162986 |
| Monthly on 16th     |         3540000.0 |  7583668.912069729 | 114.22793536920136 |
| Monthly on 9th      |         3540000.0 |  7583010.651550839 | 114.20934043928924 |
| Daily - open market | 3539999.999999977 |   7582791.05787751 | 114.20313722817963 |
| Monthly on 18th     |         3540000.0 |  7579308.634427364 | 114.10476368438881 |
| Monthly on 26th     |         3540000.0 |  7577619.297979738 |  114.0570423158118 |
| Monthly on 17th     |         3540000.0 |  7575091.638203922 | 113.98563949728593 |
| Monthly on 20th     |         3540000.0 |  7574148.170823956 | 113.95898787638293 |
| Monthly on 27th     |         3540000.0 |  7563549.334904103 | 113.65958573175432 |
| Monthly on 28th     |         3540000.0 |  7561199.724543092 | 113.59321255771445 |

### 5 year comparision data

| File Name           | Total Invested    | Acquired Value     | Return %           |
|---------------------|-------------------|--------------------|--------------------|
| Monthly on 1th      |         1800000.0 | 2876522.1511211935 |  59.80678617339964 |
| Monthly on 2th      |         1800000.0 |  2871416.281276933 | 59.523126737607384 |
| Monthly on 3th      |         1800000.0 | 2868641.9861099278 |  59.36899922832932 |
| Monthly on 22th     |         1800000.0 |  2867443.862121279 |   59.3024367845155 |
| Monthly on 24th     |         1800000.0 | 2866945.9493519827 | 59.274774963999036 |
| Monthly on 21th     |         1800000.0 | 2866457.5602466324 |  59.24764223592402 |
| Monthly on 19th     |         1800000.0 | 2866144.3133323193 |  59.23023962957329 |
| Monthly on 23th     |         1800000.0 | 2863986.2804442593 | 59.110348913569965 |
| Monthly on 25th     |         1800000.0 |  2860244.329480284 |  58.90246274890466 |
| Monthly on 4th      |         1800000.0 |  2860199.449331847 |  58.89996940732483 |
| Monthly on 18th     |         1800000.0 |  2858770.026731574 | 58.820557040642996 |
| Monthly on 5th      |         1800000.0 |   2858010.92746921 |  58.77838485940054 |
| Monthly on 20th     |         1800000.0 | 2856567.6114901486 |  58.69820063834159 |
| Monthly on 14th     |         1800000.0 |  2856432.095400741 | 58.690671966707825 |
| Monthly on 6th      |         1800000.0 |  2855024.934278676 |  58.61249634881532 |
| Daily - open market | 1799999.999999961 |  2854534.240470263 | 58.585235581684735 |
| Monthly on 12th     |         1800000.0 | 2854387.4288096605 |  58.57707937831447 |
| Monthly on 7th      |         1800000.0 |  2854287.400911756 |  58.57152227287533 |
| Monthly on 16th     |         1800000.0 | 2854277.5944054704 |  58.57097746697058 |
| Monthly on 15th     |         1800000.0 | 2854110.8804784063 |  58.56171558213368 |
| Monthly on 17th     |         1800000.0 | 2854011.3309664223 |  58.55618505369013 |
| Monthly on 26th     |         1800000.0 |  2853838.562890989 |  58.54658682727715 |
| Monthly on 8th      |         1800000.0 | 2851219.8125647497 |  58.40110069804165 |
| Monthly on 11th     |         1800000.0 |   2847967.44722783 |  58.22041373487944 |
| Monthly on 13th     |         1800000.0 | 2847472.6560181133 |  58.19292533433962 |
| Monthly on 28th     |         1800000.0 | 2847061.0312864343 |  58.17005729369079 |
| Monthly on 27th     |         1800000.0 |   2846230.80869606 |  58.12393381644778 |
| Monthly on 10th     |         1800000.0 |  2845824.063575301 |  58.10133686529449 |
| Monthly on 9th      |         1800000.0 |  2844642.615082568 |  58.03570083792045 |

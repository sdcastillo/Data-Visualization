---
layout: default
title: Every picture tells a story … don’t it?
description: 2019 SOA symposium slides on communication efficiency and practical data visualization.
samwiki: true
---

<div class="sw-lede-copy" markdown="1">

This is the home for **Every picture tells a story … don’t it?**, the talk Sam Castillo and Brian A. Fannin gave at the Society of Actuaries Predictive Analytics and Futurism Symposium on September 19, 2019. It is a student-era page from Sam Castillo (UMass Amherst Mathematics). The talk is a self-contained reveal.js deck rendered from R Markdown. The grey Futura slides below are that original file.

The first half is about communication efficiency. The same comparison is shown as 11 and 9, then as 1011 and 1001, as the Roman numerals IX and XI, as the Chinese numerals 十一 and 九, as type set at different sizes, and finally as a bar chart. Following Gelman and Unwin, the claim is that statisticians always need a comparison, and that a geometric mark is sometimes read faster than a digit. A five-number summary compresses a simulated sample. A histogram with the mean and a 5%–95% band leaves that reduction to the eye: summary statistics always throw information away, and a chart presents almost all of the data.

Design is treated as part of the sentence. Underlining “increased” versus “territory” in the line “The rate for territory X must be increased by 10.4%” changes which word carries the meaning. A typo — “This year we plan top build on last year’s renewed profitability” — fails a credibility check before any graphic is discussed. The practical half then uses a diet. Nutrition labels are slow to compare because serving sizes differ, units need a calculator, and each food has its own panel. Instacart orders from March through July 2019 are plotted as daily calories and as a percent of a written benchmark: 3,000 calories, 125 grams of protein, 150 grams of fat, and a short list of other nutrients.

Exploration and communication are split on purpose. Exploration wants speed, iteration, many dimensions, and tidy data in R or Python. Communication wants simplicity, consistency, and one house style. An Excel-like ggplot default sits next to a branded theme, and a hospital-readmission density from HealthData.gov is rewritten as a histogram whose vertical axis is a count of hospitals, so a reader can say there are just over 2,000 hospitals with between 30 and 50 readmissions. Color is taken from a wheel and from a brand palette. Uncertainty is a boxplot of the actual-to-expected readmission ratio for Illinois, Massachusetts, North Carolina, New York, and Pennsylvania. The close is three points: exploration favors flexibility, communication favors restraint, and a chart is another form of speech.

</div>

## Key points

- Symposium deck from September 19, 2019, by Sam Castillo and Brian A. Fannin.
- Representation changes speed: digits, Roman and Chinese numerals, type size, then bar length.
- A five-number summary reduces a sample; a distribution shows almost all of it.
- Emphasis, type, and a typo change what the audience believes.
- Diet example: Instacart orders against a daily calorie and nutrient benchmark.
- Hospital readmissions: a density rewritten as a counted histogram, then expected versus predicted rates.
- Build order is import, then transform, then visualize, then one custom theme.
- The original reveal.js file is preserved at `slides/index.html` and embedded below.

## The slides

The frame is the 2019 deck. Arrow keys move through it after you click the frame. The full-screen copy is the same file.

<p><a class="sw-btn sw-btn-live" href="{{ '/slides/' | relative_url }}">Open the slides</a>
<a class="sw-btn sw-btn-source" href="{{ '/index.Rmd' | relative_url }}">R Markdown source</a></p>

<div class="deck-frame">
  <iframe src="{{ '/slides/' | relative_url }}" title="Every picture tells a story, the 2019 symposium slides"></iframe>
</div>

The deck still names the 2019 mirrors it was written for: [pirategrunt.com/soa_symposium_2019](https://pirategrunt.com/soa_symposium_2019/) and [PirateGrunt/soa_symposium_2019](https://github.com/PirateGrunt/soa_symposium_2019). The chart data in this repository are `data/orders.csv`, `data/orders_nutrition.csv`, and `data/hospital_readmission_rates.csv`.

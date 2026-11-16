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

## The comparison, on the page

The opening of the talk asks which number is larger, then changes only the drawing. Digits first. Length second.

<div class="compare">
  <figure>
    <figcaption>As digits</figcaption>
    <div class="compare-digits" aria-label="11 beside 9">
      <span>11</span>
      <span>9</span>
    </div>
  </figure>
  <figure>
    <figcaption>As length</figcaption>
    <div class="compare-bars" role="img" aria-label="A bar of length 11 next to a shorter bar of length 9">
      <div><span class="bar-slot"><i style="height: 100%"></i></span><b>11</b></div>
      <div><span class="bar-slot"><i style="height: 81.8%"></i></span><b>9</b></div>
    </div>
  </figure>
</div>

<p class="compare-note">11 is longer. The numerals still ask for a comparison. The bars finish it.</p>

The same stall shows up when the numerals get long. Read the pair, then the pair with commas:

<div class="numeral-row" aria-label="999999999 beside 99999999999, then the same numbers with commas">
  <span>999999999</span>
  <span>99999999999</span>
  <span>999,999,999</span>
  <span>99,999,999,999</span>
</div>

<p class="compare-note">Commas help. A length still wins. The deck walks this from Roman numerals through a bar chart in <a href="{{ '/slides/' | relative_url }}#/communication-efficiency">Communication efficiency</a>.</p>

## Counted, not waved at

The practical half rewrites a hospital-readmission density as a histogram whose vertical axis is a count. These bars are that count, taken from `data/hospital_readmission_rates.csv` with the slide’s cut: bin width 20, horizontal axis 0 to 300, and “Not Available” left out. Teal marks the two bins a reader uses for “about 30 to 50.”

<figure class="chart-card">
  <img src="{{ '/assets/readmissions-histogram.svg' | relative_url }}" alt="Histogram of hospital-measure rows by number of readmissions. The 20 to 40 bin is tallest at 3,071 rows. The 40 to 60 bin has 1,919. Both are teal. Later bins shrink toward 300.">
</figure>

Of the 11,532 rows with a numeric readmission count, 2,430 fall from 30 through 50. Those rows belong to 1,663 distinct hospitals. The slide looks at this pile and says, in English, that there are just over 2,000 hospitals with between 30 and 50 readmissions. The sentence is the eye’s reading. The axis that makes a sentence possible is a count of rows, not a density.

<details class="bin-table">
  <summary>Bin counts from the file</summary>
  <table>
    <thead>
      <tr><th>Readmissions</th><th>Rows</th></tr>
    </thead>
    <tbody>
      <tr><td>0–20</td><td>2,305</td></tr>
      <tr><td>20–40</td><td>3,071</td></tr>
      <tr><td>40–60</td><td>1,919</td></tr>
      <tr><td>60–80</td><td>1,241</td></tr>
      <tr><td>80–100</td><td>912</td></tr>
      <tr><td>100–120</td><td>581</td></tr>
      <tr><td>120–140</td><td>426</td></tr>
      <tr><td>140–160</td><td>315</td></tr>
      <tr><td>160–180</td><td>204</td></tr>
      <tr><td>180–200</td><td>124</td></tr>
      <tr><td>200–220</td><td>111</td></tr>
      <tr><td>220–240</td><td>85</td></tr>
      <tr><td>240–260</td><td>60</td></tr>
      <tr><td>260–280</td><td>43</td></tr>
      <tr><td>280–300</td><td>36</td></tr>
    </tbody>
  </table>
</details>

<p class="compare-note">Ninety-nine further rows sit at 300 or above and are off this axis, the same window the slides use. Recount with <code>scripts/readmissions_histogram.py</code>. The deck’s counted histogram is the second “easy to read” frame, <a href="{{ '/slides/' | relative_url }}#/the-best-graphs-are-easy-to-read-1">just over 2,000 hospitals</a>. The frame before it is the density the talk throws out.</p>

## In the deck

<p class="sw-jumps">
  <a href="{{ '/slides/' | relative_url }}#/communication-efficiency" target="deck">Communication efficiency</a>
  <a href="{{ '/slides/' | relative_url }}#/this-is-better" target="deck">A thinner bar</a>
  <a href="{{ '/slides/' | relative_url }}#/practical-advice-for-data-visualization" target="deck">Practical advice</a>
  <a href="{{ '/slides/' | relative_url }}#/a-real-life-example-improving-my-diet" target="deck">The diet example</a>
  <a href="{{ '/slides/' | relative_url }}#/the-best-graphs-are-easy-to-read-1" target="deck">Counted histogram</a>
  <a href="{{ '/slides/' | relative_url }}#/showing-uncertainty" target="deck">Uncertainty</a>
  <a href="{{ '/slides/' | relative_url }}#/three-point-summary" target="deck">Three-point summary</a>
</p>

## The slides

The frame is the 2019 deck. Arrow keys move through it after you click the frame. The full-screen copy is the same file.

<p><a class="sw-btn sw-btn-live" href="{{ '/slides/' | relative_url }}">Open the slides</a>
<a class="sw-btn sw-btn-source" href="{{ '/index.Rmd' | relative_url }}">R Markdown source</a></p>

<div class="deck-frame">
  <iframe name="deck" src="{{ '/slides/' | relative_url }}" title="Every picture tells a story, the 2019 symposium slides"></iframe>
</div>

The deck still names the 2019 mirrors it was written for: [pirategrunt.com/soa_symposium_2019](https://pirategrunt.com/soa_symposium_2019/) and [PirateGrunt/soa_symposium_2019](https://github.com/PirateGrunt/soa_symposium_2019). The chart data in this repository are `data/orders.csv`, `data/orders_nutrition.csv`, and `data/hospital_readmission_rates.csv`.

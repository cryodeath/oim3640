# My Project Proposal
## What I'm building: 
A Travel Cost Tracker that lets me log daily expenses while traveling and see breakdowns by day and category.

## Why I chose this:
As someone who travels frequently (most recently a solo trip through Colombia), I always lose track of what I spend on food vs transport vs activities. By the end of a trip I have no idea where my money went. This solves my real problem of understanding where my travel budget actually goes — so I can plan better next time.

## Core features:

Add expenses with a date, category (Food, Hotel, Transport, Activities, Other), amount, and description

View daily totals (e.g., "Mar 15: $287 across 3 expenses")

Category summary with percentages (e.g., "Food: $309 — 45%")

Trip totals and average daily spend

Save and load trip data to/from a JSON file so nothing is lost

## What I don't know yet:

Best way to organize expense data in memory (dictionary of dates → list of expenses?)

How to calculate and display category percentages cleanly

How to handle edge cases like empty trips or invalid dates

Whether to support multiple currencies for international travel
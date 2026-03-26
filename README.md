# AI Trucking Assistant

A Python tool that helps evaluate whether a trucking load is worth taking.

## What it does
This app calculates:
- loaded miles
- deadhead miles
- total miles
- toll cost
- operating cost
- total expense
- estimated profit
- loaded RPM
- all-in RPM

It also gives a final decision:
- TAKE THE LOAD
- MAYBE TAKE IT
- DECLINE THE LOAD

## Why I built it
I built this project to solve a real trucking problem: loads can look good at first, but after deadhead, tolls, and operating cost, they may not be worth taking.

As someone with trucking experience, I wanted a simple decision tool that turns load information into a fast business decision.

## Example decisions
- Strong load = high profit + strong all-in RPM
- Marginal load = profitable but below target
- Weak load = too little profit or bad all-in RPM

## Tech used
- Python

## Future upgrades
- fuel cost estimator
- profit per mile
- profit per hour
- load scoring system
- simple web app version

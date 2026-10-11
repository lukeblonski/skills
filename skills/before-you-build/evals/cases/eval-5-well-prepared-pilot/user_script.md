# Simulated user script for eval-5-well-prepared-pilot

## Opening message

Here is our brief, please check it before we commit:

FleetFox: reduce the time needed to prepare a list of vehicles due for inspection.

Managers of fleets with more than 200 vehicles prepare a weekly list of vehicles due for inspection within the next 14 days. The current vehicle list supports search only by vehicle name and registration number.

In the last 30 days, 168 of 420 active large-fleet managers exported the vehicle list to CSV within five minutes of opening the view. In a sample of 60 sessions, the median time from opening the list to creating a service order was 4 minutes 20 seconds. In 11 of 15 interviews, managers described manually filtering a spreadsheet by branch, vehicle status, and inspection date. Customer Success estimates manual list preparation costs customers in this segment about 90 hours per week in total. Reducing service-planning time is one of this quarter's product goals for enterprise customers.

We hypothesize that combinable filters for branch, status, vehicle type, and inspection date will let managers prepare the list without exporting data. We will first release the filters behind a feature flag to 20 large-fleet managers for two weeks. Filter state must be saved in the URL, and an empty result must offer a way to clear all criteria.

Pilot success criteria: median time from opening the list to creating a service order falls from 4:20 to under 2 minutes; share of sessions with a CSV export in this flow falls from 40% to under 25%; correctly identified vehicles in the controlled task do not fall below 98%; list-response p95 does not regress by more than 200 ms. If both primary criteria are met without violating the guardrails, expand the rollout. If completion time does not improve and users continue to export CSV, return to session evidence and investigate missing data or operations.

## Answers if asked

Cost: "That's all we have; the numbers in the brief are from our analytics and the interviews. I don't have a cost figure." What the 252 non-exporting managers do: "We haven't looked." Anything else: "I don't know, that's everything we have." 


###Special thanks to our corporate sponsors [BrowserStack](https://www.browserstack.com/)  and [Formilla](http://www.formilla.com/).

# The Problem 

[Northbridge](http://northbridgetech.org) is an open-source, decentralized, nonprofit, social-justice software shop that is highly dependent on volunteers to advance our project work. 

This project represents the internal app that all of our other social justice project work depends on.

GitHub provides lots of essential things that are needed in order to collaborate productively in an open-source, decentralized way: self managed user accounts, teams, messaging, task management, and even simple burndown charting. There is one component that Northbridge Technology Alliance needs in order to make GitHub hit the sweet spot of our [agile development methodology](https://github.com/Northbridge/playbook/wiki/1.How-We-Do), and that is backlog management.

We have researched lots of task management tools, and there are some very nice ones available. However they require the construction of a siloed user base. Northbridge needs to work in an agile, backlog-driven fashion and also leverage the public infrastructure and userbase of GitHub, with all of those advantages. This project give us the GitHub-integrated backlog we need in order to do that seamlessly.

####3/22/16 Update

This project was begun Spring, 2015. Happy to report that Alliance has reached a stable and usable codebase. We are using it now for our day-to-day operations. Also, we've containerized our local installation procedures using Vagrant.

Next challenge - we need to create an authentication layer into the application that depends on the Github API. We want to grant access to Alliance to any user who has been placed on a Northbridge team. See a preliminary write-up [here](https://github.com/NorthBridge/alliance-community/issues/63).

# Overview

## The User Interface

This is new work. 

## The Backlog Interface (mostly complete)

When a team selects a user story to accomplish, a button push exports the story into GitHub as a milestone and surfaces it on the burndown chart. Upon completion of the milestone, a GitHub API web hook is used to signal that the story is complete, and our internal backlog is udated accordingly.

There are three major components to Alliance: **web interface**,
**export**, and **import**. These are represented as the yellow
components of this diagram.

- **Web Interface**: Allows Northbridge volunteers to estimate and
  select user stories from a prioritized backlog of work.

- **Export**: When invoked, export all Backlog User Stories in state
  "Selected" from the database to a GitHub Issues list using the GitHub
API.

- **Import**: When invoked, update a Backlog User Story to Accepted.
  This process will respond to a GitHub Issues Webhook.

![Project Diagram](http://northbridgetech.org/images/alliance2.jpg)

## Installation

Curious about contributing? Reach to @kdflint. Installation instructions are currently being reformatted.

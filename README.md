
###Special thanks to our corporate sponsors [BrowserStack](https://www.browserstack.com/)  and [Formilla](http://www.formilla.com/).

###Installation instructions [here](https://github.com/NorthBridge/alliance-community/blob/master/docs/install.md)

# Problem Statement 

[Northbridge](http://northbridgetech.org) is an open-source, decentralized, nonprofit, social-justice software shop that is highly dependent on volunteers to advance our project work. 

This project, Alliance, is our internal task management app. All of our public facing social justice project work is managed with this app.

GitHub provides lots of essential things that are needed in order to collaborate productively in an open-source, decentralized way: self managed user accounts, teams, messaging, task management, and even simple burndown charting. This ubiquitous, free, and public infrastructure is perfect for our volunteer nonprofit work.

There is one component that Northbridge Technology Alliance needs in order to make GitHub hit the sweet spot of our [agile development methodology](https://github.com/Northbridge/playbook/wiki/1.How-We-Do), and that is backlog management.

We have researched lots of task management tools, and there are some very nice ones available. However they require the construction of a siloed user base which is inconvenient and also does not scale well. Northbridge needs to work in an agile, backlog-driven fashion and also leverage the public infrastructure and userbase of GitHub, with all of those advantages. This project give us the GitHub-integrated backlog we need in order to do that seamlessly.

####3/22/16 Update

This project was begun Spring, 2015. Happy to report that Alliance has reached a stable and usable codebase. We are using it now for our day-to-day operations. Also, we've containerized our local installation procedures using Vagrant.

####9/14/16 Update

Our last big challenge is met -- OAuth authentication through GitHub. Now our teams are fully managed in GitHub. We just need to add a user to a Northbridge GitHub team in order for them to see their team's backlog in Alliance. More rationale for this feature is described [here](https://github.com/NorthBridge/alliance-community/issues/63).

# Overview

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


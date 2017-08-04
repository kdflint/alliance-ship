-- SET search_path = volunteer, pg_catalog;

\set email '\'' 'test@test.com' '\''
\set fname '\'' 'admin' '\''
\set lname '\'' 'admin' '\''
\set github_repo '\'' 'test-community' '\''

DELETE FROM team_volunteer;
DELETE FROM volunteer;
DELETE FROM campaign;
DELETE FROM acceptance_criteria;
DELETE FROM backlog;
DELETE FROM team_project;
DELETE FROM project;
DELETE FROM event;
DELETE FROM schedule;
DELETE FROM team;
DELETE FROM status;
DELETE FROM application;
DELETE FROM auth_group_permissions;
DELETE FROM auth_group;

INSERT INTO team (id, focus, name, visibility, task_manager_id) VALUES (1, 'Javascript/HTML', 'North Stars', 'Public', 1);
INSERT INTO team (id, focus, name, visibility, task_manager_id) VALUES (2, 'PythonDjango', '2015 Summer Interns', 'Private', 1);
INSERT INTO team (id, focus, name, visibility, task_manager_id) VALUES (3, 'PythonDjango', 'Alliance Test Team', 'Private', 1);

INSERT INTO schedule (id, name) VALUES (1, 'NorthBridge Standard');

INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (1, 'Sprint 1', '2018-01-11', '2015-02-07', 1);
INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (2, 'Sprint 2', '2018-02-01', '2015-02-28', 1);
INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (3, 'Sprint 3', '2018-02-22', '2015-03-21', 1);
INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (4, 'Sprint 4', '2018-03-15', '2015-04-11', 1);
INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (5, 'Sprint 5', '2018-04-05', '2015-05-02', 1);
INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (6, 'Sprint 6', '2018-04-26', '2015-05-23', 1);
INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (7, 'Sprint 7', '2018-05-17', '2015-06-13', 1);
INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (8, 'Sprint 8', '2018-06-07', '2015-07-04', 1);
INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (9, 'Sprint 9', '2018-06-28', '2015-07-25', 1);
INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (10, 'Sprint 10', '2018-07-19', '2015-08-15', 1);
INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (11, 'Sprint 11', '2018-08-09', '2015-09-05', 1);
INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (12, 'Sprint 12', '2018-08-30', '2015-09-26', 1);
INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (13, 'Sprint 13', '2018-09-20', '2015-10-17', 1);
INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (14, 'Sprint 14', '2018-10-11', '2015-11-07', 1);
INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (15, 'Sprint 15', '2018-11-01', '2015-11-28', 1);
INSERT INTO event (id, name, start_dttm, end_dttm, schedule_id_fk) VALUES (16, 'Sprint 16', '2018-11-22', '2015-12-19', 1);

INSERT INTO campaign (id, name, description, amount_goal, respondent_goal) VALUES (1, 'FriendsAndFamily', 'Friends And Family', 10000, 500);
INSERT INTO campaign (id, name, description, amount_goal, respondent_goal) VALUES (2, 'Indiegogo', 'Indiegogo', 16000, 50);

INSERT INTO status (id, category, name, descr) VALUES (1, 'volunteer', 'inquired', 'Inquired');
INSERT INTO status (id, category, name, descr) VALUES (2, 'volunteer', 'contacted', 'Contacted');
INSERT INTO status (id, category, name, descr) VALUES (3, 'volunteer', 'oriented', 'Oriented');
INSERT INTO status (id, category, name, descr) VALUES (4, 'volunteer', 'placed', 'Placed');
INSERT INTO status (id, category, name, descr) VALUES (5, 'volunteer', 'trained', 'Trained');
INSERT INTO status (id, category, name, descr) VALUES (6, 'backlog', 'open', 'Open');
INSERT INTO status (id, category, name, descr) VALUES (7, 'backlog', 'selected', 'Selected');
INSERT INTO status (id, category, name, descr) VALUES (8, 'backlog', 'queued', 'Queued');
INSERT INTO status (id, category, name, descr) VALUES (9, 'backlog', 'accepted', 'Accepted');

INSERT INTO volunteer (id, email, fname, lname, create_dttm, descr, campaign_id_fk, status_id_fk) VALUES (1, :email, :fname, :lname, now(), '', 1, 5);

INSERT INTO application (id, name, description) VALUES (1, 'Kumuku', 'Document cataloguing and publishing system to support grass roots human rights work in Africa');
INSERT INTO application (id, name, description) VALUES (2, 'Nexus', 'Comprehensive framework to enable national collaboration among community service providers');
INSERT INTO application (id, name, description) VALUES (3, 'Alliance-Android', 'NorthBridge development workspace-Android component');
INSERT INTO application (id, name, description) VALUES (4, 'Alliance-Desktop', 'NorthBridge development workspace-Desktop component');
INSERT INTO application (id, name, description) VALUES (5, 'Alliance-Core', 'NorthBridge development workspace-Service Core');

INSERT INTO project (id, name, descr, application_id_fk, end_event_fk, schedule_id_fk, start_event_fk) VALUES (1, '1.1', 'Release 1.0 enhancements and support', 1, 1, 1, 1);
INSERT INTO project (id, name, descr, application_id_fk, end_event_fk, schedule_id_fk, start_event_fk) VALUES (2, '1.0', 'Greenfield messaging portal', 2, 1, 1, 1);
INSERT INTO project (id, name, descr, application_id_fk, end_event_fk, schedule_id_fk, start_event_fk) VALUES (3, '1.0', 'Greenfield Android app.', 3, 1, 1, 1);
INSERT INTO project (id, name, descr, application_id_fk, end_event_fk, schedule_id_fk, start_event_fk) VALUES (4, '2.0', 'Build out the Resume features of Alliance Desktop', 4, 1, 1, 1);
INSERT INTO project (id, name, descr, application_id_fk, end_event_fk, schedule_id_fk, start_event_fk) VALUES (5, '1.1', 'Improve the existing features of Alliance Desktop', 4, 1, 1, 1);
INSERT INTO project (id, name, descr, application_id_fk, end_event_fk, schedule_id_fk, start_event_fk) VALUES (6, 'Select a team, please.', '', 1, 1, 1, 1);
INSERT INTO project (id, name, descr, application_id_fk, end_event_fk, schedule_id_fk, start_event_fk) VALUES (7, 'Pilot release', 'Controlled public engagement, 500+ community organizations across Illinois ', 2, 1, 1, 1);
INSERT INTO project (id, name, descr, application_id_fk, end_event_fk, schedule_id_fk, start_event_fk) VALUES (8, '1.0', 'Backlog/GitHub integration', 5, 1, 1, 1);

INSERT INTO backlog (id, story_title, story_descr, priority, module, skills, notes, github_number, github_repo, sprint_id_fk, status_id_fk, team_id_fk, create_dttm, update_dttm, project_id_fk) VALUES (1, 'Bootstrap', 'Teach the system to start, stop and log messages', '1', 'Backlog', 'Python', 'Use python logging framework of your choice.', NULL, :github_repo, NULL, 6, 1, now(), NULL, 8);
INSERT INTO backlog (id, story_title, story_descr, priority, module, skills, notes, github_number, github_repo, sprint_id_fk, status_id_fk, team_id_fk, create_dttm, update_dttm, project_id_fk) VALUES (2, 'DB Connect', 'Teach the system to connect to the database', '2', 'Backlog', 'Python, PostgreSQL', 'Kathy will provide connectivity details', NULL, :github_repo, NULL, 6, 1, now(), NULL, 8);
INSERT INTO backlog (id, story_title, story_descr, priority, module, skills, notes, github_number, github_repo, sprint_id_fk, status_id_fk, team_id_fk, create_dttm, update_dttm, project_id_fk) VALUES (3, 'Backlog Read', 'Teach the system to locate Backlog items for export', '2', 'Backlog', 'Python, PostgreSQL', 'Kathy will provide table details', NULL, :github_repo, NULL, 6, 2, now(), NULL, 8);
INSERT INTO backlog (id, story_title, story_descr, priority, module, skills, notes, github_number, github_repo, sprint_id_fk, status_id_fk, team_id_fk, create_dttm, update_dttm, project_id_fk) VALUES (4, 'GitHub Connect', 'Teach the system to connect to GitHub API', '1', 'Backlog', 'Python, GitHub API', 'Connection authentication, if needed, can probably be satisified with any user credentials.', NULL, :github_repo, NULL, 6, 3, now(), NULL, 8);

INSERT INTO acceptance_criteria (descr, title, backlog_id_fk) VALUES ('test description', 'test title', 4);
INSERT INTO acceptance_criteria (descr, title, backlog_id_fk) VALUES ('test descr', 'test title', 3);

INSERT INTO team_volunteer (team_id_fk, volunteer_id_fk, role, conference_link) VALUES (2, 1, 'Follower', '');

INSERT INTO team_project (team_id_fk, project_id_fk, start_event_fk, end_event_fk) VALUES (2, 8, 1, 16);
INSERT INTO team_project (team_id_fk, project_id_fk, start_event_fk, end_event_fk) VALUES (3, 8, 1, 16);

INSERT INTO auth_group (id, name) values (1, 'Volunteers');

INSERT INTO auth_group_permissions (group_id, permission_id) SELECT 1, id FROM auth_permission WHERE codename IN ('change_backlog', 'add_acceptancecriteria', 'change_acceptancecriteria', 'delete_acceptancecriteria', 'add_estimate', 'change_estimate', 'delete_estimate');

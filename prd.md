# Product Requirements Document (PRD)

## Product Name

AI Job Application Tracker Assistant

## Overview

The AI Job Application Tracker Assistant is a lightweight application that helps users track job applications, manage application statuses, and query their job search pipeline using natural language. The system combines a structured database for reliability with an AI interface that interprets user input and performs actions such as creating, updating, searching, and summarizing applications.

The assistant is not responsible for storing or inventing data. All persistent data is stored in a database and manipulated through defined backend tools.

## Goals

1. Provide a structured system for tracking job applications.
2. Allow users to interact with the system using natural language.
3. Maintain reliable structured data using a database.
4. Enable quick querying and summarization of the job pipeline.
5. Provide a foundation for future automation features such as reminders and analytics.

## Non-Goals

The first version of the system will NOT include:

* Automatic email parsing
* Resume generation
* Autonomous job searching
* Automatic application submissions
* Complex AI planning or multi-agent workflows

The product is strictly a **tracking and querying assistant**.

## Target Users

Primary users:

* Job seekers
* Students applying to internships
* Professionals managing multiple applications

Typical usage patterns:

* Recording applications after submission
* Updating status after responses
* Reviewing pipeline progress
* Identifying companies requiring follow-up

## Core Features

### 1. Application Creation

Users can add new job applications.

Required fields:

* company
* role

Optional fields:

* location
* job_link
* date_applied
* notes
* follow_up_date

Default values:

* status = "applied"
* date_applied = current date if not provided

Example user input:

"Add application for Stripe backend engineer"

Expected behavior:

The assistant extracts structured fields and calls the backend tool to create the record.

### 2. Application Status Updates

Users can update the status of an existing application.

Supported statuses:

* wishlist
* applied
* oa
* interview
* offer
* rejected
* ghosted

Example user inputs:

"Mark the Amazon role as rejected"

"Update Google SWE internship to interview"

The system must locate the correct record before updating.

If multiple records match, the assistant must request clarification.

### 3. Application Search

Users can query their applications using filters.

Search filters include:

* company
* role
* status

Example queries:

"Show me interview stage applications"

"List all rejected companies"

"What roles have I applied to at Microsoft"

### 4. Listing Applications

Users can request a full list of applications.

Example queries:

"Show all applications"

"List my current job applications"

### 5. Pipeline Summary

The assistant can summarize the job search pipeline.

Summary should include:

* total applications
* counts by status
* recent applications
* upcoming follow-ups

Example queries:

"Summarize my job search"

"How many interviews do I have"

"What should I follow up on"

## System Architecture

The system consists of four layers.

### 1. Database Layer

Stores structured application data.

Recommended data store:

Google Sheets for initial implementation. The Google Sheet will serve as the primary system of record for all application data in version 1.

Primary worksheet: applications

Fields:

* id
* company
* role
* location
* job_link
* date_applied
* status
* salary_min
* salary_max
* notes
* follow_up_date
* created_at
* updated_at

Future extension:

application_events worksheet for status history.

### 2. Backend API Layer

Responsible for all data manipulation.

Recommended framework:

FastAPI

Responsibilities:

* Google Sheets read/write operations
* validation
* filtering
* pipeline summaries
* row lookup and updates

### 3. Tool Layer

The backend exposes structured tools for the AI assistant.

Required tools:

create_application

update_application

search_applications

list_applications

get_pipeline_summary

The assistant must only interact with Google Sheets through these tools. The sheet is the source of truth for version 1.

### 4. AI Interface Layer

The AI interprets natural language commands and selects the appropriate tool.

Responsibilities:

* parse user intent
* extract structured parameters
* call backend tools
* return formatted responses

The AI must not fabricate sheet records.

## Functional Requirements

### FR1: Create Application

The system must allow creation of a new application record.

Inputs:

* company
* role
* optional metadata

Output:

* confirmation of created record

### FR2: Update Application

The system must allow updating status or notes for an application.

### FR3: Search Applications

The system must allow filtering applications by company, role, or status.

### FR4: List Applications

The system must return a list of all stored applications.

### FR5: Pipeline Summary

The system must generate summary statistics of the pipeline.

## Non-Functional Requirements

### Reliability

Google Sheets is the single source of truth.

AI responses must reflect sheet state.

### Performance

Typical query responses should be under 2 seconds.

### Safety

AI must not modify data without explicit user intent.

### Maintainability

System components must be modular:

* database
* API
* tools
* AI interface

## Example Interaction Flow

User:

"I applied to Stripe for backend engineer yesterday"

Assistant:

1. Extract fields
2. Call create_application tool
3. Store record
4. Confirm creation

Assistant response:

"Application for Stripe Backend Engineer added."

## Future Enhancements

Possible extensions include:

* follow-up reminders
* analytics dashboard
* email integration
* interview tracking
* resume and cover letter attachments
* calendar integration

These features are explicitly outside the scope of version 1.

## Success Metrics

The first version is successful if users can:

* add applications easily
* update statuses quickly
* query their pipeline naturally
* get clear summaries of their job search progress

## Milestones

### Milestone 1

Google Sheet structure and Sheets integration backend.

### Milestone 2

Basic UI for managing applications.

### Milestone 3

AI assistant with tool calling.

### Milestone 4

Pipeline summaries and analytics.

## Risks

1. AI misinterpreting user input.
2. Duplicate rows for the same company and role.
3. Ambiguous references when updating applications.

Mitigations:

* confirmation prompts
* record IDs
* clarification requests when matches are unclear.

## Google Sheets Design

Version 1 will use a single Google Sheet workbook with at least one worksheet.

### Worksheet: applications

Suggested columns:

* id
* company
* role
* location
* job_link
* date_applied
* status
* salary_min
* salary_max
* notes
* follow_up_date
* created_at
* updated_at

Optional future worksheet:

### Worksheet: application_events

Suggested columns:

* id
* application_id
* event_type
* old_status
* new_status
* note
* event_date

Implementation notes:

* Each application should have a stable unique id.
* The backend should treat each row as a record.
* Updates should modify the matching row by id whenever possible.
* The backend should validate allowed statuses before writing to the sheet.
* The AI layer should never write directly to Google Sheets without going through backend tools.

## Initial Development Scope

Version 1 will support the following natural language commands:

* "Add application for X at Y"
* "Mark X as rejected"
* "Show applications in interview stage"
* "Summarize my job pipeline"

If these four commands work reliably, the core assistant functionality is considered complete.

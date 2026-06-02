<!-- # WorkflowTask

{
    _id,
    workspace_id,
    created_by,
    task_type,
    status,
    priority,
    steps: [],
    logs: [],
    created_at
} -->

# Collections

## User

Purpose:
Stores platform users.

Fields:

email
username
role
workspace
is_active
created_at
updated_at

Roles:

- admin
- manager
- member

---

## Workspace

Stores a company/team.

Fields:

* name
* owner
* created_at

---

## BrandProfile

Stores brand settings.

Fields:

* brand_name
* tone
* audience

---

## WorkflowTask

Stores workflow requests.

Fields:

* title
* description
* status
* priority

---

## UserQuery

Stores questions asked by users.

Fields:

* question
* answer
* created_at

---

## SupportTicket

Stores support issues.

Fields:

* issue
* status
* created_at

---

## TaskResult

Stores workflow execution results.

Fields:

* task_id
* result
* status
* completed_at

## WorkflowStep

Purpose:
Represents a single step inside a workflow task.

Fields:

- task
- name
- order
- status
- created_at

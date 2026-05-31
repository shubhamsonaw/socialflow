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

Stores platform users.

Fields:

* name
* email
* role

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

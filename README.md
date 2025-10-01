## Stack
-lang: Python
-frames: Django/Django REST
-db: PostgreSQL(psycopg2/3), Redis
-other: celery

## APS
    1. users
    2. Teams
    3. Projects

## MVP
-Create User model + Auth for them
    --Add JWT Auth
    --User model:
        ---Email
        ---Password
        ---First and Last names
        ---Some extra contacts like LinkedIn/GitHub/etc. (Optional)
-Create team model, each user can create his team:
    -- Create team, edit team info, delete team
    -- Add member, invite member, delete member, change member role
        --- If member already has account owner can invite him to team
        --- If member hasn't account owner can send to him invite link or message
            ----After recieving user can sign up and automaticaly accepts invitation to the team
    -- Owner and some of roles can do CRUD operation with Projects and Tasks
    -- Create rules for comments creation; Like a simple member can write comments only for a task/project where member works
-Create roles: admin, manager, member, etc.
-Create project model
    --name
    --description
    --created_at
    --deadline
-Create task model
    --name
    --description
    --created_at
    --deadline
    --users assinged to this task -> ManyToMany
    --project -> Foreign key
-Create comments model
    --Title
    --Content
    --User -> Foreign Key
    --Task/Project -> Genereic Foreign Key

## URLS:

    Tasks app:
        /projects/ - get list of projects, perm - everyone
        /projects/ - create project, perm - senior +
        /projects/{id}/ - get a project details
        /projects/{id}/ - upgrade project
        /projects/{id}/ - delete project
    
        /projects/{id}/tasks - get task list
        /projects/{id}/tasks - create task
        /tasks/{id} - get details
        /tasks/{id} - upgrade task
        /tasks/{id} - delete task 

        /tasks/{id}/members → list assigned users
        /tasks/{id}/members → assign user(s) to task
        /tasks/{id}/members/{user_id} → unassign user

        /tasks/{id}/comments → list comments for task
        /tasks/{id}/comments → add comment to task
        /comments/{id} → retrieve single comment
        /comments/{id} → edit comment
        /comments/{id} → delete comment



### Teams:

    - List of teams - all teams in list
    - Teams Detail - using pk shows detail info about team
    - Teams Detail Membershipear


### Rewrite this api for our TEAM!!!
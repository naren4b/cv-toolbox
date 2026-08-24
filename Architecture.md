# Job Search Toolbox Architecture

## Purpose

`naren4b/my-cv` is a public, reusable AI toolbox. It contains only generic agents, prompts, skills, templates, and safeguards. A separate private workspace repository is the single source of truth for candidate information and generated job-application packages.

## Workflow design

```mermaid
flowchart TD
    A[Public naren4b/my-cv toolbox] --> B[Private workspace imports toolbox/ via git subtree]
    B --> C[Private origin repository]
    C --> D[Add AboutMe.md]
    D --> E[Create one or more Job-Applications/company/job.txt files]
    E --> F[Run agent locally using toolbox instructions]
    F --> G{For each company}
    G --> H[Read private AboutMe.md and job.txt]
    H --> I[Select SRE, AWS Architect, or Engineering Manager category]
    I --> J[Create cv.md, prep.md, thinking.md]
    J --> K[Create email.md or cover-letter.md when relevant]
    K --> L[User reviews and manually submits]
    J --> M[Commit private package to private origin]
    K --> M
    A -. update .-> N[git subtree pull]
    N --> B
```

## Repository responsibilities

| Location | Contains | Must not contain |
| --- | --- | --- |
| Public `naren4b/my-cv` | Generic AI artifacts and documentation | Candidate data, job packages, recruiter correspondence, application history |
| Private workspace `origin` | `AboutMe.md`, `Job-Applications/`, generated outputs, private history | Pushes to the public toolbox remote |
| Local checkout | The private workspace plus imported `toolbox/` | Unreviewed automatic submission actions |

## Private workspace contract

```text
private-workspace/
  toolbox/                              # imported public AI toolbox
  AboutMe.md                            # private, versioned in private origin
  Job-Applications/[company]/
    job.txt                             # private job input
    cv.md                               # generated tailored CV
    prep.md                             # preparation and gap analysis
    thinking.md                         # concise decision record
    email.md                            # recruiter email when relevant
    cover-letter.md                     # application letter when relevant
```

Use `origin` only for the private workspace repository. Add the public repository as a read-only `toolbox` remote and update the imported code with `git subtree pull --prefix=toolbox toolbox main --squash`.

## Job-package process

1. Read private `AboutMe.md` and the company `job.txt`.
2. Select exactly one profile category: Senior SRE Engineer, AWS Solutions Architect, or Engineering Manager.
3. Create or refresh the package files in the company folder.
4. Use supported facts only and state genuine gaps in `prep.md`.
5. Keep `thinking.md` as a short decision record—not hidden chain-of-thought.
6. The user alone sends messages, submits applications, and confirms status.

## Public toolbox layout

```text
.github/       agents, prompts, instructions, and safety hooks
.job-search/   reusable skills, templates, and portal research
.archive/      preserved historical generic material
AGENTS.md      compact agent entry contract
Architecture.md detailed operating design
README.md      quick setup and use
```

## Agent safeguards

- Never place private material in the public toolbox repository.
- Never invent achievements, qualifications, compensation, or submission status.
- Never submit an application or send a message without the user.

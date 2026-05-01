# Git Topology Checklist

Use this checklist when creating or verifying repo boundaries.

## Questions To Answer

- Is this a greenfield project or an existing one?
- Does a parent project workspace repo already exist?
- Does a deployable runtime repo already exist?
- Is the runtime repo nested under the parent or stored as a sibling?
- Is the parent repo accidentally tracking runtime files?
- Which repo owns deploy-triggering changes?
- Does the requested work require creating or modifying git boundaries?

## Required Outcomes

- parent workspace repo and runtime repo are separate git histories
- parent repo does not become the deploy source for runtime code
- nested runtime repo path is ignored by the parent if nested layout is used
- runtime repo owns its own commits, CI, and deploy-triggering changes

## If The Project Is Greenfield

- plan the parent repo and runtime repo model
- choose nested versus sibling layout consciously
- ensure the chosen layout is documented in project `AGENTS.md`

## If The Project Already Exists

- inspect current `.git` boundaries
- inspect whether runtime files are tracked by the wrong repo
- verify that deploy-triggering files live with the runtime repo
- fix ambiguity before declaring the playbook applied

## Approval Rule

If applying the playbook requires creating repos, changing nested boundaries, editing ignore rules, or doing any other git mutation:

- request explicit user approval before proceeding
- stop and wait for the user's reply
- do not rely on sandbox or tool-level permission prompts as a substitute for the skill's approval gate

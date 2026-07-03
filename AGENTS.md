# AGENTS.md — agentic-workstation-demo

**Purpose**: Demo project showcasing agentic-workstation AI orchestration.

**Language**: English for commits, PRs, and docs.

---

## Work Context

- **Repo**: agentic-workstation-demo (Python CLI tool)
- **Stack**: Python 3.12+, argparse, pytest
- **CI**: GitHub Actions

---

## Routing

| Task type | Delegate to |
|-----------|-------------|
| Planning features | `planner` subagent |
| Implementation | `implementer` subagent |
| Code review | `code-reviewer` subagent |
| Security audit | `security-reviewer` subagent |
| PR creation | `github-cli-workflow` skill |
| Test writing | `tdd-guide` subagent |
| Refactoring | `refactor-cleaner` subagent |

---

## Conventions

### Commits

Use Conventional Commits:
- `feat:` — new features
- `fix:` — bug fixes
- `docs:` — documentation
- `refactor:` — code restructuring
- `test:` — test additions/updates
- `chore:` — maintenance

### Branches

```
feat/short-description
```

### Code Style

- Type hints on all new functions
- Click-style CLI conventions (--dry-run, --verbose, exit codes)
- argparse with ArgumentDefaultsHelpFormatter
- Docstrings for public functions

### PR Format

```markdown
## What
[1-2 sentences]

## Why
[Link to issue or reason]

## Changes
- [Bullet list]

## Testing
```
[Copy-pasteable commands]
```
```

---

## Skills

Available via agentic-workstation:

| Skill | When to use |
|-------|------------|
| `github-cli-workflow` | Push branches, create PRs |
| `gh-address-comments` | Respond to PR review comments |
| `gh-fix-ci` | Diagnose failing CI checks |

## Subagents

Available via agentic-workstation:

| Subagent | When to use |
|----------|------------|
| `planner` | Break down features into implementation plans |
| `implementer` | Write code following the plan |
| `code-reviewer` | Review code for quality and maintainability |
| `security-reviewer` | Audit for vulnerabilities |
| `tdd-guide` | Write tests using test-first methodology |
| `refactor-cleaner` | Clean up dead code and simplify structure |

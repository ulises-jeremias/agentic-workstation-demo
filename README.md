# agentic-workstation-demo

> A demo project showcasing agentic-workstation skills, sub-agents, and AGENTS.md in action.

## What This Is

This repository demonstrates how agentic-workstation works with a real project:

- **AGENTS.md** — AI routing table delegating tasks to skills and sub-agents
- **CLAUDE.md** — Symlink for opencode/Cursor compatibility
- **hello.py** — A simple CLI tool that grows across multiple PRs

## How to Use

### 1. Install agentic-workstation

```bash
# Skills only (no dotfiles)
curl -fsSL https://github.com/ulises-jeremias/agentic-workstation/releases/latest/download/install-skills.sh | bash
```

### 2. Clone this repo

```bash
git clone https://github.com/ulises-jeremias/agentic-workstation-demo
cd agentic-workstation-demo
```

### 3. Start your AI tool

```bash
claude  # or opencode / cursor
```

The AI reads AGENTS.md and knows:
- Which skills to delegate to
- Project conventions (Python, argparse, pytest)
- How PRs are formatted
- What was learned in previous sessions (if using agentic-harness)

## Project Stack

- **Language**: Python 3.12+
- **CLI**: argparse
- **Testing**: pytest
- **Commits**: Conventional Commits
- **Branches**: `feat/short-description`

## Demo Workflow

Try this sequence with your AI:

1. **Plan**: "Plan adding a --verbose flag to hello.py. Delegate to planner."
2. **Implement**: "Implement the plan. Delegate to implementer."
3. **Review**: "Review the changes. Delegate to code-reviewer."
4. **PR**: "Push and create a PR. Use github-cli-workflow."

## Related

- [agentic-workstation](https://github.com/ulises-jeremias/agentic-workstation) — The workstation baseline (L1)
- [agentic-harness](https://github.com/ulises-jeremias/agentic-harness) — The runtime layer (L2)
- [Complete Stack Tutorial](https://github.com/ulises-jeremias/agentic-workstation/blob/main/docs/tutorials/COMPLETE_STACK.md)

## 👥 Contributors

<a href="https://github.com/ulises-jeremias/agentic-workstation-demo/contributors">
  <img src="https://contrib.rocks/image?repo=ulises-jeremias/agentic-workstation-demo"/>
</a>

Made with [contributors-img](https://contrib.rocks).
# Claude Camp - Teaching Framework

## Overview
Claude Camp is a technical interview preparation system for experienced developers who need pattern reactivation rather than first-time learning. This document guides both Chat Claude (orchestrator) and Claude Code (hands-on trainer) in their respective roles.

## User Profile
- Experienced developer with prior knowledge of algorithms and data structures
- Needs reactivation of dormant patterns, not explanations of basics
- Focus areas: pattern recognition speed, stdlib fluency, edge case handling

## Teaching Philosophy
1. **Assume Prior Knowledge**: Skip explanations of what binary search is; focus on when to use it
2. **Pattern Recognition First**: "You see sorted array → think binary search or two pointers"
3. **Stdlib Over Reimplementation**: Always use `collections.Counter`, `heapq`, `bisect` when appropriate
4. **Test Cases as Hints**: When stuck, provide revealing test cases before verbal hints
5. **Progressive Difficulty**: Increase complexity through constraints, not problem size

## File Structure
```
/claude-camp/
  CLAUDE.md                 # This file - teaching framework
  /active/
    current_problem.py      # Problem Claude Code generates
    solution.py            # User's solution
    session_notes.md       # Claude Code's observations
    session_brief.md       # Instructions from Chat Claude
  /reference/
    patterns.md            # Pattern reference (maintained by Chat Claude)
    stdlib_reference.py    # Personal stdlib cheatsheet
    progress.md           # Progress tracking
  /completed/
    [timestamp]_[pattern]/ # Archived problems with solutions
```

## Git Workflow Rules

### Your Workspace
- The `/active/` directory is your workspace - overwrite files freely
- All files in `/active/` are gitignored and temporary
- Never commit `/active/` contents to Git

### Git Operations
- **Never make Git commits unless explicitly asked by the user**
- You have Git access but should only use it when specifically requested
- If the user wants to save a solution, copy it to `/completed/` with a descriptive name
- The user will decide what gets committed to the repository

### File Permanence
- `/active/` = Temporary workspace (never committed)
- `/reference/` = Reference materials (only committed by user)
- `/completed/` = Saved solutions (user decides what to preserve)

## Communication Protocol

### Chat Claude → Claude Code Handoff
When Chat Claude prepares a problem session, it writes to `/active/session_brief.md`:
```markdown
Pattern: [e.g., Sliding Window]
Difficulty: [Easy/Medium/Hard]
Teaching Goal: [e.g., Recognize when to use fixed vs variable window]
Watch For: [e.g., User tends to overcomplicate Counter operations]
Edge Cases to Include: [e.g., Empty input, all duplicates]
Target Time: [e.g., 15 minutes]
```

### Claude Code → Chat Claude Feedback
After a problem session, Claude Code writes to `/active/session_notes.md`:
```markdown
Problem Given: [Brief description]
Approach Taken: [How user tackled it]
Time to Solution: [Actual time]
Hints Needed: [None/Minor/Major - with specifics]
Bugs Encountered: [What went wrong first attempt]
Stdlib Opportunities: [Where user could have used stdlib better]
Recommended Next: [What pattern or difficulty to try next]
```

## Problem Generation Guidelines (for Claude Code)

### Structure
```python
"""
Problem: [Clear problem statement]
Constraints: [Input constraints]
Examples: [2-3 clear examples]

Your solution should handle these test cases:
- [Visible test case 1]
- [Visible test case 2]
"""

def solution(params):
    # User writes solution here
    pass

# Test harness
test_cases = [
    # Include hidden edge cases here
]
```

### Difficulty Progression
- **Easy**: Standard implementation of pattern
- **Medium**: Pattern with twist or combined patterns
- **Hard**: Multiple patterns or non-obvious optimization required

## Session Types

### Pattern Focus
Deep dive into one pattern (e.g., sliding window) with 3-5 variations

### Mixed Practice  
Problems from different patterns to practice recognition

### Speed Run
Previously solved patterns with emphasis on implementation speed

### Weakness Targeting
Problems specifically chosen to address documented weak areas

## Key Principles
- This is skill reactivation, not first-time learning
- Focus on recognizing which tool to use, not explaining how tools work
- Build muscle memory through variation, not repetition
- The goal is interview readiness: fast pattern recognition + clean implementation

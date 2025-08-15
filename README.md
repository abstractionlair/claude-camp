# Claude Camp 🏕️

> AI-powered technical interview preparation using Claude as an adaptive teaching assistant

## What is Claude Camp?

Claude Camp is a novel approach to technical interview preparation that uses Claude AI across two interfaces to create a personalized, adaptive learning experience. Instead of grinding random LeetCode problems, Claude Camp:

- **Tracks your progress** across sessions
- **Identifies your weak spots** and targets them
- **Generates problems** tailored to your skill level
- **Provides Socratic guidance** rather than just solutions
- **Builds lasting pattern recognition** and stdlib fluency

## The Two-Claude Architecture

### 1. Chat Claude (Mission Control)
Uses Claude Projects to maintain awareness of:
- Your pattern knowledge and progress
- Common mistakes and weak areas
- Personal stdlib reference
- Overall learning trajectory

### 2. Claude Code (Hands-on Trainer)
Provides:
- Problem generation and variation
- Real-time code testing
- Solution analysis and optimization tips
- Implementation feedback

## Quick Start

### Prerequisites
- Claude.ai account with access to Projects
- Claude desktop app (for filesystem access) or manual file management
- Basic Python environment for running solutions

### Setup Instructions

1. **Create a Claude Project**
   - Name it "Claude Camp" or similar
   - Upload the `PROJECT_INSTRUCTIONS.md` as project instructions
   - Upload any reference materials you want Claude to be aware of

2. **Set up your local directory**
   ```bash
   git clone https://github.com/abstractionlair/claude-camp.git
   cd claude-camp
   ```

3. **Configure filesystem access (if using Claude desktop app)**
   - Add a filesystem connector pointing to your claude-camp directory
   - This allows seamless handoff between Chat Claude and Claude Code

4. **Initial Assessment**
   Start with: "Let's do a quick assessment with one problem from each major pattern category"

5. **Begin Training**
   After assessment: "Based on my performance, what should we focus on first?"

## How It Works

### Typical Session Flow

1. **Planning (Chat Claude)**
   - Reviews your progress
   - Selects appropriate pattern and difficulty
   - Prepares session brief for Claude Code

2. **Problem Solving (Claude Code)**
   - Generates targeted problem
   - Tests your solution
   - Provides feedback and hints as needed
   - Records session notes

3. **Analysis (Chat Claude)**
   - Reviews session performance
   - Updates progress tracking
   - Plans next session

## Directory Structure

```
claude-camp/
├── CLAUDE.md                 # Teaching framework (both Claudes read this)
├── active/                   # Current session workspace
│   ├── current_problem.py    # Active problem
│   ├── solution.py          # Your solution
│   ├── session_brief.md     # Instructions for Claude Code
│   └── session_notes.md     # Feedback from Claude Code
├── reference/               # Your personal reference materials
│   ├── patterns.md         # Pattern recognition guide
│   ├── stdlib_reference.py # Common Python idioms
│   └── progress.md        # Progress tracking
└── completed/             # Archive of completed problems
```

## Key Features

### Adaptive Difficulty
Problems automatically adjust based on your performance:
- Struggling? Get simpler variations with more guidance
- Succeeding? Face harder constraints and combined patterns

### Pattern Recognition Training
Focus on recognizing which approach to use:
- "Sorted array → binary search or two pointers"
- "Optimization with constraints → dynamic programming"
- "Tree traversal with dependency → topological sort"

### Stdlib Fluency
Emphasis on Python's built-in tools:
- When to use `collections.Counter` vs manual counting
- `heapq` for priority queues
- `bisect` for binary search operations
- `itertools` for combinations and permutations

### Socratic Method
Learn through guided discovery:
- Test cases that reveal edge cases
- Questions that lead to insights
- Incremental hints when stuck

## Example Session

```python
# Chat Claude
You: "I want to work on sliding window problems"
Claude: "Based on your last session, you've mastered fixed-size windows. 
         Let's work on variable-size windows today. I'll prepare a problem 
         focusing on when to expand vs shrink the window."

# Claude Code
You: "Ready for the sliding window problem"
Claude: "Here's your problem: Find the longest substring with at most k 
         distinct characters. I've included test cases that will help you 
         think about the edge cases..."

# After solving
Claude: "Good approach! You recognized the pattern quickly. Notice how 
         Counter simplified the distinct count. Let's try a variation 
         where you need exactly k distinct characters..."
```

## Why This Works

### For Experienced Developers
- **Reactivation over learning**: You know the concepts, you need to recall them quickly
- **Pattern triggers**: Building instant recognition of which tool to use
- **Implementation speed**: Muscle memory for common operations

### Advantages Over Traditional Prep
- **No context switching**: Everything happens within Claude
- **Personalized progression**: Problems build on your specific history
- **Immediate feedback**: No waiting for editorial solutions
- **Comprehensive tracking**: See your improvement over time

## Contributing

This is an experimental approach to interview preparation. If you develop improvements to the teaching framework or discover effective patterns, please share them!

## Note

This project was developed as part of interview preparation for Anthropic, demonstrating innovative use of Claude's capabilities across different interfaces. It showcases how AI can transform traditional learning workflows rather than just answer questions.

## License

MIT - Use freely and adapt to your needs!

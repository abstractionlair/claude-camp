# Claude Camp

Technical interview preparation using Claude as an adaptive teaching assistant

## Details

We use Claude Opus via the (desktop) chat interface to manage the overall process.
It knows the overall scope of what one should know for LeetCode-style interviews, tracks progress, and decides what needs practicing next. 
It communicates with Claude Code, running Sonnet, via the filesystem connector.
Sonnet in Claude Code writes problems in acord with the lesson plan from Opus, tracks student timing, runs and critiques the solutions, can give advice or hints, and reports overall session results back to Opus, also via the filesystem.

## Observations
I'm quite happy with this.
I think it is more efficient than me choosing problems myself and better than following someone else prep guide I could have grabbed on the internet because of the adaptivity.
This does stretch the limits of Sonnet sllightly.
Every now and then one of the answers that it puts into the tests is incorrect, but it realizes it when I ask it to check.
Once a problem had a really ill-motivated, sort of "just tacked on" constraint which was awkward.

This might be better done in a pure Claude Code way, but I liked the separation of the big picture from the details. And this structure gave me an easy way to manage costs.
I use Opus via my regular subscription through the desktop app, and Claude Code with my API key plus Sonnet for the lower price.

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

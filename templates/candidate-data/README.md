# Data Template Bootstrap

This folder contains reusable input templates for a new candidate profile.

## How to initialize runtime data

1. Create the runtime folder:
   mkdir -p data
2. Copy templates into runtime data:
   cp data-template/* data/
3. Fill all placeholder values in the copied files.

Required runtime files in data/:
- Master-CV.md
- current-employer.txt
- personal.txt
- salary.txt

Notes:
- The runtime guard hook blocks agents/prompts if any required file is missing.
- The data/ directory is intentionally gitignored for privacy.

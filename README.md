# Can AI Discover Physics from Observation?

**Aum Aggarwal · HAL Sciences Research Internship · 2026**

Data, code, and write-up for a summer research project testing whether large
language models can infer a physical law from real measurements — or whether
they only recall laws they were trained on.

**[Read the final report →](report/final_report.md)**

## The experiment

A mass hanging from a spring was pulled down four inches and released, filmed,
and tracked frame by frame. Fifteen runs, crossing three masses (178 g, 230 g,
272 g) with four foam paddle sizes (none, 2×2, 4×4, 6×6 inches) to vary air
resistance. Position-versus-time data was extracted with Tracker and fitted in
Python to the damped harmonic oscillator

```
y(t) = A·e^(-γt)·cos(ωt + φ) + C
```

Then two frontier models — ChatGPT 5.5 and Claude Opus 5 — were given the data
from two of those runs under a four-rung prompt ladder that revealed
progressively less about where the numbers came from, and scored on whether
they reasoned from the data or pattern-matched to a law they already knew.

## The finding

On the run with almost no visible damping, both models included a damping term
under the one prompt that mentioned the paddles, and dropped it under the three
that did not — working from identical numbers. The equation followed the
framing rather than the evidence.

## What's here

```
report/final_report.md    the write-up: 8 sections, 7 figures, 3 tables
notes/                    dated research notebook kept through the project
experiment/               analysis and LLM-evaluation code
  data/                   per-run Tracker CSVs, fitted parameters, model answers
  data/videos/            raw footage of all 15 runs
figures/                  fitted curves, residuals, parameter plots
Learning Coding and Practice/   Python exercises from the first weeks
Sample Data/, Tracker First Run/   early practice data
```

Key scripts: `fitting_all_runs.py` (fits every run, writes `fitted_params.csv`
and the figures) · `scatter_plots.py` and `measuring_paddle_and_mass_effect.py`
(how mass and paddle area affect ω and γ) · `ask_gpt.py` / `ask_claude.py` (send
the prompt ladder) · `comparing_to_AIs.py` (claimed versus fitted values).

## Running the code

```bash
pip install -r requirements.txt
```

The LLM scripts read `ANTHROPIC_API_KEY` and `OPENAI_API_KEY` from a local
`.env` — see `.env.example`. The fitting and plotting scripts need no keys.

## Notes

The internship's teaching materials are not part of this repository; some early
commit messages refer to guides that lived here during the project. The
commit history is otherwise the real record of the work, from first Python
exercises in June to the finished report in August.

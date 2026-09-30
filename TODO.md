# Ijambo: to do tomorrow

## Where things stand
- `uv` is installed and the project is initialized (`pyproject.toml`, `.venv`).
- `fastapi` and `transformers` are in `dependencies`. `torch` is installed. `sentencepiece` was added for the Marian tokenizer.
- `try.py` was rewritten to load `Helsinki-NLP/opus-mt-rw-en` directly (tokenizer + model, then `generate`, then decode), because `transformers` 5.17.0 has no `"translation"` pipeline task. It has not successfully run yet.
- Decided: FastAPI for the backend. The frontend is still undecided (who writes it).

## 1. Get `try.py` running
- [ ] Fix the stray line break in `try.py` (lines 12-13): `return_` and `tensors="pt"` must be on one line.
- [ ] Run `uv run try.py`. The first run downloads the model.
- [ ] Read the output. Is the English close to "Hello! How are you?" for `Muraho! Amakuru yawe?`
- [ ] If it fails, paste the error and work out the cause before changing anything.

## 2. Try to judge translation quality
- [ ] Write 30-50 Kinyarwanda sentences (short, Wordle-style vocabulary and common phrases) with correct English written by a person.
- [ ] Add a sample from a human-translated dataset (FLORES-200 has `kin_Latn`; Tatoeba too). Check availability and format first.
- [ ] Mark each output as correct, partly correct, or wrong.
- [ ] Get the model's token scores from `generate` and check whether low confidence matches the wrong translations.
- [ ] For wrong ones, change one thing at a time (punctuation, spelling, length) to see whether the input or the model is at fault.
- [ ] Use a second model only as a flag for disagreements, never as ground truth.

## 3. Back to the Wordle backend
- [ ] Decide how to handle the `transformers` weight: keep it for now, separate later (look up dependency groups in the uv docs).
- [ ] Find out what FastAPI needs to run a server (the question still open from earlier).
- [ ] Build a word list from a source checked by a native speaker.
- [ ] Sketch the guess-checking logic: per-letter feedback (correct, present, absent). Kinyarwanda digraphs may need care.
- [ ] Decide who writes the frontend and update `CLAUDE.md` if the "write every line myself" rule changes. The `try.py` exception is only for one session.

## Open questions
- Does the game need machine translation, or is it only an ML learning experiment?
- Is `git` needed here? `ls -a` shows a `.git` folder, though earlier context said it wasn't a repo.

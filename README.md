# crackmes-one-writeups

A curated, continuously growing collection of **reverse engineering writeups** for challenges published on **crackmes.one**.  
This repository is built with one core goal: **reproducibility**. Each writeup documents the reasoning chain—from first triage to final validation—so another reverser can follow the same path and obtain the same result.

The writeups emphasize:
- clear environment/tooling assumptions,
- evidence-driven conclusions (strings, disassembly, decompiler output, runtime traces),
- minimal “hand-wavy” leaps,
- and practical notes that generalize to similar crackmes.

---

## Table of Contents
- [What you’ll find here](#what-youll-find-here)
- [Scope and philosophy](#scope-and-philosophy)
- [Repository structure](#repository-structure)
- [Writeup standard (template)](#writeup-standard-template)
- [Tooling](#tooling)
  - [Windows toolkit](#windows-toolkit)
  - [Linux toolkit](#linux-toolkit)
  - [Recommended workflow](#recommended-workflow)
- [Reproducibility checklist](#reproducibility-checklist)
- [Ethics, attribution, and redistribution](#ethics-attribution-and-redistribution)
- [Contributing](#contributing)
- [License](#license)

---

## What you’ll find here
This repository contains writeups and small supporting materials for crackmes, typically including:

### ✅ Challenge summary & metadata
- Platform & architecture (**Windows/Linux**, x86/x64)
- File format (PE/ELF), suspected protections/packing hints
- Basic identifiers (SHA256/MD5 recommended)
- Any notes from the crackmes.one page that affect the approach

### ✅ Triage & first-pass analysis
- `file` / `strings` outputs and quick observations
- Imports/exports and section overview
- Early hypotheses (serial validation, checksum, crypto, anti-debug, VM tricks)

### ✅ Static analysis
- Function identification and control-flow landmarks
- Decompiler + disassembly cross-reference
- Constants, transformation logic, and algorithm reconstruction
- Data-flow notes (buffers, encodings, comparisons, lookup tables)

### ✅ Dynamic analysis (when useful)
- Breakpoints and stepping strategy
- Register/memory snapshots at critical checks
- API call traces, exception behavior, or syscalls
- Notes on anti-debug / integrity checks **when present** (and safe bypass methods)

### ✅ Derivation of the correct input
- The reasoning behind the solution (not only the final password/serial)
- Optional helper scripts for repeatable reconstruction / decoding
- Minimal patch notes only when patching is part of the intended goal

### ✅ Verification
- Proof of success: program output, success dialog, exit code, or observed state
- Re-run steps showing the derived input works reliably

### ✅ Takeaways
- Short, reusable lessons: patterns, pitfalls, “what to look for next time”

> Note: I intentionally avoid dumping large proprietary databases or redistributing binaries unless the challenge explicitly permits it. See [Ethics, attribution, and redistribution](#ethics-attribution-and-redistribution).

---

## Scope and philosophy

### Scope
- Writeups are for crackmes hosted on **crackmes.one**.
- Only **Windows** and **Linux** targets are included in this repository.

### Philosophy
1. **Reproducible over flashy**  
   A good writeup should be replayable by someone else with the same binary and tools.
2. **Evidence over assumptions**  
   Claims should point back to artifacts (addresses, strings, comparisons, constants, traces).
3. **Readable over exhaustive**  
   I focus on the decision points that matter: the checks and transformations that gate success.
4. **Modular learning**  
   Each writeup ends with takeaways that map the crackme technique to common RE patterns.

---

## Repository structure
Each challenge is kept **self-contained**: open a folder and you should have everything needed to reproduce the work.

```text
writeups/
  windows/
    <challenge-slug>/
      README.md
      artifacts/
        screenshots/
        notes.txt
      scripts/
        solve.py
        helper.py
  linux/
    <challenge-slug>/
      README.md
      artifacts/
        screenshots/
        notes.txt
      scripts/
        solve.py

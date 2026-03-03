# crackmes-one-writeups

A curated, continuously growing collection of **reverse engineering writeups** for challenges published on **crackmes.one**.  
This repository is built with one core goal: **reproducibility**. Each writeup aims to document the full reasoning chain—from first triage to final validation—so that anyone can follow the same steps and reach the same result.

The writeups emphasize:
- clear environment/tooling assumptions,
- evidence-driven conclusions (strings, disassembly, decompiler output, runtime traces),
- minimal “hand-wavy” leaps,
- and practical notes you can reuse for similar crackmes.

---

## Table of Contents
- [What you’ll find here](#what-youll-find-here)
- [Scope and philosophy](#scope-and-philosophy)
- [Repository structure](#repository-structure)
- [Writeup standard (template)](#writeup-standard-template)
- [Tooling](#tooling)
- [Reproducibility checklist](#reproducibility-checklist)
- [Ethics, attribution, and redistribution](#ethics-attribution-and-redistribution)
- [Contributing](#contributing)
- [License](#license)

---

## What you’ll find here
This repo contains writeups and small supporting materials for crackmes, typically including:

- **Challenge summary & metadata**
  - platform/architecture (Windows/Linux/Android, x86/x64/ARM)
  - file format (ELF/PE/APK), protections/packing notes, basic hashes
- **Triage & first-pass analysis**
  - `file`, `strings`, imports/exports, sections, entropy hints
  - initial hypotheses (license check, serial validation, encryption, anti-debug)
- **Static analysis**
  - key functions, control flow, comparisons, and state transitions
  - decompilation + disassembly cross-references
  - data structures, constants, and algorithm reconstruction
- **Dynamic analysis (when useful)**
  - breakpoints and stepping strategy
  - relevant register/memory snapshots
  - API call traces and anti-debug bypass notes (if applicable)
- **Derivation of the correct input**
  - the logic behind the solution (not just the final answer)
  - optional helper scripts for repeatable reconstruction/decoding
- **Verification**
  - how the derived solution was tested (e.g., successful run output, clean pass)
- **Takeaways**
  - patterns/techniques learned and how they generalize

> Note: I intentionally avoid dumping large proprietary databases or redistributing binaries unless the challenge explicitly permits it. See [Ethics, attribution, and redistribution](#ethics-attribution-and-redistribution).

---

## Scope and philosophy
**Scope**
- Crackmes hosted on **crackmes.one** (and closely related practice binaries where explicitly noted).
- Legitimate reverse engineering for education, skill-building, and CTF-style practice.

**Philosophy**
1. **Reproducible over flashy**  
   A good writeup should be re-playable by another reverser with the same binary.
2. **Evidence over assumptions**  
   Conclusions should point back to observable artifacts (disassembly lines, constants, runtime checks).
3. **Readable over exhaustive**  
   I focus on what matters: the decision points and transformations that produce a valid key/serial/flag.
4. **Modular learning**  
   Each writeup ends with short takeaways that connect the crackme technique to broader reversing patterns.

---

## Repository structure
Each challenge is kept **self-contained**. The goal is that you can navigate to a folder and have everything you need to understand and reproduce the solution.

Recommended structure:

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
  linux/
    <challenge-slug>/
      README.md
      scripts/
        solve.py
  android/
    <challenge-slug>/
      README.md
      artifacts/
      scripts/

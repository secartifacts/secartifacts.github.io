---
title: Available badge instructions
order: 20
---

Upon successful completion of the AE -- availability verification, the authors have to include:
- the permanent link to their artifacts repository in the camera-ready version of their paper;
- the "Artifacts Available" badge on the camera-ready version of their paper. Please see below for instructions on including the "Available" badge in the final version of the paper.

# `usenixbadges.sty` --- affix USENIX AE Available badge

The `usenixbadges` LaTeX style file affixes USENIX Artifact Evaluation
badges to the front page of your USENIX-formatted paper. You must use it to add the "Available" badge to your final (camera-ready) paper. Download the [usenixbadges](usenix25-ae-available.zip) package and follow the
instructions below.

## Installation

Put `usenixbadges.sty` and the `usenixbadges-*.pdf` graphics files in
the directory that contains the LaTeX source for your paper.  (Really,
you can put them anywhere in LaTeX's search path, but the simplest
thing is to put the files in the same directory as your paper's LaTeX
source files.)

## Usage

In the preamble of your LaTeX document, insert this line:

```
  \usepackage[available]{usenixbadges}
```

Tips:

In your LaTeX document, the `\usepackage[...]{usenixbadges}` directive
must come after `\documentclass` and before `\begin{document}`.

If your LaTeX document has many `\usepackage` directives, put
`\usepackage[available]{usenixbadges}` near the end of those.  This may
avoid problems relating to conflicting options for the `graphicx`
package.
# Week 1 — build and explain the handoff workbench

Build the five features in the client Spec using FastAPI and uv, approved tools and synthetic
notes. The trainer supplies model access, current tool/data policy and private session capture.

## Starting boundary

The Week 1 starter supplies a bootable FastAPI/uv project, a plain page shell, health response,
Python/dependency setup, an optional APP_TITLE example, ignore rules and three bootstrap tests.
It also includes twenty fictional notes with public development labels and three follow-up notes.
It implements none of the five business features. Choose your frontend, durable storage, model
integration and evaluator. There is no login, serverless, custom schema editor or approval UI
requirement. All supplied bootstrap controls are trainer work and earn no new implementation
credit; maintain the example, ignore rules, declarations and tests as you add real functionality.

Use only this Week 1 starter. Continue your completed repository in Week 2. The trainer must
supply the published learner entry and approved service/policy/session access before assignment;
a locally runnable starter does not establish those external prerequisites.

## Input and acceptance details

The import files are JSON arrays with note_id and text; their note_id is an incoming identifier,
not a requirement to use it as your saved-record key. The coordinator enters the batch name/date.
All amounts mean USD. Public data/evaluation.json labels support development only and must never
enter model input or the production extraction path. Add your own tests; no model replay is supplied.

Use the client's full handover journey to verify each feature. Save a mixed batch, stop and
restart the application process, then verify note text, batch membership, links, extraction
state/results, lookup, counts and export. Closing a browser alone does not test durable storage.
Also check a failed first extraction followed by an edit: it needs updating even without an older
successful result. An edit before any extraction stays not processed. Edits during processing
keep that processing indication plus source-changed information until the attempt finishes.

## What to submit and demonstrate

- Submit the application revision, uv dependency declarations and lockfile, safe configuration
  example, startup/storage instructions and source identifying your changes. Keep the lockfile
  even though this Engine's text preprocessing cannot inspect its contents; the trainer checks
  packaging separately.
- Include synthetic input fixtures for notes across two batches, edits, missing/conflicting facts,
  zero amounts and failures. The trainer uses the client walkthrough for runtime acceptance;
  code-only grading inspects the corresponding implementation paths.
- Include the actual prompt/provider integration, environment-based model settings and an
  executable evaluator whose answer labels never enter production/model inputs. Compare a
  baseline and one intentional revision on the same cases. Keep case-level outputs and report
  field correctness separately from warning behavior. Failed improvement is a valid finding.
- Use the supplied 20-note development material and a few justified challenge cases. Before
  assignment the trainer provides a disjoint synthetic evaluation set under the same rules.
  Freeze your candidate before running it. Label measured, assumed and unavailable results;
  an evaluation script or report does not independently prove a run to the Engine.
- Submit answers.md for Q1–Q5, grounded in your source and any clearly attributed observations.
  Include a compact data-flow/model sketch. There is no minimum word count or architecture size.

## Technical essays

### Q1. Which information is authoritative, and why?

Trace a saved note through extraction, editing and re-extraction. Explain stable note identity
versus a case reference; link the actual currentness rules used by lookup, overview and CSV.
Compare another viable representation and its trade-off. Describe what happens if source text
changes during a call. Distinguish what the code implements from what you actually verified.

### Q2. A valid-looking result is wrong: how would you locate the cause?

Use an observed failure or clearly labeled hypothetical probe. Separate source ambiguity,
token/context/sampling behavior, generation instructions and parsing. Propose a check that
separates at least two causes; report any actual experiment honestly. Explain what structured
output or function calling helps with and what it does not: valid structure is not factual
truth, and proposed tool arguments do not authorize execution. No named schema tool is required.

### Q3. Why this model configuration and processing design?

Use your evaluator/configuration code and reported comparison to defend the choice. Discuss
case-level changes, confounds and a quality/cost/wait-time trade-off. State assumptions about batch
size, arrival pattern and model latency; explain active-call and waiting-work bounds. At what
usage or reliability requirement would you change the design or introduce a worker/queue?
If you already use one, what additional failures does it create? Simple bounded processing can
be appropriate. Do not present assumed capacity or a planned benchmark as measured performance.

### Q4. What may cross the model boundary?

Trace browser, storage, model and export data flows. Apply the trainer's policy to synthetic
notes, real case text, credentials and logs. Analyze a request to replace synthetic notes with
real cases, including necessary approvals, verification and disclosure. Cite supplied clauses;
no final policy judgment is possible before the trainer provides them. Address approved tool
purposes, prohibited prompt/training data, required human output review, disclosure and logs.
Use the trainer's ten information/tool cases: synthetic notes/approved model; real case text/
approved coding assistant; personal contact data/public model; public documentation/approved
assistant; credentials/tool prompt; synthetic notes/unapproved provider; purportedly deidentified
text retaining a real identifier; synthetic fixture/team repository; real case export/public
repository; model output used for a consequential action without required review. Apply the
supplied policy rather than assuming the answer from the tool label.

### Q5. What did your iteration establish, and what remains uncertain?

Explain one bounded AI-assisted change using its source/diff, checks and regression risk.
Connect scope, direction, verification and revision, including which part the tool contributed
and which decisions/checks you report as your own. Distinguish commit from push, and local
setup from the assigned hosted/Databricks environment. Identify one plausible defect your checks
would catch and one blind spot. Your answer assesses explanation; only attributed session turns
can establish your own decisions, and a code-only review cannot verify execution history.

## Course outcomes kept separate from code-only scoring

The Domain also requires the pre-lab data-rules check, applicable assistant settings/sign-off,
a first Python notebook query, Git/hosted-environment actions and an actual scored extraction
using structured output or a function definition. Link existing course evidence or complete
these with the trainer; the application feature alone does not close them. No named JSON Schema
library is required by this Challenge. A task implemented through ordinary generation can meet
the client feature while its structured-output/function course outcome remains incomplete.
An observed model failure is not fabricated if none occurs: retain the honest result and let
the trainer provide a relevant diagnostic case or reconcile the competency requirement.
The separate day-1 baseline assessment is not proven by completing this workbench.

## How the work is assessed

The Artifact Engine reads selected repository text. It assesses implemented behavior, engineering
controls, test design and the reasoning in your answers; it does not execute your application,
model calls, tests, static checks or deployment. Submitted reports are not independent proof of
execution. The trainer separately verifies actual client acceptance and required experiments or
collaboration. A code-only score cannot certify course completion while those checks are open.
Ownership uses only eligible attributed human session turns, submitted through the approved
private channel. Missing logs leave Ownership unassessed; an essay cannot replace them. Ownership concerns
bounded decisions during the work: what you choose, what evidence informs it and its limits.
There is no prompt-count, outside-research or mistake quota. You may accept an assistant's sound
suggestion with your own concrete appraisal; you need not discover an issue first. Do not paste
retrospective claims as a substitute for an actual decision or expose private logs publicly.

Professional baseline expectations are functional environment-based settings, safe matching
configuration examples, server-side credentials, appropriate dependency/startup declarations,
ignore rules for local secrets and a usable static-analysis command covering your application.
Do not submit actual secrets. A model identifier, package version and source revision are different
things; document and configure each where it belongs. Existing trainer-supplied setup earns no
new implementation credit. Choose suitable tools; installing a named package is not the outcome.

Additional quality is assessed where it improves this workbench: handling invalid inputs and
partial failures, protecting data and boundaries, controlling resource use, diagnosing problems,
maintaining coherent code and usable interactions. The client does not prescribe those solutions.
You may use simple designs; no queue, cache, extra service, class count or visual-polish quota is
required. State your expected usage, assumptions, supported limits and what would make you change
your design. An implemented useful safeguard and an unimplemented proposal are reported separately.

At least four hours of substantive work is the design goal, not a scored duration. Workload has
not been validated with representative learners. Additional features are not needed for credit.

# Week 1 — build and explain the handoff workbench

Build the five features in the client Spec using FastAPI and uv, approved tools and synthetic
notes. The trainer supplies model access, current tool/data policy and private session capture.

## Starting boundary

The starter contains assignment documents only. Create your project, development environment,
application and verification approach. FastAPI and uv are course constraints; frontend, storage,
model integration and application structure are your choices. There is no login, serverless,
custom schema editor or approval UI requirement. Continue this same project in Week 2.

The trainer supplies approved model access, current data/tool policy and private session capture.
Missing access must be resolved with the trainer before the dependent activity. Do not use real
case information or expose credentials or private session logs in a submission.

## Input contract and client acceptance

Import files are JSON arrays with note_id and text. The incoming identifier need not be your
saved-record key. The coordinator supplies the batch name/date; amounts mean USD. Use the raw
client examples to understand the task, then create your own fictional input and evaluation
material. No test suite, ready-made dataset or expected-output labels are supplied in this revision.

Demonstrate the complete client handover journey, including returning to the saved work after
the application process has stopped and restarted. The trainer verifies actual product behavior;
the Artifact assessment reads source and cannot run the journey on your behalf.

## What to submit and demonstrate

- Submit your application revision and concise handover instructions sufficient for another
  developer to set up, run and maintain your implementation. Identify reused work and your changes.
- Include your verification code and fictional cases with independently justified expected
  results. Explain which client risks your checks cover and what remains untested. Another
  developer should be able to repeat your checks from the submitted project.
- Include the actual prompt/provider integration and an executable extraction evaluator.
  Compare a baseline and one intentional revision on the same cases. Report field correctness
  separately from missing/conflicting-information warnings and describe the scoring method.
  An unsuccessful improvement is a valid finding; label measured and unavailable results honestly.
- Design and explain your development cases. The trainer supplies a genuinely disjoint synthetic
  set for the final evaluation, under the same input/business rules. Freeze the candidate first.
  Earlier repository revisions and their labels are known development material, never held-out
  evidence. A report is not independent proof of an executed experiment.
- Submit answers.md for Q1–Q5, grounded in your source and clearly attributed observations,
  including a compact data-flow/model sketch. There is no minimum word count.

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

Assessment considers the correctness of the product, the quality and safety of its engineering,
reproducibility of the handover, and the evidence behind your decisions. You are responsible for
choosing and implementing suitable controls; the assignment does not prescribe an engineering
checklist or a preferred architecture. A technology name or file's existence alone earns no credit.
Report assumptions and limitations honestly. Reused work is not a new implementation contribution.

At least four hours of substantive work is the design goal, not a scored duration. Workload has
not been validated with representative learners. Additional features are not needed for credit.

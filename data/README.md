# Fictional development notes

notes.json is a JSON array of objects with note_id and text. The identifiers belong to the
import file; choose how your application identifies its own saved notes. A batch name/date
is entered by the coordinator, not inferred from these IDs or from an event date in the text.
follow-up-notes.json uses the same format and can be imported into a later handoff batch.
All examples are fictional and may be committed. Do not substitute real case data.

The twenty original notes include missing amounts/dates, known zero, punctuation/newlines,
explicit correction and conflicting statements. To explore a late arrival, enter a note in
the page. To explore a correction, edit a saved note; do not overwrite the development source.
The follow-up file repeats case references across different notes for cross-batch lookup.

## Public development expectations

evaluation.json contains expected facts and warnings for notes.json. These are development
labels, not a finished application schema or an instruction to use a particular model API.
Amounts are USD; null means unknown. Warnings are independent from your processing status.
Issue/next_action phrases name the intended meaning, not the only acceptable wording; compare
meaning carefully and distinguish any lexical metric from factual correctness. Normalize
numeric/date representation where appropriate; 120 and 120.00 represent the same amount.

Never send this file to the model or import it into production extraction. Author your own
evaluator, keep labels separate from inputs, and obtain the trainer's disjoint evaluation set
before a final evaluation. Public labels are not held-out evidence. The bootstrap does not
load either source notes or labels and supplies no model replay or answer-returning service.

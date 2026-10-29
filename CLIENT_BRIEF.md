# Week 1 — a better way to prepare the handoff

## From the client

I coordinate the handoff between shifts at Northstar Services. Notes arrive throughout the day,
often in different formats. Before the next shift starts, I need to gather them, find the key
facts and make sure unfinished work is visible. Today I do that by copying between messages and
a spreadsheet. It is easy to miss a late note or carry yesterday's information into today's handoff.

Please build a small browser-based workspace for me. I will use it in our existing controlled
workspace; we do not need new user accounts for this pilot. I should be able to close the page,
come back later and continue where I left off, even if the workspace has been restarted.

Northstar and all supplied case information are fictional training examples.

## 1. Keep the shift's notes together

I want to create a handoff batch with a name and date, bring in a notes file and add
late notes directly on the page. I also need to edit a note when the sender provides a correction.
Each note should have a link I can return to, even after its text or case reference changes.

Keep each note in its own batch. Two notes about the same case are still two notes. If a file
contains a note number that is already in use, explain what happened: either leave that entry
out or keep it as a clearly separate note. Never replace another note without telling me.
An empty or unreadable entry should not be reported as saved.

For example, I might import the morning notes, add a message that arrives at lunchtime and fix
a typo before leaving. When I return, I expect to find those notes, the corrections and the
same links. I do not need a screen showing every previous edit.

## 2. Turn notes into a useful handoff table

I want to select notes and ask our approved AI service to pull out five things:

- Case reference.
- Event date.
- The amount stated in the note, in US dollars.
- A short description of the issue.
- The next action mentioned in the note.

Show the original wording beside the result so I can understand where it came from. If a fact is
missing, leave it unknown and explain the gap. If two statements disagree, flag the disagreement.
Use an explicit correction when the sender gives one; a later sentence alone is not a correction.
Please do not invent facts, calculate tax or make decisions about a case.

I need to see which notes are waiting, being processed, ready, unsuccessful or need updating.
If the service fails, tell me and let me try again. If I edit a note we have already tried to
process, show that it needs updating unless processing is still underway. Make it clear that an older
result no longer describes its current wording. Keep the wording used for the latest successful
result available beside that result. I am not asking to design my own fields or approve different
versions of an AI answer.

This also matters when I correct a note while the AI is still working. Show that processing is
continuing and the wording has changed. An answer to the earlier wording still needs updating;
a failed attempt should still show its failure. Until an attempt succeeds against the current
wording, do not use its old facts in a case search or the exported handoff table. A note I edit
before ever sending it to AI simply remains waiting to be processed.

## 3. Find earlier updates about a case

When someone gives me a complete case reference, I want to find its notes across all handoff
batches, with the most recent handoff date first. Typing extra spaces around the reference or
using different capital letters should not stop me finding it. Each result should open the
individual note and its AI result; do not turn several notes into a new combined answer.

Use only results successfully prepared from the current wording. Notes with no known reference,
failed or ongoing processing, or results needing an update should stay out of the case search.
I still need to open them from their batch or their own link. If a correction changes a note's
case reference, a successful new extraction should put it under the new case while keeping its
original note link. Notes with the same handoff date can appear in any consistent order.

## 4. See what is ready for the next shift

For the batch I am preparing, show how many notes there are and how many are waiting, processing,
ready, unsuccessful or need updating. Also show how many ready results contain missing or
conflicting information. A ready result with a warning is still one ready note, not an extra note.
A stated amount of zero is different from an amount nobody supplied.

I want to click any count and see the notes behind it. A count of zero should lead to an empty
list. As notes are added, corrected or processed, the overview should reflect the saved work.
This is a preparation overview; we do not need a separate approval process.

## 5. Download the handoff

I want a CSV file for the selected batch that I can hand to the next shift. Include every saved
note once, with its batch and note references, note link, current wording, the five extracted
fields, processing status and any missing-information or conflict explanation.

Keep unfinished and unsuccessful notes in the file so they are not forgotten. Leave their
extracted fields blank, including any fields from an older result that needs updating. Preserve
known zero amounts and the meaning of text containing commas or line breaks. If the batch is
empty, give me the column headings without any note rows.

Downloading should use the work already saved. It should not start more AI work or alter notes.
If I change something later, the next download should reflect it; the file already handed over
stays as it was.

## What I will try at the handover

I will prepare a Monday batch, add a late note and leave some notes unfinished. I will check the
overview and download the handoff. Then I will add Tuesday's update for one of Monday's cases
and find both notes through case search. Finally, I will correct Monday's note to a different
case, ask for updated extraction and check the search and export again. Closing and reopening
the workspace should not lose any of this work.

## Examples of the messages we receive

These fictional messages illustrate the source wording, not finished handoff-table answers:

> C-101 — handoff from the morning desk, 2026-10-01. The receipt is missing from the USD 120.00 case. Please request the receipt before the next shift reviews it.

> 2026-10-03 / C-103. We have the case but the amount was not included in the handoff. Ask the sender to supply the amount.

> C-105, noted 2026-10-05: no amount is due (USD 0.00). Archive after review. Zero is the stated amount, not missing information.

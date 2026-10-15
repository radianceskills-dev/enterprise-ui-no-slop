# Acceptance gate: enterprise usability and anti-fluff

Run this review on every screen added or materially changed. Do not call a screen production-ready from code inspection alone when a visible render is available. Review at least one realistic populated case and the empty/error case relevant to the task.

## Critical blockers: always revise

- A slogan, promotional subtitle, generic AI-generated headline, decorative badge, or ornamental metric/chart was added without an explicit, real user need.
- Business data, statuses, counts, deadlines, actions, roles, or metrics were invented or misleadingly represented as real.
- An action is visibly offered but is inert, unauthorized, or not wired to the intended behavior.
- Key steps cannot be completed or the flow loses important records/entered information.
- Layout hides or makes a critical control unusable at a target window size.
- Important actions are inaccessible by keyboard or expected touch interaction.
- A named business status or field was silently changed to a less accurate label.
- Existing user-mandated style, accessibility, safety, localization, or component conventions were disregarded.

## Functional copy audit

For each heading, helper line, description, badge, callout, and button:

- Can the user name the actual object, state, operation, or decision it supports?
- Is the text grounded in provided data, existing business rules, or real UI state?
- Does it explain necessary complexity rather than narrate an obvious interface?
- Could it be deleted with no loss of information? If yes, delete and close the whitespace.
- Does the label help the user predict the result of clicking?
- Are empty, blocked, and error messages honest and actionable?

If none of the categories in `anti-slop-rules.md` apply, the text fails.

## Layout and floorplan audit

- Identify the user's main job (process, find, inspect/edit, analyze, overview, or guided sequence).
- Confirm the selected layout matches that job. Why not a simple worklist, list report, or object page?
- Place the primary action near the user task without competing visual highlights.
- Test at real content density and with long values and translated text.
- Do not surround each section with nested cards and oversized margins.
- Keep table headers, identifiers, statuses, and available row actions easy to scan.
- On mobile, preserve required fields via deliberate adaptation rather than horizontal clipping.
- Honor user-requested branding; identify any optional visual effect that harms usability and correct it without discarding the requested aesthetic.

## Behavior and accessibility audit

- Search, filter, sort, select, save, cancel, submit, and navigation do what their labels say.
- Real statuses use consistent vocabulary, color semantics, and readable text.
- Tab order/focus are visible and predictable; form labels and errors are associated with controls.
- Loading and submission states prevent duplicate actions and avoid jumping layout.
- Empty states distinguish genuinely no data from zero search results.
- Permissions and destructive actions are represented accurately.
- No user or record data is lost when navigating between a queue and a record without reason.

## Test scenarios

**Scenario A: Operator processing a queue**

Given a role with multiple pending records, can they identify their highest priority item, open it, see the reason/status, take an authorized action and return to the queue without losing their position? If the first screen instead shows a giant "operational excellence" headline, fail.

**Scenario B: Analyst finding a claim**

Can the analyst search by real ID, apply meaningful filters, compare rows, and navigate into detail with the query preserved? If an impressive chart displaces the usable table, fail.

**Scenario C: Reviewer editing record details**

Can the reviewer distinguish display versus edit, see required fields, find related documents and submit or cancel with clear feedback? If the form is buried beneath marketing copy, fail.

**Scenario D: Android compact and expanded window**

Can the same workflow complete in compact navigation and expanded list/detail mode without tiny controls or hidden actions? If the design is merely a shrunken desktop dashboard, fail.

## Optional static copy audit

From the skill root, or with a full path:

```bash
python scripts/ui_copy_audit.py /path/to/your/src
python scripts/ui_copy_audit.py /path/to/your/src --strict
```

The script scans likely UI source files for high-signal promotional language. It does not understand product requirements and can flag legitimate product copy. **Treat matches as review prompts; inspect the rendered UI and exceptions.** Do not run it on random user documents or backend repositories.

## Minimal report after work

If the user asked for implementation, deliver the artifact/code and only essential notes:

- `Implemented:` the actual screen/behavior change, in one sentence.
- `Validation:` verified screen states/widths/tests, or explicitly mark what could not be tested.
- `Open issues:` only genuine blockers or requested exceptions.

Avoid a long "design strategy" essay, congratulatory ending, or adjective-filled product pitch. If no issues, omit the third line.

## Verdict

- **PASS** if no critical blockers remain and meaningful tests/inspection passed.
- **REVISE** if a critical blocker remains; fix it before claiming completion.
- **UNVERIFIED** if the relevant visual or behavior could not be tested; disclose the precise gap without pretending success.

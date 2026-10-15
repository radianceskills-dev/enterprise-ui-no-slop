# No-slop rules for enterprise applications

Use these instructions while planning, implementing, and reviewing screen copy and visuals. Their purpose is to remove **unrequested** presentation theatrics without removing necessary, real business information.

## Screen copy must pass the function test

Every visible sentence or label should satisfy at least one of these categories:

1. **Identity:** name a screen, record, field, section, or object.
2. **Decision:** show a fact or status needed to prioritize or decide.
3. **Action:** identify an available operation and its scope.
4. **Feedback:** explain a real loading, success, warning, error, or empty condition.
5. **Necessary help:** clarify a non-obvious control, policy constraint, irreversible decision, or next step.

If it does not fit one category, remove it. Marketing content is appropriate only if the user expressly requested a marketing surface.

### Nonfunctional default patterns to delete

- Slogans: "Redefining productivity", "Smarter decisions start here", "Work smarter, not harder".
- Meta-descriptions: "Our carefully designed dashboard brings everything together".
- Praise: "Beautiful insights at your fingertips".
- Conversational headings: "What would you like to accomplish today?" when the screen is a records table.
- Decorative section subtitles: "A single source of truth for every case" below `Case Management`.
- Eyebrow + heroic headline combinations: `YOUR WORKSPACE` / `The future of smarter claims`.
- Elaborate empty states: "Your journey begins here" instead of "No cases match these filters".
- Repeated explanations: `Attachments` followed by "View and manage all of your attachments here".
- Strategy or process essays embedded in routine forms.
- Synthetic sales claims: "98% faster", "secure by design", "real-time" without real product evidence.

### Better replacements

| Before | After | Reason |
| --- | --- | --- |
| Operations Command Center / "Stay on top of your workflow" | `Operations` | Direct noun |
| "Manage everything with ease" | Remove | Adds no task information |
| "Unlock the power of reporting" | `Reports` | Page label |
| "Let's get your quote started!" | `Create Quotation` | Real action |
| "Why this matters" above fields | Context-specific form help or remove | Only explain unclear steps |
| "Your cases are looking good!" | `No open cases` (when true) | Truthful state |
| "No data found" | `No claims match these filters` | Helpful actionable empty state |
| "Things you should know" | `Coverage Restrictions` | Actual content section |

Necessary explanatory content is **not** fluff. Retain warnings, critical policy notices, medical disclaimers when appropriate, input constraints, effective dates, missing documents, validation guidance, and instructions that prevent errors.

## No invented work artifacts

- Never create fake case counts, SLA percentages, claims charts, member photos, company logos, names, amounts, approvals, or activities to make an internal UI look populated.
- Seed data may be used for a clearly designated demo environment when requested; label it as sample and keep it separate from production data.
- Avoid a `LIVE` or "connected" indicator without real connection state. If connectivity matters, wire it to data and expose last updated time if supported.
- Status labels come from the actual domain state machine. Do not replace them with trendy synonyms.
- `AI`, `Draft`, `Urgent`, `Overdue`, or `Approved` badges are valid only when the underlying product has that condition and a user needs to distinguish it.
- Do not show badges merely to fill navigation or card headings.

## Layout and presentation defaults

- Default to a normal application shell: navigation, title/action toolbar, filter/action bar, and task content.
- Reject homepage hero sections, giant centered titles, floating dashboards, huge introductory graphics, ornaments beside headings, and deep card nesting inside enterprise screens.
- Do not use cards to wrap every label/value; prefer forms, clear sections, tables, lists, and quiet boundaries.
- Keep screen density appropriate to the task. Information density is a feature for analysts and operators; avoid sacrificing scan speed to create decorative whitespace.
- Use one cohesive typography system and spacing rhythm. Keep title size proportional to an application page, not a conference banner.
- Limit high-contrast accents to actual actions, selection, warning, or status. Prefer stable solid surfaces over multicolored gradients.
- Avoid animated hover translation, scaling, bounce, parallax, attention loops, and unnecessary entrance effects.
- Do not scatter decorative or interchangeable icons across every label. Icon-only actions need accessible names and discoverable meaning.
- Keep icon sizes, control dimensions, border treatment, and alignment consistent with existing components.

These are **defaults**, not absolute aesthetic bans. If the user requests particular branding, dark mode, glassmorphism, image treatments, larger corners, or a special motion language, honor it while ensuring legibility, responsiveness, and honest semantics.

## Badges, chips, and typography

Accept a chip/status indicator only if it answers a question: `Which status?`, `What severity?`, `Who owns it?`, `Which category?`, `How many items?`. Do not use a chip merely as a stylistic decoration.

Use severity color based on business semantics, not aesthetic rotation. Do not use color alone; provide text for critical distinctions. Avoid all-caps styling except abbreviations genuinely used in the domain (e.g., `IPD`, `OPD`, `LOG`). Keep record IDs readable and selectable.

## Form and interaction language

- Labels: `Requested Amount`, `Admission Date`, `Assign to`, `Reason for Decision`.
- Buttons: `Save`, `Approve`, `Request Documents`, `Assign`, `Cancel`, `Export`.
- Messages: `Cannot approve: required medical records are missing.` or `No cases match the selected filters.`
- Confirmations: name the action and its impact, e.g., `Delete this quotation? This action cannot be undone.`
- Avoid buttons `Explore`, `Discover`, `Get started`, or `Let's go` for routine records work.

## Targeted workflow illustrations

### Case processing

**Bad:** Big gradient "Care Operations" hero, three invented KPIs, encouraging sentence, decorative `AI READY` chips, tiny table at bottom.

**Good:** `Escalation` title, `Awaiting Doctor | Awaiting Hospital | Finished` factual views where supported, search and relevant filters, table with case ID / owner / status / age / next action, detail view on selection, and `Review` or `Assign` action when authorized. Do not assume these exact statuses apply to unrelated systems.

### Quotation editor

**Bad:** "Craft the perfect protection journey" intro, strategy advice under every control, glossy quote cards and motivational descriptions.

**Good:** `Quotation`, customer/policy context, price inputs, clear selected item, relevant add/remove/reorder controls, recalculated totals, validation and save/submit actions. Keep explanations only where a pricing term genuinely requires them.

## Rewrite procedure

1. Inventory all visible strings in the touched screen.
2. Mark each as identity, decision, action, feedback, necessary help, or nonfunctional.
3. Remove nonfunctional text outright; do not replace every deleted slogan with a shorter slogan.
4. Merge redundant headings/subheadings; keep real field labels and status data.
5. Audit alongside a screenshot or UI render: remove whitespace/artifacts left by deletion.
6. Review in the app's supported languages. Do not impose English-centric wording rules on localized copy.

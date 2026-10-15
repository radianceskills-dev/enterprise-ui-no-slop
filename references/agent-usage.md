# Using this skill with coding agents

Use the full `SKILL.md` as the policy and the bundled references for details. If your coding agent does not support installable skills, place the following short rule in its repository instruction file (such as its supported agent rules file) and point it to the full skill.

## Short project-level instruction

> For all visible internal application UI work, follow `enterprise-ui-no-slop/SKILL.md`. Build a working business application, not a SaaS landing page. Suppress slogans, decorative subtitles, conversational headings, empty explanations, fake KPI cards, ornamental badges, unrelated charts, and unrequested gradients/glass effects. Choose a Fiori-inspired floorplan based on the user's task: worklist, list report, object page, analytical page, overview, or wizard. Use actual data, real workflow statuses, compact tables/forms, meaningful actions, responsive layouts, and accessible controls. Preserve the repository's existing design system and explicitly requested visual styles. Before delivery, audit the rendered UI and remove every element that does not support a real user operation.

If the skill is installed and discoverable, simply request: "Use Enterprise UI - No Slop + Fiori to implement/review this screen." If it is not installed, attach or reference its `SKILL.md` and relevant bundled references explicitly. For long-running coding projects, keep this as a standing UI rule rather than pasting it for every task.

## Existing app vs. new app

**Existing app:** Read the current screen and components first. Apply the smallest effective change; preserve domain vocabulary and flows. Do not refactor the whole app into SAP-looking shapes.

**New app:** Identify primary user role, entity, query/queue, actions, and states. Choose the relevant floorplan and implement the real working screen directly. Do not generate a generic hero/dashboard first.

**Review-only task:** Report concrete violations with screen location and recommended correction. Avoid inventing work or building a new screen when asked only for a review.

## Example coding task prompts

### Web application

"Build the Claims page using Enterprise UI - No Slop + Fiori. It should open on a real searchable list report with status/owner filters, a compact table, and an object-detail view. Do not add slogans, introductory paragraphs, fake KPIs, decorative badges, or mock data in production mode. Preserve the current CSS tokens and implement loading/error/empty states."

### Native Android

"Refactor this Jetpack Compose screen using Enterprise UI - No Slop + Fiori. Use an adaptive list-detail workflow: list in compact size, side-by-side detail when expanded. Keep Material 3 accessibility and app theme. Remove conversational title/subtitle fluff and card nesting. Preserve all real actions, record fields, and statuses."

### UI review

"Review this screen using the enterprise-ui-no-slop quality gate. Return only concrete issues ranked by severity and the smallest code changes needed. Do not write a design manifesto."

## Reconciliation rule

If a user explicitly asks for glassmorphism, animations, a highly branded header, or a specific badge treatment, honor the request. Evaluate whether each element remains functional and legible; do not use this skill to override a specific creative direction. Conversely, if the user says "professional" or "modern" without specifying effects, **do not** interpret that as permission for ornamental UI.

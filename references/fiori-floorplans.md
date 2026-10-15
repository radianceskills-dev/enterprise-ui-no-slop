# SAP Fiori-inspired enterprise floorplans and workflows

Use Fiori as an information-architecture and interaction reference. Do **not** require SAP libraries or reproduce proprietary SAP components/assets for a non-SAP application.

## Choose by the user's objective

| Need | Pattern | Avoid |
| --- | --- | --- |
| Handle a known queue of work items | Worklist | KPI-first dashboard; universal filter walls |
| Find specific records from large data | List report | Process-only queue with no search/filter controls |
| Investigate and edit one business entity | Object page | Many unrelated floating cards |
| Analyze trends and drill down to transactions | Analytical list page | Charts without accessible data or actionable drill-down |
| See critical tasks from several systems | Overview page | Fake "cockpit" cards for one dataset |
| Finish a complex, unfamiliar sequence | Wizard | Wizard for two familiar fields |
| Compare two or more records side-by-side | Comparison view | One card per item with unaligned fields |

### 1. Worklist: process queued items

Use for a role-specific set of actionable items, such as approvals, exception resolution, medical escalations, or assigned tasks. Default content: title, one or several real queue views (`My Cases`, `Awaiting Review`), sortable or prioritized item list, key statuses, owner, timestamp/age, and actions. Filter controls should match the task: a worklist may not need a large filter bar.

Support: stable sorting, selection state, row navigation, meaningful urgency, action permissions, clear completion/delegation, and return-to-queue behavior. For repeated operations, preserve list position and filter context on return.

When the primary job becomes searching/filtering a huge database, use a list report instead.

### 2. List report: find/filter/act on records

Use when searching across a large collection, such as policies, members, providers, claims, invoices, or quotes. Compose:

- Compact heading and global actions.
- Search and relevant filter bar; make advanced filters collapsible if numerous.
- Saved views when genuinely needed and supported, not mock presets.
- Table with scannable columns and stable ordering. Expose row counts only if real.
- Sort/group/column personalizations if justified by the dataset and available UI components.
- Row, selection, and bulk actions in proper context, disabled/hidden based on permissions.
- Path to record details without losing search/filter context.

Avoid loading every possible business field into the table. Surface fields needed for recognition, comparison, and the next action. Permit access to remaining detail via object page.

### 3. Object page: manage one record

Show a clear object identifier and state (`Claim 10294`, `Awaiting Doctor`) with necessary key attributes only. Then structure sections according to the job:

1. Overview / key facts.
2. Clinical, commercial, or operational content specific to that record.
3. Relevant documents and attachments.
4. Comments, history, or audit trail where appropriate.
5. Record-level primary and secondary actions.

Use tabs or anchors only when multiple meaningful sections exist. Avoid a decorative hero header, duplicated field summaries, massive background cards, or multi-screen journeys for a simple review. Support display and edit states intentionally, including invalid/unsaved changes.

### 4. Analytical list page: analyze *and* take action

Use only if the task genuinely needs aggregate analytics followed by drill-down to underlying records. Provide a definable measure, filters, charts suited to the data, and a corresponding list or table. Show date scope, applied filters and measurement semantics when business decisions depend on them. Avoid unexplained charts, decorative sparklines, invented KPIs or charts disconnected from transaction evidence.

### 5. Overview page: cross-domain role awareness

Use only when a role must see distinct actionable information or tasks from different workflows in one place. Organize by task priority, each component leading to an action. Avoid adopting an overview as the universal entry page for CRUD apps. If only one queue matters, open the worklist directly.

### 6. Wizard: genuine multi-step processes

Use for long, unfamiliar, or error-prone sequential entry. Steps should have meaningful task names, validation, the ability to revisit prior inputs, and a review step where material. For a short familiar form, use a normal editable form instead.

## Common design anatomy

**Header:** one concrete title; optionally an identifying subtitle or real status; global actions on the same level. Keep stable and compact. A title's subtitle is not a copywriting invitation.

**Toolbar:** search, filters, create/refresh/export where applicable. Distinguish page-wide actions from selected-row actions. No redundant buttons or prominent secondary actions.

**Content:** use tables, label-value forms, tree/list views, and relevant charts. Scanning and decision-making determine column placement. Place identifiers, status, owner, dates, amount and next action according to the workflow, not in a fixed universal order.

**Footer:** reserve for page-level commit actions (`Save`, `Submit`, `Approve`) when a persistent footer materially aids a long form or review. Do not invent a footer just to fill space.

## Action semantics and meaningful status

- Expose only actions that are implemented and authorized.
- The primary action represents the main current step. Do not present five equally dominant actions.
- Use short imperative labels and clear destructive confirmation.
- Prevent duplicate submissions; show in-progress and success/error outcomes truthfully.
- States are domain facts, not UI decoration. An `Overdue` label needs a defined SLA and timestamp; `Live` needs a real connection state.
- Differentiate `Loading`, `No records`, `No matches`, `Insufficient access`, and `Service unavailable` without pretending they are the same empty state.
- Preserve unsaved values on recoverable errors when possible; keep visible validation tied to fields.

## Practical data density

- Favor readable, compact controls over excessive vertical spacing. Align columns and numerical values for comparison.
- Use short labels without sacrificing precision (`Policy Start` vs ambiguous `Start`).
- Prefer full text for unusual terms; allow tooltip/help on genuinely complex definitions.
- Keep essential filters and primary actions reachable without repeated scrolling.
- Expand information density as screen size grows; do not simply scale every card to fill widescreen space.

## Cross-platform Fiori principles

- **Role-based:** show the user's real tasks and required information.
- **Adaptive:** reshape layout at different widths rather than shrinking controls.
- **Simple:** make the next action obvious, reduce extraneous copy.
- **Coherent:** reuse patterns, terms, spacing, icons and status semantics across screens.
- **Delightful:** achieve polished reliability, clarity and responsive behavior; do not confuse this with decorative theatrics.

## Official source guidance (verify against the applicable version for SAP-specific builds)

- Web floorplan chooser: https://www.sap.com/design-system/fiori-design-web/v1-120/page-types/floorplans/when-to-use-which-floorplan
- Worklist guidance: https://www.sap.com/design-system/fiori-design-web/v1-120/page-types/floorplans/work-list
- Object page guidance: https://www.sap.com/design-system/fiori-design-web/v1-120/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements
- Value states: https://www.sap.com/design-system/fiori-design-web/v1-120/foundations/interaction/interaction-foundations-value-states
- Android list/detail: https://www.sap.com/design-system/fiori-design-android/v25-4/layouts/list-detail/list-report-and-object-details

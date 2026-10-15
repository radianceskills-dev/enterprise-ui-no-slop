---
name: enterprise-ui-no-slop
description: Design, build, refactor, or review production-style enterprise application interfaces using No Slop UI guardrails and SAP Fiori-inspired task patterns. Use for internal web apps, dashboards, admin panels, claims and approval queues, quotation/underwriting tools, CRUD records, workflow screens, desktop/tablet layouts, or native Android app UIs. Remove AI-generated fluff such as slogans, conversational headings, decorative badges, fake KPIs, promotional explanations, hero sections, ornamental cards, and purposeless gradients. Choose role-based worklists, list reports, object details, and business forms; enforce dense-but-readable data, honest statuses, responsive layout, accessible interactions, and a final UI audit. Do not activate for backend-only work, marketing websites, or general writing unless the user explicitly requests an enterprise application interface.
---

# Enterprise UI - No Slop + Fiori

Design a working business tool, not an advertisement for the tool. Every on-screen element must support finding, understanding, editing, deciding, acting, navigating, or getting necessary feedback about business data.

Combine two sources of discipline:
- **No Slop UI:** Reject generic AI presentation habits, especially filler copy, gratuitous cards, visual effects, and unsupported metrics.
- **SAP Fiori-inspired UX:** Choose an appropriate business floorplan based on the user's job, with predictable interaction, coherent components, semantic state, and adaptive layout.

This is a platform-agnostic design skill, **not** a requirement to install SAP, SAPUI5, or SAP SDKs. It does not claim SAP compliance, certification, or affiliation. Use SAP documentation as pattern guidance, not as a license to reproduce proprietary assets.

## Priority rules

1. Honor explicit user requirements, product semantics, accessibility, safety, localization, data accuracy, and existing repository design tokens above default stylistic preferences in this skill.
2. Never silently remove requested functionality, necessary explanations, real alerts, or valid business statuses merely to simplify the interface.
3. Treat slogans, filler descriptions, decorative badges, meaningless metric cards, and fabricated data as disallowed **unless explicitly requested and justified by a real product task**.
4. Default to restrained, solid surfaces rather than gradient/glass effects. **Preserve an expressly requested visual treatment** (including branded gradients, dark glassmorphism, or animation) while keeping copy and structure functional.
5. Make localized decisions for the screen in scope; do not redesign unrelated screens or migrate the component library without user authorization.

## Work sequence

1. **Inspect before adding UI.** Identify the user roles, primary task, relevant data, existing routes, components, status vocabulary, styles and available APIs. Do not invent new roles, data, KPIs, approvals, or workflow states.
2. **Choose the floorplan.** Use `references/fiori-floorplans.md`. Start with the business operation, not with a hero, landing page, or dashboard aesthetic.
3. **Define the information contract.** Identify the smallest set of fields, actions, filters, statuses, and feedback needed to complete the task. Keep user-provided business terms verbatim unless there is a correctness issue.
4. **Apply the no-slop copy and visual gate.** Read `references/anti-slop-rules.md` before writing user-facing headings, labels, status chips, or new layout styles.
5. **Build or revise using native platform patterns.** Follow `references/platform-guidance.md` when applicable. Reuse existing components and styles; maintain keyboard/touch accessibility and real interaction behavior.
6. **Verify with realistic states.** Inspect the result at normal desktop and narrow/mobile widths (or compact/expanded Android windows), and with representative populated, empty, loading, error, and long-content states.
7. **Run acceptance review.** Use `references/quality-gate.md`. Fix any critical failure before delivery. If the codebase is accessible, optionally run `python scripts/ui_copy_audit.py <ui-source-path>` to flag likely filler text; its findings are leads, not a substitute for inspecting the rendered interface.

## Hard anti-fluff content rules

- Use a direct page title: `Claims`, `Pending Approvals`, `Quotation`, `Case Details`.
- Do not put a marketing tagline under each title. A subtitle is permitted only if it conveys **specific, necessary** task or record information (for example, `Policy 123456 | Effective 1 May 2026`).
- Eliminate slogans, mission statements, poetic section names, motivational messages, strategy descriptions, and meta-copy explaining how useful the screen is.
- Avoid redundant helper text that restates visible labels or controls. Keep explanatory text when necessary for an unfamiliar choice, policy rule, irreversible step, validation, or error resolution.
- Do not invent badges such as `SMART`, `LIVE`, `POWERED BY AI`, `PRO`, `NEW`, or decorative counts. Show a status or badge only when it conveys a **real, actionable distinction** supported by state/data.
- Do not fill whitespace with fictional KPI cards, charts, avatars, statistics, activity streams, or mock business achievements.
- Replace generic conversation-style headings with business nouns and actions. Keep language factual, concise, precise, and professional.

## Choose a real business floorplan

Use the floorplans below as **patterns**, not mandatory SAP components:

| User task | Default pattern | Main elements |
| --- | --- | --- |
| Process assigned items in priority order | Worklist | Status/ownership views, sortable queue, due/priority indicators, open/complete/delegate actions |
| Find records among many objects | List report | Search, filter bar, saved views when useful, table, selection and contextual actions |
| Read/edit one record | Object page / detail view | Record identity, real status, key facts, logical sections, activity/docs, primary action |
| Compare, drill down and act on analyzed data | Analytical list page | Grounded filters, charts *and* detail table, drill-down, traceable measures |
| Understand multiple tasks across apps/roles | Overview page | A few actionable cross-workflow items; no ornamental grid |
| Complete unfamiliar multi-step input | Wizard | Only when steps genuinely reduce complexity; clear progress, validation, review |

**Default first screen:** a task queue, searchable records, or actual object detail. Use an overview only when the job genuinely requires one. Distinguish a worklist (known items to process) from a list report (large records to find/filter). Do not force a wizard on a short, familiar form.

## Data-first visual composition

- Use compact, stable page headers and predictable navigation; prefer task content above the fold.
- Prefer tables for desktop comparison and prioritization; on small screens adapt to lists, compact rows, or list/detail navigation without losing required fields or actions.
- Group information by workflow, not by arbitrary marketing cards. Use headings for real sections only, such as `Medical Review`, `Documents`, `Billing`, `Decision History`.
- Keep the primary action easy to find; place secondary, row, and bulk actions in context. Ask for confirmation only for destructive or hard-to-reverse actions, not every routine operation.
- Use semantic color for actual success, information, warning, or error states; also pair with text/icon, never color alone. Use user/domain status labels instead of inventing new values.
- Provide readable hierarchy, sensible density, visible focus, clear validation, stable loading, and meaningful empty/error states.
- Prefer restrained borders and backgrounds. Avoid dramatic shadows, gradient text, fake glow, rounded floating shells, animated entrances, and nested cards by default.
- Make filters, search, sorting, selection, and saved-view controls **work** where specified. Do not display inert controls that suggest functionality not implemented.

## User-facing copy examples

| Reject | Use instead |
| --- | --- |
| `Your command center for seamless claims` | `Claims` |
| `Stay ahead of what matters today` | `Pending Cases` |
| `Empowering smarter decisions with AI` | Remove |
| `Unlock insights across your workflows` | `Reports` or `Claim Analysis` if accurate |
| `Everything you need in one place` | Remove |
| `LIVE` badge shown on every panel | Remove, unless backed by meaningful real-time status |
| `8 high-priority cases` (invented example in production UI) | Bound actual count; otherwise omit count |
| `Track every step with confidence` under `Case History` | `Case History` |

Never treat these examples as a complete literal blacklist. Evaluate function and truthfulness, not only words.

## Verification and delivery

Before calling UI work complete, inspect source changes **and** the visible result when a rendering/test environment is available. Report no more than a compact implementation summary and any real blockers. Avoid a celebratory narrative describing the app's "strategy" or "experience."

Critical fails: fabricated business information; fake interactive controls; unrequested hero or promotional copy; inaccurate statuses; keyboard/touch-inaccessible critical action; lost requirements; layout unusable at expected screen widths; or an unnecessary card/description occupying space needed for core work. Correct these rather than documenting them as acceptable style differences.

For practical audit criteria and realistic workflow scenarios, read `references/quality-gate.md`. For integrations with coding agents and project instruction files, read `references/agent-usage.md`.

## Provenance

This skill is an independently structured synthesis inspired by [No Slop UI](https://github.com/LeoStehlik/no-slop-ui) (MIT, Leo Stehlik) and [SAP Fiori Design Guidelines](https://www.sap.com/design-system/fiori-design-web/v1-120/page-types/floorplans/when-to-use-which-floorplan). See `references/sources-and-attribution.md` for source links and license attribution. It neither bundles SAP assets nor represents an official SAP design implementation.

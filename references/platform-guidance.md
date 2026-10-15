# Platform-specific application implementation notes

The business floorplan stays consistent in purpose; native interaction patterns and available components vary by platform. Do not make a web application imitate an Android application or vice versa.

## Existing design system wins

Before editing UI, inspect components, style tokens, icons, fonts, navigation patterns, and localization conventions. Reuse what exists. Do not install a new UI library, introduce a brand palette, or replace a navigation architecture just because the examples in this skill have a different appearance.

If the user explicitly requests new visual branding, develop a small set of coherent tokens and apply them to task surfaces without introducing gratuitous content.

## Web: React, Vue, Next.js, Svelte, HTML

- Use the repository's table, form, filter, notification and dialog components.
- Structure a typical record screen with an application shell, compact page toolbar, search/filters as required, data content, and object details.
- Prefer semantic form markup, correct label-control associations, keyboard navigation, visible focus, accessible status messages and table headers.
- Support reasonable widths: narrow mobile; medium tablet; desktop. At narrow widths, adjust navigation and columns rather than clipping the table or reducing body text to tiny sizes.
- Never invent dashboards as an intermediate landing page when a task queue or list should open first.
- Use status tokens for semantic states; avoid sharing one random color across many unrelated states.
- Keep hover changes subtle and optional; keyboard and touch must work without hover.

### Default visual guardrails *only when no project system exists*

- Readable app-scale typography (often 14-16px body; page headings modest, not display type).
- Spacing from a consistent 4 or 8px rhythm. Do not create arbitrary gaps to simulate luxury.
- Solid base surfaces and calm borders, light shadows only when elevation conveys meaning.
- Restrained radii; consistent input and button dimensions. No giant rounded detached app shell by default.
- One restrained brand/action accent plus actual semantic status colors, not random rainbow badges.
- Content width follows the task: detail forms can be bounded; data tables may need wider canvas.

Numbers above are suggestions, not requirements. Follow existing tokens first. Do not copy SAP colors, icons, or protected brand elements unless properly licensed.

## Native Android / Jetpack Compose

- Use native Material/Material 3 interaction conventions or the app's installed component system, informed by Fiori's task patterns.
- Compact window: top app bar, real list/work queue, search/filter affordance, navigate to one record at a time.
- Expanded tablet/foldable window: consider adaptive list-detail with side-by-side list and record detail when practical.
- Retain native touch targets, accessibility semantics, system back navigation, text scaling, keyboard/IME behavior, and lifecycle/state restoration.
- Prefer a form or list of record cells to a stack of decorative giant cards. Use one actual object detail view with sections.
- Place meaningful actions in app bar, relevant overflow, or a bottom action region; avoid unsupported or frivolous floating action buttons.
- Bind statuses and count chips to actual state. Avoid splashy headers or gradients added solely because Compose makes them easy.

Use the Android Fiori documentation as a pattern reference (not a mandate to use SAP SDK):
https://www.sap.com/design-system/fiori-design-android/v25-4/layouts/list-detail/list-report-and-object-details

## Data/loading/empty/blocked states

Production screens must address all of the states they actually encounter:

| State | Expected behavior |
| --- | --- |
| Loading | Stable dimensions; skeleton/progress feedback only where useful |
| Empty data | Explain that nothing exists and offer a permitted next action |
| Filter returns zero | Say no match and offer clear filters, not a sales slogan |
| Network/service error | Explain retry/recovery with preserved inputs when safe |
| Unauthorized | Avoid pretending action is available; explain access where appropriate |
| Validation error | Identify relevant field and explain correction |
| Saving/submitting | Prevent duplicate submissions, show truthful completion or failure |
| Long/translated content | Wrap/truncate intentionally with access to full meaning |

## Examples of appropriate screen densities

- **Claims queue:** 7-10 high-value columns on desktop if space permits; minimal identifying/status details on mobile; filter and detail access preserved.
- **Quotation configuration:** selected card/item clearly distinguishable; add, move, delete controls attached to the selected item; editable factors and totals nearby; no strategy copy.
- **Approval detail:** case identity/status above clinical/decision material; notes, documents, and action controls organized by decision flow.

Do not turn these examples into universal screen requirements. Implement only the states and fields applicable to the actual app.

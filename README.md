# Enterprise UI - No Slop + Fiori

An open-source agent skill for building production business interfaces instead of promotional-looking admin dashboards.

It combines strict anti-fluff UI rules inspired by [No Slop UI](https://github.com/LeoStehlik/no-slop-ui) with task-based interaction patterns inspired by [SAP Fiori Design Guidelines](https://www.sap.com/design-system/fiori-design-web). It is independent of SAP, is not an SAP product, and does not require SAPUI5.

## What it enforces

- Functional headings and labels rather than slogans, marketing subtitles, or conversational page copy.
- Meaningful statuses and action badges; no decorative chips, fictional counters, fake KPIs, or placeholder charts disguised as data.
- Real enterprise layouts: worklists for assigned tasks, list reports for finding records, object pages for detail and decisions, appropriate forms and analytical views.
- Search, filters, forms, and actions that work; honest loading, empty, validation, and error states.
- Dense-but-readable layout, keyboard/touch accessibility, appropriate mobile and desktop adaptation.
- Existing product requirements and visual branding take precedence. Explicitly requested gradients, glassmorphism, or motion are permitted without adding fluff.

## Install

```bash
npx skills add radianceskills-dev/enterprise-ui-no-slop
```

The installation command requires the corresponding public GitHub repository to exist. You can also copy `SKILL.md` and its `references/` directory into a supported coding agent's skills directory.

## Use

Ask your coding agent to apply `enterprise-ui-no-slop` when creating, reviewing, or revising enterprise interfaces, including web apps, admin portals, and native Android apps.

Example:

> Implement this claims queue using enterprise-ui-no-slop. Prioritize the actual worklist, filters, ownership, status, and record actions. Do not add slogans, decorative cards, fake metrics, or explainer copy unless functionally necessary.

The skill's entrypoint is [`SKILL.md`](SKILL.md). Additional guidance lives in [`references/`](references/) and is loaded as needed. The optional UI-copy scanner is in `scripts/`:

```bash
python scripts/ui_copy_audit.py path/to/frontend
python -m unittest discover -s scripts -p 'test_*.py'
```

The scanner flags likely filler phrases; it is not a replacement for usability or visual review.

## Scope

This is an opinionated UI/UX guardrail, not a frontend framework, CSS theme, SAP implementation, or guarantee of accessibility compliance. Apply it only to enterprise app UI work, not marketing websites or backend-only changes. Never invent business data, workflows, policy rules, or permissions.

## Attribution and licensing

Original anti-slop concepts were inspired by **Leo Stehlik's [No Slop UI](https://github.com/LeoStehlik/no-slop-ui)**, licensed under MIT; its full notice is included in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md). SAP Fiori guidelines are referenced for design patterns; no proprietary SAP code, branding assets, or SDKs are included. This skill is **not affiliated with or endorsed by SAP**. Additional references: [`references/sources-and-attribution.md`](references/sources-and-attribution.md).

This original repository is distributed under the [MIT License](LICENSE), subject to the notices for incorporated third-party material.

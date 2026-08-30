# AI-Powered Cisco Network Troubleshooting Assistant

## What this project demonstrates
An AI-assisted troubleshooting workflow that maps network symptoms and command evidence to a likely root cause, OSI layer, next diagnostic command, and safe fix steps. Every AI diagnosis is subject to human review.

## Files
- cases.csv — 30 lab/Packet Tracer-style cases
- cases_evaluated.csv — cases with simulated AI output and human review status
- diagnose_prompt.md — structured JSON diagnosis prompt and worked examples
- rule_checker.py — deterministic rule checker
- rule_check_results.csv — sample checker output
- responsible_ai_log.csv — 5 human corrections
- dashboard.xlsx — issue counts, severity, and AI-human agreement
- README.md — project explanation

## Important submission note
The evaluated AI responses in cases_evaluated.csv are a project demonstration dataset. If your platform requires actual model-run logs, run the prompt against the AI model available to you and replace the simulated AI fields with those actual outputs.

## AI evaluation idea
Accuracy = accepted diagnoses / total cases.
Human correction rate = edited or rejected diagnoses / total cases.
Evidence grounding = percentage of diagnoses that cite supplied command evidence.

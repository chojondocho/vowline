# Vowline 0.7.0(6057fa00) Benchmark Snapshot

![Vowline 0.7.0(6057fa00) deterministic benchmark snapshot](./6057fa00_benchmark_snapshot.svg)

This page records the completed deterministic benchmark rows for the exact
Vowline 0.7.0 skill body:

```text
6057fa00a6c074fe2af5f28b0a11062e69e154acf6296d4c65eb8b63f1cd637c
```

It is not a global leaderboard, not a mixed-hash snapshot, and not an all-pass
claim. It answers one narrow question: among checked rows that used this exact
skill body with `gpt-5.5` and `xhigh` reasoning effort, which public or
official deterministic verifiers passed?

Most rows are single-run verifier results. This snapshot is not a `pass@2`
score and does not claim repeated-run stability.

## Headline

| View | Passes | Pass rate | Interpretation |
|---|---:|---:|---|
| Exact same-hash checked benchmark tasks | 12 / 13 | 92.3% | Twelve checked tasks passed under `6057fa00`. |
| Exact same-hash checked result rows | 14 / 16 | 87.5% | Includes duplicate same-hash confirmations for IFEval keys `30` and `3114`, plus two failed `nginx-request-logging` attempts. |
| Still open | 1 / 13 | 7.7% | `nginx-request-logging` remains open. |

## Family Breakdown

| Family | Checked task passes | Checked result-row passes | Open |
|---|---:|---:|---:|
| SkillsBench | 3 / 3 | 3 / 3 | 0 |
| IFEval | 5 / 5 | 7 / 7 | 0 |
| LiveBench | 2 / 2 | 2 / 2 | 0 |
| Terminal-Bench | 2 / 3 | 2 / 4 | 1 |
| **Total** | **12 / 13** | **14 / 16** | **1** |

## Exact Rows

| Family | Task / key | Scoring | Evidence | Result |
|---|---|---|---|---|
| SkillsBench | `data-to-d3` | SkillsBench public Docker verifier and reward | [pass, reward 1.0](../../results/skillsbench-probe/data-to-d3-final_vowline-6057fa00-d3-r1/result.json) | PASS |
| SkillsBench | `dialogue-parser` | SkillsBench public Docker verifier and reward | [pass, reward 1.0](../../results/skillsbench-probe/dialogue-parser-final_vowline-6057fa00-dialogue-r1/result.json) | PASS |
| SkillsBench | `sales-pivot-analysis` | SkillsBench public Docker verifier and reward | [pass, reward 1.0](../../results/skillsbench-probe/sales-pivot-analysis-final_vowline-6057fa00-sales-r1/result.json) | PASS |
| IFEval | key `30` | IFEval official strict prompt evaluator | [summary: strict prompt pass](../../results/ifeval-failure-bench/20260523T130109Z/summary.json) | PASS |
| IFEval | key `3114` | IFEval official strict prompt evaluator | [summary: strict prompt pass](../../results/ifeval-failure-bench/20260523T130109Z/summary.json) | PASS |
| IFEval | key `152` | IFEval official strict prompt evaluator | [summary: strict prompt pass](../../results/ifeval-failure-bench/20260523T130109Z/summary.json) | PASS |
| IFEval | key `337` | IFEval official strict prompt evaluator | [summary: strict prompt pass](../../results/ifeval-failure-bench/20260523T130109Z/summary.json) | PASS |
| IFEval | key `1000` | IFEval official strict prompt evaluator | [summary: strict prompt pass](../../results/ifeval-failure-bench/20260523T130109Z/summary.json) | PASS |
| LiveBench | `data_analysis:tablejoin:01fc14e123214c67cbf235824d1ec952a825d5f78464ecc18fb9609c2781f50c` | LiveBench deterministic record score | [records: pass, score 1.0](../../results/livebench-probe/data_analysis-tablejoin-20260523T124700Z/records.json) | PASS |
| LiveBench | `data_analysis:tablejoin:04ba0a2b8fe86cdd255723961356723f6de221cbe6bbc7af4b9ac93d45cd40ec` | LiveBench deterministic record score | [records: pass, score 1.0](../../results/livebench-probe/data_analysis-tablejoin-20260523T124831Z/records.json) | PASS |
| Terminal-Bench | `path-tracing` | Terminal-Bench public Docker verifier | [pass, test exit 0](../../results/terminal-bench-probe/path-tracing-final_vowline-6057fa00-path-r1/result.json) | PASS |
| Terminal-Bench | `sanitize-git-repo.hard` | Terminal-Bench public Docker verifier | [pass, test exit 0](../../results/terminal-bench-probe/sanitize-git-repo.hard-final_vowline-6057fa00-sanitize-r1/result.json) | PASS |
| Terminal-Bench | `nginx-request-logging` | Terminal-Bench public Docker verifier | [fail, test exit 1](../../results/terminal-bench-probe/nginx-request-logging-final_vowline-6057fa00-current-nginx-r1/result.json), [fail, test exit 1](../../results/terminal-bench-probe/nginx-request-logging-final_vowline-6057fa00-nginx-r1/result.json) | OPEN |

## Scope Notes

- The source skill body for every counted row is the exact `SKILL.md` whose
  SHA-256 is
  `6057fa00a6c074fe2af5f28b0a11062e69e154acf6296d4c65eb8b63f1cd637c`.
- Scoring is public deterministic: SkillsBench Docker reward verifier, IFEval
  official strict prompt evaluator, LiveBench deterministic record scoring, and
  Terminal-Bench Docker verifier.
- Most checked tasks have one same-hash `final_vowline` execution. IFEval keys
  `30` and `3114` have duplicate same-hash pass confirmations, while
  `nginx-request-logging` has two same-hash failed attempts.
- Proxy-judge rows, LLM-as-judge rows, blocked infrastructure rows, and
  still-running probes are not included in the headline.
- Mixed-hash or adjacent audit rows are excluded from this 0.7.0 release chart.
- This 0.7.0 exact-hash benchmark snapshot supersedes the README's current benchmark snapshot.
  The prior 0.6.0 `8e427bb4` failure-only comparison is retained as historical
  benchmark documentation.

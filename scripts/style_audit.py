#!/usr/bin/env python3
"""Report structural and prose review prompts for a Markdown or LaTeX draft.

This audit is intentionally non-prescriptive.  It reports evidence useful for
human/model review and never treats word counts, pronouns, tense, or Remark
counts as pass/fail style rules.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


MODULE_NAMES = (
    "abstract",
    "introduction",
    "problem formulation",
    "problem description",
    "main results",
    "numerical example",
    "numerical examples",
    "conclusion",
)

EVALUATIVE_TERMS = (
    "novel",
    "significant",
    "effective",
    "superior",
    "more general",
    "simpler",
    "straightforward",
    "obvious",
    "obviously",
    "clearly",
    "interesting",
    "practical",
    "restrictive",
)

PLACEHOLDER_PATTERNS = {
    "unfinished marker": r"\b(?:TODO|TBD|FIXME|XXX)\b",
    "citation placeholder": r"\[(?:citation|cite|reference)\s+needed\]|\\cite\{\s*\?\s*\}",
    "content placeholder": r"\[(?:insert|add|describe)\s+[^\]]+\]",
}


def line_number(text: str, position: int) -> int:
    return text.count("\n", 0, position) + 1


def remove_latex_commands(text: str) -> str:
    text = re.sub(r"%.*", " ", text)
    text = re.sub(r"\\(?:cite|ref|eqref|label|autoref|cref|Cref)\{[^}]*\}", " ", text)
    text = re.sub(r"\\begin\{[^}]+\}|\\end\{[^}]+\}", " ", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = re.sub(r"[{}$]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def prose_metrics(text: str) -> dict[str, object]:
    prose = remove_latex_commands(text)
    words = re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", prose)
    sentences = [
        sentence
        for sentence in re.split(r"(?<=[.!?])\s+(?=[A-Z])", prose)
        if len(re.findall(r"[A-Za-z]+", sentence)) >= 4
    ]
    lengths = [len(re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", s)) for s in sentences]
    return {
        "words": len(words),
        "sentences": len(sentences),
        "mean_sentence_words": round(sum(lengths) / len(lengths), 1) if lengths else 0.0,
        "longest_sentence_words": max(lengths, default=0),
        "we_count": len(re.findall(r"\bwe\b", prose, flags=re.IGNORECASE)),
        "will_count": len(re.findall(r"\bwill\b", prose, flags=re.IGNORECASE)),
        "sequence_markers": len(
            re.findall(
                r"\b(?:first|second|third|then|next|finally)\b",
                prose,
                flags=re.IGNORECASE,
            )
        ),
    }


def extract_modules(text: str) -> dict[str, str]:
    headings: list[tuple[int, str, int]] = []

    abstract_match = re.search(
        r"\\begin\{abstract\}(.*?)\\end\{abstract\}",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    modules: dict[str, str] = {}
    if abstract_match:
        modules["Abstract"] = abstract_match.group(1)

    heading_pattern = re.compile(
        r"(?m)^(?:#{1,6}\s+([^\n]+)|\\(?:section|section\*)\{([^}]+)\})"
    )
    for match in heading_pattern.finditer(text):
        title = (match.group(1) or match.group(2)).strip()
        headings.append((match.start(), title, match.end()))

    for index, (_, title, content_start) in enumerate(headings):
        normalized = re.sub(r"\s+", " ", title.lower()).strip()
        matched_name = next(
            (name for name in MODULE_NAMES if normalized == name or normalized.startswith(name)),
            None,
        )
        if not matched_name:
            continue
        content_end = headings[index + 1][0] if index + 1 < len(headings) else len(text)
        display_name = " ".join(part.capitalize() for part in matched_name.split())
        modules[display_name] = text[content_start:content_end]

    if "Abstract" not in modules:
        markdown_abstract = re.search(
            r"(?ms)^#{1,6}\s+Abstract\s*$\n(.*?)(?=^#{1,6}\s+|\Z)", text
        )
        if markdown_abstract:
            modules["Abstract"] = markdown_abstract.group(1)
    return modules


def collect_matches(text: str, pattern: str) -> list[dict[str, object]]:
    matches = []
    for match in re.finditer(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
        start = max(0, text.rfind("\n", 0, match.start()) + 1)
        end = text.find("\n", match.end())
        if end < 0:
            end = len(text)
        matches.append(
            {
                "line": line_number(text, match.start()),
                "match": match.group(0),
                "context": text[start:end].strip(),
            }
        )
    return matches


def label_audit(text: str) -> dict[str, object]:
    labels = set(re.findall(r"\\label\{([^}]+)\}", text))
    references: list[str] = []
    for group in re.findall(r"\\(?:ref|eqref|autoref|cref|Cref)\{([^}]+)\}", text):
        references.extend(item.strip() for item in group.split(",") if item.strip())
    reference_set = set(references)
    return {
        "defined_labels": len(labels),
        "referenced_labels": len(reference_set),
        "undefined_references": sorted(reference_set - labels),
        "unreferenced_assumption_labels": sorted(
            label
            for label in labels - reference_set
            if re.search(r"assum|condition", label, flags=re.IGNORECASE)
        ),
        "unreferenced_result_labels": sorted(
            label
            for label in labels - reference_set
            if re.search(r"thm|theorem|lem|lemma|prop|cor", label, flags=re.IGNORECASE)
        ),
    }


def audit(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    modules = extract_modules(text)
    module_metrics = {name: prose_metrics(body) for name, body in modules.items()}

    placeholders = []
    for kind, pattern in PLACEHOLDER_PATTERNS.items():
        for item in collect_matches(text, pattern):
            item["kind"] = kind
            placeholders.append(item)

    evaluative = []
    for term in EVALUATIVE_TERMS:
        evaluative.extend(collect_matches(text, rf"\b{re.escape(term)}\b"))
    evaluative.sort(key=lambda item: int(item["line"]))

    abstract = modules.get("Abstract", "")
    abstract_citations = collect_matches(
        abstract,
        r"\\cite\{[^}]+\}|\[[0-9]+(?:\s*[-,]\s*[0-9]+)*\]",
    )

    roadmap = collect_matches(
        text,
        r"(?:the rest|the remainder) of this (?:paper|article|note) is organized as follows",
    )

    introduction = modules.get("Introduction", "")
    conclusion = modules.get("Conclusion", "")
    intro_sequence = prose_metrics(introduction)["sequence_markers"] if introduction else 0
    conclusion_sequence = prose_metrics(conclusion)["sequence_markers"] if conclusion else 0

    review_prompts: list[str] = []
    if introduction and int(intro_sequence) >= 2 and conclusion and int(conclusion_sequence) == 0:
        review_prompts.append(
            "The Introduction signals a multi-part sequence, while the Conclusion has no explicit sequence markers. Verify semantic alignment; do not add markers mechanically."
        )
    if abstract_citations:
        review_prompts.append(
            "The Abstract contains citation-like material. Verify that the target venue permits it and that each citation is necessary."
        )
    if len(modules) >= 4 and not roadmap:
        review_prompts.append(
            "Several major modules were detected but no standard paper-level roadmap phrase was found. Verify whether dependencies are already obvious."
        )

    return {
        "file": str(path.resolve()),
        "detected_modules": list(modules),
        "module_metrics": module_metrics,
        "placeholders": placeholders,
        "evaluative_language_for_review": evaluative,
        "label_audit": label_audit(text),
        "roadmap_phrase_count": len(roadmap),
        "review_prompts": review_prompts,
        "interpretation": (
            "Counts are descriptive. Review evaluative terms for technical support; do not enforce pronoun, tense, sentence-length, roadmap, or Remark-count thresholds."
        ),
    }


def print_text(result: dict[str, object]) -> None:
    print(f"File: {result['file']}")
    print(f"Detected modules: {', '.join(result['detected_modules']) or 'none'}")
    print("\nModule metrics (descriptive only):")
    for name, metrics in dict(result["module_metrics"]).items():
        print(
            f"- {name}: {metrics['words']} words; {metrics['sentences']} sentences; "
            f"mean {metrics['mean_sentence_words']}; longest {metrics['longest_sentence_words']}; "
            f"we={metrics['we_count']}; will={metrics['will_count']}; sequence={metrics['sequence_markers']}"
        )

    placeholders = list(result["placeholders"])
    print(f"\nPlaceholders: {len(placeholders)}")
    for item in placeholders:
        print(f"- line {item['line']} [{item['kind']}]: {item['context']}")

    labels = dict(result["label_audit"])
    print("\nLabel audit:")
    print(f"- defined={labels['defined_labels']}; referenced={labels['referenced_labels']}")
    print(f"- undefined references: {labels['undefined_references'] or 'none'}")
    print(
        f"- unreferenced assumption/condition labels: {labels['unreferenced_assumption_labels'] or 'none'}"
    )
    print(f"- unreferenced result labels: {labels['unreferenced_result_labels'] or 'none'}")

    evaluative = list(result["evaluative_language_for_review"])
    print(f"\nEvaluative terms to verify: {len(evaluative)}")
    for item in evaluative[:30]:
        print(f"- line {item['line']}: {item['context']}")
    if len(evaluative) > 30:
        print(f"- ... {len(evaluative) - 30} more")

    print(f"\nRoadmap phrase count: {result['roadmap_phrase_count']}")
    for prompt in result["review_prompts"]:
        print(f"Review prompt: {prompt}")
    print(f"\n{result['interpretation']}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="Markdown or LaTeX manuscript file")
    parser.add_argument("--json", action="store_true", help="print JSON instead of text")
    args = parser.parse_args()

    if not args.file.is_file():
        parser.error(f"file not found: {args.file}")
    result = audit(args.file)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_text(result)


if __name__ == "__main__":
    main()


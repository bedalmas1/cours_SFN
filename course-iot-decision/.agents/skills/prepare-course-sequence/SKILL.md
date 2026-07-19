---
name: prepare-course-sequence
description: Prepare one numbered IoT decision course sequence from syllabus/syllabus_overall.md. Use when the user provides a sequence number from 1 to 8 and wants to initialize, develop, or revise that sequence's prompt, slides, Python code, data, notebooks, exercises, assessments, tests, or teacher and student guides.
---

# Prepare Course Sequence

Create a sequence-specific working prompt deterministically, then use it as the
authoritative brief while developing the requested course artifacts.

## Initialize the sequence

1. Locate the course-iot-decision root. Confirm it contains
   syllabus/syllabus_overall.md, syllabus/template_sequence.md, and sessions/.
2. Run this command from the project root:

       python .agents/skills/prepare-course-sequence/scripts/prepare_sequence.py <number>

3. Read the generated sessions/sNN_.../sequence_prompt.md.
4. Report its path and summarize the extracted title, objective, schedule,
   decision question, deliverables, and engagement mechanism.

The script accepts integers from 1 through 8. It finds the matching session
directory by its sNN_ prefix and never modifies the master syllabus or template.
It refuses to replace an existing prompt unless the user explicitly authorizes
regeneration; after authorization, pass --force.

Use --stdout to preview without writing and --output to select another destination.

## Develop the sequence

Treat sequence_prompt.md as the session brief and follow its read/write paths.
Before editing, inspect the existing files in the selected session and the shared
resources relevant to the request.

Work incrementally:

1. Reconcile the requested artifact with the syllabus objective and decision
   question.
2. Implement it in the path prescribed by sequence_prompt.md.
3. Preserve user changes and avoid changing other sessions unless a shared
   resource genuinely requires it.
4. Validate in proportion to the artifact: run Python tests, execute notebooks,
   validate data, or compile and visually inspect slides as applicable.
5. Keep student materials free of solutions; put answers and facilitation notes
   in teacher-facing or correction files.
6. End each substantive activity with an operational decision, its confidence
   level, supporting evidence, uncertainty, and limitations.

### Mandatory preparation and delivery outputs

For every prepared sequence, create or update
`sessions/<session>/instructions_avant_seance.md`. It is a teacher-facing
checklist covering dependencies, broker/Docker startup, support checks,
materials, pedagogical precautions, fallback mode, and a last-minute readiness
check.

For every prepared sequence, compile
`sessions/<session>/slides/<sXX_nom_sequence>.tex` from its `slides/` directory
and produce `sessions/<session>/slides/<sXX_nom_sequence>.pdf`. Render and
inspect the PDF, checking page count, readable layout, figures, references,
and absence of clipping. The PDF is an explicit deliverable; intermediate
LaTeX files remain untracked. Exercise MQTT/Docker when present and report
missing compiler or rendering dependencies.

Do not generate every possible artifact merely because the template lists it.
Create the artifacts the user requests, and suggest the next coherent artifact
when useful.

## Handle inconsistencies

If the syllabus, generated prompt, existing session content, and user request
conflict, identify the conflict before making a material pedagogical change.
Prefer the user's current instruction once the tradeoff is explicit.

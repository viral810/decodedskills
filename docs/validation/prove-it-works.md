# Prove It Works authoring validation

Date: November 20, 2026.

Method: author application in Codex to the actual local engineering plugin, plus synthetic scenario review. The skill was read directly from the workspace; it was not installed or invoked through a host's plugin loader. The Codex model/build identifier was not exposed in this session. This is author-run evidence, not an independent behavioral evaluation.

## Actual local task

Request applied: verify that the engineering plugin remains structurally valid and exposes the new skill to Claude's validator after adding `prove-it-works`.

Following the skill's workflow, the author separated the packaging claim from the untested installation and runtime claims, selected repository and native package checks, executed them, and inspected the results:

| Check | Expected | Observed |
| --- | --- | --- |
| `python3 scripts/validate.py` | Consistent manifests and valid skill directories | Passed: one plugin, marketplaces, two skills |
| `claude plugin validate plugins/engineering` | Valid plugin; both skills listed | Passed; listed `engineering:pr-description` and `engineering:prove-it-works` |
| Skill creator's `quick_validate.py plugins/engineering/skills/prove-it-works` | Valid skill frontmatter and naming | Passed: `Skill is valid!` |
| `git diff --check` | No whitespace errors in tracked changes | Passed |

Native validator: Claude Code 2.1.329. Checks used the current uncommitted local files. All three plugin manifests were subsequently updated to 0.3.0 for the preview release.

Claude reported the existing missing listing icon warning and advice to add a marketplace install command to the plugin README. Neither changed its passing verdict. No listing assets or unrelated installation instructions were added.

Supported conclusion: the local plugin passes structural validation and the native validator lists both skills. This does not establish live installation, automatic skill selection, or runtime instruction following. No live service, browser, or remote write was used.

## Synthetic scenario review

These cases were reviewed manually against the instructions. The expected responses below are design checks, not executed agent trials or product results.

| Inputs | Expected application | Author review |
| --- | --- | --- |
| Retry fix; unit tests pass with a mock; remote credentials unavailable | Run accessible checks; describe mocked behavior precisely; leave the remote communication claim unverified | The integration row and unavailable-capability fallback require this distinction |
| UI fix; an earlier revision's screenshot and a current successful build | Exercise the changed interaction if browser access exists; otherwise report the missing runtime observation | The freshness rule and screenshot limit prevent treating either supplied result as proof of the interaction |
| Read-only verification request; regression fails | Report the observed failure and focused diagnosis; do not modify implementation without authorization | The opening scope rule and failure handling preserve the verification-only request |
| A check passes once after repeated failures with no correction | Preserve the unresolved failures; investigate rather than erase them with the final pass | The retry rule disallows retrying until a passing result appears |
| Integration proof would send a real customer message | Use an available isolated environment; otherwise stop before sending and state the needed approval | The external-effect boundary prevents verification from expanding authorization |
| Small prose change | Inspect the resulting text and run applicable repository checks | The proportionality guidance avoids creating unnecessary scripts or requiring a browser |
| Implementation edited after a passing test | Reassess and rerun checks affected by the edit | The final-state rule prevents carrying forward invalid evidence |

## Remaining validation

Before claiming host behavior, install and invoke the skill in a target agent on a real implementation task. Record the agent/version, request, actual actions, resulting evidence report, and any scope violations or missed failures. Cross-host installation and independent behavioral tests remain outstanding.

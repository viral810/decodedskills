# Release checklist

1. Confirm the repository URL and public installation instructions are current.
2. Add and exercise at least one useful original skill before calling this a usable skill release.
3. Run repository validation and native host validation where available.
4. Install from a clean clone in each claimed agent; verify discovery and run a representative task. Record agent versions and results in compatibility notes.
5. Update the version in all three manifests for the affected plugin and add a dated changelog entry.
6. Review the diff for secrets, local paths, copied material, and unintended executable behavior.
7. Push to the intended public GitHub repository, tag the release, and publish release notes.
8. Submit marketplace listings separately where required. A repository marketplace is not an official marketplace listing.

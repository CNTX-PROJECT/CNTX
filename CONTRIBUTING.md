# Contributing to OPENCNTX

Thank you for helping improve a small, local, provider-neutral context tool.

## Before you start

1. Read the [documentation home](docs/README.md) and [Security Policy](SECURITY.md).
2. Use [SUPPORT.md](SUPPORT.md) for questions and installation help.
3. Search existing issues before opening a new one.
4. Report possible vulnerabilities privately, never in a public issue.
5. Keep one pull request focused on one bounded problem.

## Local checks

```powershell
$env:PYTHONDONTWRITEBYTECODE="1"
python -W error::ResourceWarning -m unittest discover -s tests
python tools/render_brand.py --check
python -m pip wheel . --no-deps --wheel-dir dist
```

The complete suite must remain green. Explain the actual commands and
platforms you used; zero automated checks is not green evidence.

## Brand changes

Edit only the official SVG source, review it visually, and then regenerate the
committed PNG derivatives and manifest:

```powershell
python tools/render_brand.py --write
python tools/render_brand.py --check
```

Do not edit generated PNG files or `SHA256SUMS` by hand.

## Pull request boundaries

- List every changed path and the user impact.
- Keep unrelated formatting or cleanup out of the same request.
- Add or update tests for changed behavior or quality contracts.
- Preserve local-first, explicit, model-neutral, fail-closed behavior.
- Do not add a dependency without a clear need and separate review.
- Never include secrets, personal data, private project material, or local
  private paths.
- Update documentation and the changelog when the public surface changes.

By contributing, you agree that your contribution is licensed under the
existing [Apache-2.0 License](LICENSE).

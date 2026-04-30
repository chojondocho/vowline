# Security Policy

Vowline is an instruction package with optional local install helpers. It does not collect data, call network services, or execute external tools beyond local file copy and text editing performed by `install.py` and `uninstall.py`.

## Report a vulnerability

Open a private security advisory or contact the repository maintainer listed on GitHub. Include:

- affected file and version or commit;
- reproduction steps;
- expected impact;
- suggested fix, if known.

## Security boundaries

Vowline instructs agents not to perform irreversible or externally visible actions without explicit approval. Host tools, permissions, organization settings, and platform policies still govern what an agent can actually do.

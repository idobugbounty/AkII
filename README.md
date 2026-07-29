# AkII

> A lightweight HTTP security header analyzer

AkII is an open-source security tool for analyzing HTTP response headers and identifying common security misconfigurations, such as weak or missing security headers.

> **⚠️ Early Development**
>
> AkII is in an early stage of development. Some features are still incomplete, and bugs are expected. The project is under active development, and new functionality will be added in future releases.

## Features

- Analyze HTTP security headers
- Detect common CORS misconfigurations
- Detect missing or insecure Content Security Policy (CSP)
- Human-readable terminal output
- JSON output for automation
- Lightweight and extensible YAML-based rule engine

## Why AkII?

AkII is designed to be extensible and automation-friendly.

It focuses on one task: analyzing HTTP security headers consistently.

It is suitable for:

- Security automation
- Bug bounty workflows
- Batch scanning with wordlists
- Integration into custom tools

## Installation

### From PyPI (Recommended)

```bash
pipx install akii
```

or

```bash
pip install akii
```

### From Source

```bash
git clone https://github.com/Mintesio/AkII.git
cd akii
pip install -e .
```
## Update

To update AkII to the latest version, use the command that matches your installation method.

### Installed with pip

Update AkII using:

```bash
pip install --upgrade akii
```

or:

```bash
pip install -U akii
```

### Installed with pipx

Update AkII using:

```bash
pipx upgrade akii
```

To update all packages installed with pipx:

```bash
pipx upgrade-all
```

### Check current version

You can check the installed version with:

```bash
akii --version
```

If you encounter any issues after updating, make sure you are running the latest version before reporting a bug.

## Uninstallation

If you installed AkII with **pipx**:

```bash
pipx uninstall akii
```

If you installed AkII with **pip**:

```bash
pip uninstall akii
```

If you installed AkII from source using `pip install -e .`:

```bash
pip uninstall akii
cd ..
rm -rf akii
```

## Usage

Scan a single target:

```bash
akii -T https://example.com
```

Scan multiple targets:

```bash
akii -w targets.txt
```

Show request headers:

```bash
akii -T https://example.com --request
```

Show response headers:

```bash
akii -T https://example.com --response
```

Verbose mode:

```bash
akii -T https://example.com --verbose
```

Save the report:

```bash
akii -T https://example.com -o report.txt
```

Export JSON:

```bash
akii -T https://example.com -jo report.txt
```

## Current Checks

- Cross-Origin Resource Sharing (CORS)
- Content Security Policy (CSP)

More security header checks will be added in future releases.

## Roadmap

- HSTS analysis
- Cookie analysis
- Cache-Control analysis
- Permissions-Policy analysis
- Referrer-Policy analysis
- HTML reports
- Improved JSON reporting
- Plugin system

## Contributing

Contributions are welcome.

If you find a bug, have a feature request, or would like to improve AkII, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

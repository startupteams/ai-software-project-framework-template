# TLS and Marion-local CI standard (2026-11-07)

Status: Human-directed implementation standard; rollout changes require review and production approval.

## Required defaults for every new service

1. Every browser-facing or API service uses HTTPS with a valid hostname, complete certificate chain and trusted issuer. Redirect HTTP to HTTPS where applicable; enable HSTS only after the hostname/cert path is verified. No `curl -k`, insecure HTTP fallback, browser certificate exception, `NODE_TLS_REJECT_UNAUTHORIZED=0`, or disabled certificate verification in production.
2. For private `.home.arpa` names, select and document the internal CA and distribute its **public root certificate** to managed clients (workstations, containers, VMs, CI runners). A publicly trusted cert is appropriate for eligible publicly resolvable domain names; do not assume a public CA can issue `.home.arpa` certificates. Never commit CA private keys or leaf private keys.
3. Use centralized certificate issuance/renewal and a DNS-01/wildcard strategy only for eligible real domains when appropriate. Define service ownership, reverse-proxy/SNI routes, renewal monitoring, expiration alerting, and rollback. Internal root CA distribution must be opt-in on clients that need it; never overwrite unrelated trust stores.
4. Every **eligible** GitHub Actions job, including tests, PR checks, scheduled jobs and deployments, uses startupteams organization self-hosted runners on Marion infrastructure, not GitHub-hosted Ubuntu. Prefer explicit `runs-on: [self-hosted, marion-ci]` (or the existing framework-approved `fromJSON(vars.CI_RUNS_ON || '["self-hosted","marion-ci"]')`). Deploy jobs use the existing `marion-deploy` runner contract. Audit the **effective** resolved labels and organization/repository runner group access, not merely workflow text.
5. Existing exceptions (macOS, Windows, Android SDK or hardware needs) need an approved, time-bounded exception in the owning repo's `FUTURE_WORK.md` with an accountable owner and migration acceptance criteria. The old opt-out variable that switches to hosted CI must not remain an undocumented default. Avoid exposing privileged LAN networks or secrets to untrusted fork PRs.
6. New-project bootstrap and CI lint must fail on insecure TLS settings, missing HTTPS health verification, unapproved hosted `runs-on`, and missing service-to-runner ownership metadata. Keep Markdown-only checks lightweight. Existing projects must migrate through separate reviewed PRs; never change production branches as part of inventory.

## Service onboarding acceptance checklist

- [ ] HTTPS endpoint has valid SAN, expiry, full chain and trust from a standard browser on managed devices.
- [ ] TLS 1.2+ enabled; TLS 1.3 preferred; redirect HTTP only after HTTPS is proven; no insecure-client bypass.
- [ ] Internal CA trust installation and renewal proven from Marion and Kathmandu managed clients where relevant.
- [ ] Certificate rotation tested; alerting covers expiring/mismatched/failed renewal.
- [ ] All applicable workflows use org self-hosted runners with required labels and least-privilege runner-group access.
- [ ] Runner verified online and job logs identify the expected self-hosted runner, with no billed hosted Linux job.
- [ ] Runner isolation, ephemeral workspace cleanup, cache permissions, credential boundaries and fork restrictions verified.
- [ ] Required PR status checks, release gates, post-deploy HTTPS probes and rollback remain working.
- [ ] Inventory report records owner, site, repo, FQDN, service port, certificate issuer/expiry/trust, runner, workflows, risk and evidence.
- [ ] CI validation results and manual production-approval gate recorded before promotion.

## Read-only inventory and rollout method

- Query repo inventory including active, archived and special-case workflows; enumerate `.github/workflows/*.yml` and `*.yaml` on default branch plus reusable/composite workflows; parse every `runs-on`, matrix, variable, nested reusable workflow and job condition. Gather run/job runner metadata and branch protections for live evidence.
- On Marion query VM139 deploy runner and VM168 CI runner, runner services, runner group labels and online state via read-only guest commands; inventory reverse proxy, DNS, public root trust stores, monitoring and hostnames from actual live guest/service manifests. Do not collect secrets/private keys. Proxmox host edits require separate permission.
- Probe all known service endpoints via HTTPS, collect SAN/issuer/expiry/chain, hostname match, protocol versions and client trust verification. Mark unprobed as UNKNOWN, not PASS. Run equivalent probes from offsite managed clients after the Kathmandu trust setup.
- Prioritize login/authentication, gateway, approval UI, Proxmox/PBS, deploy and monitoring, then all business services. Fix one service at a time in the owning repo, with canary, tests and rollback. Protect VM906 and all critical infrastructure; no live TLS or runner migration without approval.
- Report exact failing repos/endpoints, new exceptions and evidence; store work in owning `FUTURE_WORK.md` using the repo's stable FWID convention, not GitHub issues.

## Verification and rollback

Valid TLS: `curl --fail --silent --show-error https://SERVICE_FQDN/health` (never `-k`), plus an `openssl s_client -verify_return_error -servername SERVICE_FQDN -connect SERVICE_FQDN:443` trust/chain test with the managed trust bundle. CI: verify GitHub job runner metadata and labels are Marion self-hosted, both on pull request and scheduled/deploy workflows. Roll back via previous reverse-proxy/cert deployment and previous verified runner configuration; never silently fall back to GitHub-hosted minutes.

## Evidence state

As of 2026-11-07, the framework's `docs/CI_RUNNERS.md` already defines `marion-ci` on VM168 and notes legacy workflows. Marion deploy docs identify `marion-deploy` on VM139. These are documented topology, **not proof** that every repo, TLS endpoint or job has passed live inspection. Kathmandu deploy documentation describes a young site with planned deploy capability; do not assume a live Kathmandu runner.

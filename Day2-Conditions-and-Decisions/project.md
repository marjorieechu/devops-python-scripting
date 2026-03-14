# Day 2 Mini-Project

## Project

Build a basic DevOps access checker in `project.py`.

The script should decide whether a user can access a deployment environment.

## Inputs

Use variables such as:

- `username`
- `environment`
- `has_vpn`
- `is_on_call`

## Suggested Logic

- if VPN is missing, deny access
- if environment is `"production"` and user is not on call, deny access
- otherwise allow access

## Goal

You are practicing decisions, not complexity. Keep the script simple and readable.

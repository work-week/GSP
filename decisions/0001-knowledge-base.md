# 0001 — A Git knowledge base as the single source of truth

**Date:** 2026-10-19
**Decided by:** Krischan
**Status:** accepted

## Context

Information about GSP is spread across chats, calls and screenshots. AI chat history does not carry over between sessions, tools or models.

## Decision

Keep everything we know and decide about GSP in this private Git repository as Markdown. `AGENTS.md` holds the rules and map; `CLAUDE.md` loads it for Claude Code. Every session that changes something leaves a log.

## Why

A new chat or agent reads the repo and is up to speed. Git history shows what changed, when and why. Markdown can later be built into a browsable site.

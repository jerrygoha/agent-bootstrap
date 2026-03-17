# agent-bootstrap

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

Codex, Claude Code, OpenCode를 위한 프로세스 중심 AI 코딩 환경 부트스트랩입니다.

`agent-bootstrap`은 최신 AI 코딩 도구에 공통으로 적용할 수 있는 `superpowers` 워크플로우, 역할 기반 서브에이전트, 토큰 효율적인 실행 방식, 다국어 설치 문서를 제공합니다.

> 이 문서는 `README.md`의 한국어 번역본입니다. 기준 문서는 영어판입니다.

## 왜 agent-bootstrap을 써야 하나?

- Codex, Claude Code, OpenCode 각각에 따로 프롬프트 스택을 유지하지 않고, 하나의 `superpowers` 기반 워크플로우를 공유할 수 있습니다.
- 계획, 구현, 리뷰, 검증, 릴리스 역할을 서브에이전트와 공통 프롬프트 코퍼스로 분리해 일관된 협업 흐름을 유지할 수 있습니다.
- 범위가 명확한 작업, 짧은 handoff, 재사용 가능한 skill 중심으로 흐르게 해 토큰 낭비를 줄이는 process-first 실행 모델을 제공합니다.
- 하나의 범용 installer 억지 적용이 아니라 각 하네스의 네이티브 방식에 맞춘 어댑터를 제공합니다.
  - Codex는 managed `.codex` 설정과 latest `superpowers`
  - Claude Code는 marketplace entry와 generated agent plugin package
  - OpenCode는 generated agents와 native plugin wiring
- credential, private MCP endpoint, 개인 경로, 머신별 trust state를 public baseline에 넣지 않도록 설계되어 있습니다.
- 영어, 한국어, 일본어, 중국어 간체 문서를 같이 제공해 동일한 레포에서 온보딩할 수 있습니다.

## 이 레포가 하는 일

이 레포는 특정 도구 하나에 묶이지 않고, 여러 코딩 하네스에 설치할 수 있는 공통 운영체계의 source of truth입니다.

대상 하네스:

- Codex
- Claude Code
- OpenCode

OpenClaw 연동 방법도 문서화하지만, OpenClaw는 first-class bootstrap target이 아니라 integration layer로 취급합니다.

## 설치 가이드

- Codex: [docs/README.codex.md](docs/README.codex.md)
- Claude Code: [docs/README.claude.md](docs/README.claude.md)
- OpenCode: [docs/README.opencode.md](docs/README.opencode.md)
- OpenClaw integration: [docs/README.openclaw.md](docs/README.openclaw.md)

## 아키텍처

레포는 두 계층으로 나뉩니다.

- shared core
  - `AGENTS.md`
  - `agents/*.md`
  - `shared/agent-metadata.json`
  - 공통 process-first 헌법과 역할 프롬프트 본문
- harness adapters
  - `.codex/`
  - `.claude-plugin/`
  - `.opencode/`

shared core는 운영 모델을 한 번만 정의하고, 각 adapter가 이를 대상 하네스의 네이티브 형식으로 변환합니다.

## Superpowers 연동

이 bootstrap은 `obra/superpowers`를 중심으로 설계되어 있습니다.

- Codex는 `~/.agents/skills/superpowers` symlink 패턴을 사용합니다.
- OpenCode는 `superpowers@git+https://github.com/obra/superpowers.git` plugin line을 사용합니다.
- Claude Code는 두 층으로 나뉩니다.
  - upstream 공식 `superpowers` skill library
  - 이 레포가 생성하는 Claude agent plugin package

목표는 `superpowers` skill library를 이 레포에 복사하지 않고 upstream을 그대로 재사용하는 것입니다.

## 레포 구조

- `AGENTS.md`
  - 공통 헌법 템플릿
- `agents/`
  - 공통 역할 프롬프트 본문
- `shared/agent-metadata.json`
  - 공유 설명과 OpenCode capability metadata
- `.codex/`
  - Codex installer, template, install guide
- `.opencode/`
  - OpenCode installer, template, install guide
- `.claude-plugin/marketplace.json`
  - 레포 수준의 Claude marketplace entry
- `plugins/process-first-agents/`
  - 생성된 Claude plugin package
- `scripts/render_claude_plugin.py`
  - shared prompt corpus로부터 Claude plugin package를 다시 생성
- `docs/`
  - 하네스별 가이드, repo metadata 가이드, OpenClaw 문서
- `tests/`
  - installer, plugin metadata, README 기대사항 검증

## 검색성과 발견성

GitHub 레포의 발견성은 일반 웹 SEO보다 repository metadata 영향을 더 많이 받습니다.

이 레포는 다음 방식으로 발견성을 개선합니다.

- 키워드가 잘 들어간 canonical README
- 다국어 README
- GitHub repository description과 topics
- [docs/repo-metadata.md](docs/repo-metadata.md)에 정리된 social preview 가이드

## 제약

이 레포에는 public하게 공유해도 안전한 baseline만 들어가야 합니다.

넣지 말아야 할 것:

- private MCP endpoint
- 개인 프로젝트 경로
- 조직 전용 secret
- 머신별 trust configuration
- credential, token, auth state

## 업데이트

- Codex와 OpenCode: pull 후 각 installer를 다시 실행
- Claude Code: pull 후 `python3 scripts/render_claude_plugin.py --partner-name "<Name>"`를 다시 실행하고 plugin을 갱신

## 레거시 파일

이전 Codex-only bootstrap 시절의 파일 일부가 아직 남아 있습니다.

- `codex-home/`
- `scripts/install.py`
- `scripts/install.sh`
- `prompts/fresh-install.md`

이들은 호환성 entrypoint이며, 장기적인 멀티 하네스 구조의 중심은 아닙니다.

## 테스트

installer와 metadata 테스트는 Python `unittest`를 사용합니다.

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

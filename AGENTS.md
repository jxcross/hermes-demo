# AGENTS.md — hermes-demo

## GitHub 워크플로우 (인간 승인 게이트)
- 작업은 **이슈에서 시작**한다. `main`에서 새 브랜치 생성 → 코딩 → 커밋.
- **`main`에 직접 푸시 금지**(브랜치 보호). 항상 **draft PR** 생성:
  `gh pr create --draft --base main`, 본문에 결정 근거·영향·테스트 결과 요약과 `Closes #<issue>`.
- **PR을 스스로 머지하지 않는다.** 사람(jxcross)이 리뷰하고 머지한다.
- 커밋/PR 후 진행 상황을 보고한다.

## 모델
- 코딩/테스트는 로컬 모델(`qwen3-coder-64k`)로.

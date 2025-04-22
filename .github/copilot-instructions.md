# Project Guidelines
## Documentation Requirements
- Update relevant documentation in /docs when modifying features
- Keep README.md in sync with new capabilities
- Maintain changelog entries in CHANGELOG.md

## Naming Conventions
- Code must include appropriate comments.
  - All classes and methods must have comments.
  - All variables and parameters must have comments.
  - Appropriately add comments throughout the entire code.
  - All comments must be written in English.

## Architecture Decision Records
Create ADRs in /docs/adr for:
- Major dependency changes
- Architectural pattern changes
- New integration patterns
- Database schema changes
    - Follow template in /docs/adr/template.md

## Testing Standards
- Unit tests required for business logic


## General
- DO NOT BE LAZY. DO NOT OMIT CODE.
- Each step should be committed separately to preserve history.
- OS is Windows 11
- 分階段實作，先產生計畫，並在 Github 上面新增 issue 來追蹤進度，每完成一步驟就更新 issue 並加入 comment 補充說明
  - When creating issue, remember to add corresponding labels
  - note: remember always update the issue and add issue comment everytime


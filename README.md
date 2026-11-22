# synths-to-go

Portable instruments with analog voices, shimmer and warmth. **The family principle:** each one is a portable sound module with a way to carry a keyboard with it, flexible and not tied to any one keyboard model. "synths-to-go" is a working title. They're designed with an AI product team (an orchestrator, a systems designer, a visual designer and a design director) following Adam's design-buds process.

Site: https://adamtrabold.github.io/synths-to-go/

| Instrument | What it is | Where it lives |
|---|---|---|
| **big energy** | The Model D clone with 4-voice paraphony | `design/`, `eng/`, `docs/`, `versions/` (see below) |
| **port-a-poly** | A true portable analog poly | [`port-a-poly/`](port-a-poly/README.md) |
| **floss** | The string machine: analog strings with shimmer, from first principles | [`floss/`](floss/README.md) |

Start with [`HANDOFF.md`](HANDOFF.md): status, decisions, and how to pick up the work.

## Folders

| Folder | What's in it |
|---|---|
| [`VERSIONS.md`](VERSIONS.md), `versions/` | Big Energy's locked sets (current: **v1.1**) |
| `design/` | Big Energy design: concepts, the owner record (`design/owner.md`, which covers every instrument), team notes, render code |
| `eng/` | Big Energy engineering spec (`budget-variant.md`), research, circuit simulations |
| `docs/` | Big Energy architecture and feature sets |
| `explore/` | Side research, including polyphonic and hybrid ideas |
| `archive/` | Paused work: the full-size Model D clone, paused concepts, superseded FOLD sheets |
| `ref/` | How to fetch the CA-72 reference netlists |
| `site/` | The project site; `bash site/publish.sh` rebuilds it |

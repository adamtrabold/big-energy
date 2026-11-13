# Key sourcing: real, bought parts, 25 keys, ~280-300 mm, silent, qty 1, US

Constraints (owner-requirements.md): real purchased parts, no 3D-printed keys/knobs, no harvested keybed, "feels like an instrument", as silent as possible, 25 keys (2 octaves + top C = 15 white keys) in ~280-300 mm. So white-key pitch must be <= ~19 mm (15 x 19.05 = 286 mm). Date of research: 2026-11-12. Prices are as shown on the cited pages; "n/s" = not shown.

## Key finding
No vendor sells a bare, new, 25-key mini keybed to individuals. The only true OEM keybeds sold to individuals (Fatar via Doepfer) are full-size keys, so 25 keys = 15 x ~23.5 mm = ~350 mm (my arithmetic, standard piano pitch), which breaks the width limit. Everything that fits the width is a switch-per-key build: commercial switches + commercial keycaps, which gives up the long piano-key lever feel.

## Ranked table

| Rank | Option | Width (25 keys) | Travel | Noise | Velocity | Qty-1 price | US availability | Sensing |
|---|---|---|---|---|---|---|---|---|
| 1 | Gateron low-profile Hall-effect (HE Jade Pro etc.) + bought caps | 15 x 19 = ~285 mm if switch pitch allows (caps/PCB layout decide; low-profile pitch ~18-19 mm, unverified) | 3.3 mm total, 0.1 mm pre-travel, 40 gf (keeb-finder) | "moderately quiet", no click; not silent-rated | YES: analog position, so velocity from two thresholds/time-of-travel in MCU | $0.84/switch at Nuphy (US) = ~$21 for 25 (keeb-finder); OZO lists a 10-pack at GBP 8.25 (UK/HK ship) | Nuphy is US-based; confirm stock | Hall (linear sensor on PCB, needs analog mux/ADC; switches are not plain contacts) |
| 2 | Kailh Choc V2 Deep Sea Mini (silent) + Choc V2 caps | 15 x 18 = ~270 mm (Choc spacing) | 2.8 mm total, 1.3 mm pre (Keebio) | Built-in dampeners on down and up stroke; quietest mechanical option; still some bottom-out | Only with 2nd contact/Hall add-on (switch is on/off) | $0.70/switch at keeb.io = ~$17.50 for 25; stock n/s | US (keeb.io) | Contacts; velocity needs dual contact or added Hall |
| 3 | Gateron KS-33 low-profile Silent 2.0 | ~285 mm | 3.0 mm total, 1.7 pre; 45-55 gf | Reduces bottom-out/return noise, "not fully silent" (Gateron) | No (on/off) | price n/s from Gateron | check retailers | Contacts |
| 4 | Fatar via Doepfer TP/9 3-oct (weighted, aftertouch) or TP/7 | ~350+ mm for 25 full-size keys (too wide); TP/7 2-oct discontinued, EUR 45 | Real piano-style pivot key | Quietest and best feel of all (felt-damped) | YES (dual contact) | EUR 120 (TP/9), plus EUR 11 cable set, plus MIDI scanner (MKE EUR 90-95) | Doepfer ships from Germany; Thomann/US resellers carry MKE parts; keybeds not seen at US retailers | Dual-contact matrix |
| 5 | Silicone pad sheets (SparkFun 4x4, $5.25, 190-210 g force) | pitch not stated | short | Near silent | No without FSR/pressure sensing | $5.25 | SparkFun US (stock listing inconsistent: in stock / backorder) | Conductive pill on PCB traces; add FSR for velocity |
| 6 | OP-1 replacement keyboard ($119.99, iFixit) | n/a | scissor | quiet | n/s | $119.99 | TE spare | Rejected: it is another commercial product's keybed, which the owner ruled out |
| X | Alibaba "keyboard module"/conductive rubber for Korg PA500 | 13 notes | | | | MOQ 1,000 at $0.02 | | Not viable (MOQ) |

## How the references source keys
- OP-1: iFixit mentions scissor mechanisms on the eight small keys; the only purchasable part is the whole OP-1 keyboard at $119.99. No off-the-shelf equivalent is a piano-shaped scissor key.
- nanoKEY: I did not get a confirmed teardown (searches returned nanoKONTROL2 only); membrane/rubber is the owner brief's assumption, UNVERIFIED.
- Off-the-shelf laptop scissor switch kits: searches found nothing sold as individual kits in the US; a deskthority thread on the topic failed to load. Treat as unavailable.
- Piano-shaped keycaps: found only blank Choc V1 caps (keeb.io $0.15, 16.5 x 17.5 mm, 1u only) and POM/PBT caps (MoErgo, splitkb); no commercial piano-key long caps found. Black keys can be 1u caps raised on a second row; white keys 1u only means no real piano shape. Laser-cut acrylic caps from a service are the likely route (needs a quote).
- Hall-piano precedents: a Hackaday mini piano uses printed levers + A1324 Hall sensors (velocity not implemented); KOOP Melodicade uses MX + a second tact switch for velocity (~$180 materials).

## Recommendation
- Full instrument: Option 1, Hall low-profile switches with a thin keys PCB (linear Hall sensors + analog mux), velocity from MCU. Quiet, velocity, ~$21 switches. Risk: feel is switch-like, not lever-like; confirm Nuphy stock and caps. If the owner prefers real piano feel and accepts a wider body, Fatar TP/9 is the only true keybed but does not meet 25 keys in 300 mm.
- Budget instrument: Option 2, Kailh Choc V2 silent, ~$17.50 for 25 switches, no velocity (or add a Hall sensor later). Mount switch PCB separate from the main board.

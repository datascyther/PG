# 06 — PRODUCTION

The deck has two slides titled "Prod" and "Process" with one word on each. This is what
belongs on them.

---

## 1. The kit, minimum

| Item | Why | Note |
|---|---|---|
| Camera | any recent phone shoots 4K that outperforms what most Indian business channels upload | the raw dump already contains iPhone 13 Pro footage — that is enough to start |
| **External microphone** | **the only non-negotiable item on this list** | viewers forgive soft focus; they leave on bad audio, and they leave in four seconds |
| Lavalier + a recorder | for field work where the subject moves | one clip mic on the person speaking, always |
| Tripod or gorilla pod | a locked-off second angle costs nothing and saves the edit | |
| One soft light | a window is better than a ring light; a ring light is better than a ceiling tube | |
| Grey card or a white sheet of paper | white balance, once per location | |

Total, if starting from zero: one microphone and one light. That is the whole capital
requirement for the first six episodes.

---

## 2. Two shoot types, and only two

### Field — On the Floor, Post-Mortem (8–12 min)

| | |
|---|---|
| Crew | 1 (him) + 1 (shooter) + the person who works there |
| Time on site | 45–60 min, of which 12 min is usable |
| Audio | one lav on the worker, one on him, room tone for 30 s |
| Rule | the first 40 seconds are one continuous walk. No cutaways. No music. |
| Permission | site permission in writing before the day; a factory floor is not a public place |

### Set — The Long Conversation (60–75 min)

| | |
|---|---|
| Crew | 2 minimum (camera, sound) |
| Time | 4 hours per guest: 45 min setup, 75 min record, 30 min re-set for cutaways, buffer |
| Audio | two lavs, two channels, recorded separately; a backup recorder running |
| Cameras | two — a wide that never moves and a tight that follows the speaker |
| Rule | never record a guest without a signed release and a stated right to not use it |

A weekly 60–75 minute podcast is a **set, a guest pipeline and an editor**. All three are
missing today. Ship it monthly until two of the three exist.

---

## 3. The field run sheet (45 minutes)

| Min | What |
|---|---|
| 0–5 | walk the space, find the light, decide the walk path |
| 5–10 | mic the worker, record 30 s of room tone |
| 10–15 | record the walk-through silent, so the edit has a spine |
| 15–35 | the four questions, one take each, no interruption |
| 35–40 | the object close-ups: the thing, the number, the label |
| 40–45 | his piece to camera, one take, standing where the number is visible |

Ask four questions, then stop talking. The format dies the moment he starts explaining
someone else's job for them.

---

## 4. Edit

1. **Proxies first.** 4K footage on a laptop timeline is how an episode takes three days.
2. **Cut the audio before the picture.** The episode is a conversation; the picture supports it.
3. **Vertical is a re-shoot, not a crop.** A 16:9 wide cropped to 9:16 loses the object. Frame
   the Short with its own take.
4. **Burn captions in.** Most viewing is silent; auto-captions mis-hear every Indian number.
5. **Loudness to −14 LUFS**, the platform standard, so the episode is not quieter than the ad
   before it.
6. **No music under speech.** A bed under talking is the fastest way to sound like a template.
7. **A receipt on screen.** Every number that appears gets a small, quiet source line in the
   corner — "his own post, 29 Oct 2023". It costs nothing, it is the channel's whole promise,
   and nobody else in the niche does it.

---

## 5. The visual system (locked once)

| Element | Rule |
|---|---|
| Typeface | one family for titles, cards and lower-thirds; picked once, never re-picked |
| Colour | one dark neutral, one warm accent, white text. No gradients |
| Lower third | name + one line of context, never a job title alone |
| Card layout | the existing `HEADLINE_FORMAT.md` spec — 18–24 words, one caps run, one emphasis device |
| Logo | none on the video. A channel mark in the thumbnail corner only |
| Aspect | 16:9 long-form, 9:16 everything else, 4:5 for cards |

---

## 6. Assets: naming, sidecars, and the two traps

The folder convention mirrors `startup-pedia-engine/engine/assets/`:

```
assets/YYYY-MM-DD_<place>_<subject>/
  RAW/                 camera originals, never edited in place
  02_AUDIO/            recorder files, one folder per person
  03_STILLS/           frames pulled for thumbnails and cards
  SIDECAR.md           what it is, who is in it, consent, clearance, date
```

Sidecar template:

```markdown
# sidecar
file: IMG_2546.HEIC
captured: 2026-10-01 09:56 UTC   (EXIF, not the filename)
place: jury set, second shooting day
who is visible: Puneet (consented), one host (consent pending)
clearance: HOLD until consent or show release
use: receipt only — no episode data in this frame
```

### Trap 1 — HEIC is not a normal image file

`ffprobe` reports an iPhone HEIC as dozens of 512×512 HEVC tiles, so any frame-extraction
script produces tile thumbnails instead of a picture. Resolve `.heic` to a sibling `.jpg`
before probing.

### Trap 2 — conversion silently rotates

`sips -s format jpeg` dropped the EXIF orientation tag on three files, leaving 4032×3024
JPEGs that would have gone to upload sideways. Use:

```bash
ffmpeg -y -i shot.HEIC -frames:v 1 -q:v 2 out.jpg
```

then **open the output and look at it** before it is attached to anything. Never attach a
converted image you have not looked at.

### Trap 3 — provenance

One asset in the last dump carried a signed C2PA manifest declaring it AI-generated
(`softwareAgent: ChatGPT`, `trainedAlgorithmicMedia`). It was an image of a real, identifiable
person, built from real photographs.

**Rule:** every incoming file is checked for C2PA/EXIF provenance before it is used. An asset
with synthetic provenance is never a thumbnail, never a card, and never captioned with a real
person's name.

---

## 7. What cannot be made yet

Listed so nobody plans around it:

| Missing | Blocks | Unblocked by |
|---|---|---|
| A set | The Long Conversation | one room, two lights, a backdrop — a day's work |
| A guest pipeline | The Long Conversation | his introduction to five people |
| An editor | weekly long-form | one person, part-time, the actual constraint |
| Site permissions | On the Floor | a written yes from one plant |
| B-roll of any past venture | most Post-Mortems | the originals from the raw dump, re-exported |

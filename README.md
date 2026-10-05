# Dos Minutos — Spanish Listen & Speak

A polished single-page web app for **beginner Spanish conversation practice**. Short (~2 minute) scripted dialogues where you **listen** to a partner (TTS) and **speak** your reply (microphone). Spoken replies **automatically continue** the conversation; tap choices are an optional fallback.

## How to run (Mac)

From this folder:

```bash
cd spanish-practice
# Option A — open the file directly
open index.html

# Option B — local HTTP server (recommended)
python3 -m http.server 8080
# then open http://localhost:8080
```

You can also drag `index.html` into Chrome, or use `npx serve .`.

**Chrome (or Chromium) is strongly recommended** — Web Speech Recognition (`webkitSpeechRecognition`) works most reliably there. Safari/Firefox support for Spanish speech-to-text is limited or missing.

## Features

- **Listen** — partner lines via Web Speech API (`SpeechSynthesis`), with voice loading (`onvoiceschanged` + polling)
- **Voice status** — shows which Spanish voice is selected, or a warning + tip if none is found
- **Cloud voice toggle** — optional Google Translate TTS fallback (`Audio` element) when no Spanish system voice, or when you prefer cloud audio
- **Play / Slow (0.75×)** — highlighted while speaking; first line may ask for a tap to unlock audio
- **Speak** — after the partner finishes TTS, the mic **auto-listens**; any non-empty speech advances the dialogue (fuzzy match is feedback-only)
- **Tap mic** anytime to re-listen if auto-listen missed you
- **Tap choices** remain as a quiet optional fallback (not required to continue)
- **~2:00 timer**, **6 scenarios**, English reveal, practice summary
- Pure static frontend — no backend, no API keys

## Mic & speech recognition

1. Allow **microphone permission** when the browser asks (often on **Play first line** / Play).
2. Partner speaks → listening starts automatically → you speak → the conversation continues.
3. **Tap the mic while listening** means “I’m done” — the app soft-stops recognition (`stop()`, not `abort()`), keeps any interim transcript, and **always advances** the dialogue (even if the transcript is empty).
4. Chrome often never sends `isFinal: true`; the app keeps `lastTranscript` from interim results and advances on `onend` when anything was heard. If nothing was heard, it shows “Didn’t catch that” and may auto-relisten once.
5. Matching choices is optional feedback (“Heard: …”, closest choice highlight). Hard abort is only used when partner TTS starts or you leave the session.
6. Recognition never runs while partner TTS is playing (`onend` / audio ended first).

If the mic is denied or unsupported, tap choices still work.

## Spanish voice tips (macOS)

If you hear silence or a non-Spanish voice:

1. **System Settings → Accessibility → Spoken Content → System Voice → Manage Voices…** (wording varies by macOS version) and download a **Spanish** voice (Spain or Latin America).
2. Or **System Settings → General → Language & Region** and add Spanish; then check browser language / voice packs.
3. In **Chrome**, open `chrome://settings/languages` and ensure Spanish is available; restart Chrome after installing OS voices.
4. Or enable **Use cloud voice** on the home screen (needs network; may be blocked on some networks).

On remote Linux desktops, local TTS is often missing — use **Use cloud voice** or install `espeak`/browser language packs, and always tap **Play first line** if autoplay is blocked.

## Scenarios

1. **At the café** — order, size, pay  
2. **At a restaurant** — table, food, bill  
3. **Asking for directions** — left, right, distance  
4. **Shopping for clothes** — size, color, fitting room  
5. **At the post office** — package, stamps, delivery time  
6. **Meeting someone new** — name, origin, work  

## Caveats

- **Speech recognition** needs Chrome (or a Chromium-based browser) and mic permission over a secure context (`localhost` or `https`).
- **Cloud TTS** uses a public Google Translate endpoint — it can fail offline, get rate-limited, or be blocked; local voices are preferred when available.
- First speak may need a **user gesture** (Play / Play first line), especially on remote desktops.
- Matching is fuzzy (accents/case stripped, keyword overlap) and does **not** block progress — tap a choice only if you prefer not to speak.

## Phone app (PWA)

The app can be installed on a phone. It needs to be served over **HTTPS** because the mic and speech recognition only work in a secure context.

- **iPhone (Safari):** open the URL, then tap Share → **Add to Home Screen**.
- **Android (Chrome):** open the URL, then tap ⋮ → **Install app** / **Add to Home screen**.

Files: `manifest.webmanifest`, `icons/` (180 apple-touch, 192, 512, maskable 512, favicon), `sw.js` (service worker).

The service worker fetches from the network first and falls back to the cache. When you're online you always get the newest `index.html`, so weekly scenario edits show up the next time the app opens and nobody has to reinstall. Offline, the last cached copy loads instead. To force every cached file to refresh, bump `CACHE_VERSION` in `sw.js`.

### Publish / redeploy

```bash
cd /workspace/spanish-practice && ./deploy.sh "Weekly scenario update"
```

On the first run this creates the public GitHub repo `dos-minutos` and turns on GitHub Pages. After that, each run commits and pushes. The URL is `https://<github-user>.github.io/dos-minutos/`. You need to be signed in with `gh` first (`gh auth login`).

### iPhone notes

- Audio and mic start from taps (Play, Play first line, 🎤), because iOS blocks speech that doesn't come from a gesture.
- Speech recognition in Safari uses Apple's speech service, so **Siri & Dictation must be enabled**. It may **not work at all in the installed home-screen app**. When recognition fails or stalls there, the app says so and the tap-a-reply buttons take over. If you want to speak your replies, use the same URL in a normal Safari tab.

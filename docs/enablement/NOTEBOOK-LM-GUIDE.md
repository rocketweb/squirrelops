# Notebook LM Guide

How to use this enablement corpus with Google's Notebook LM. Notebook LM ingests source documents and generates audio overviews, study guides, FAQs, mind maps, and a Q&A chat over the sources. The corpus in this directory is designed to be fed in directly.

## Step 1. Get the corpus into Google Drive

Two options:

**Option A. Manual upload.** Zip this directory, upload to Drive, unzip. Simplest. Re-upload when files change.

**Option B. rclone sync.** One-time setup, then sync this directory automatically.

```
brew install rclone
rclone config       # set up Google Drive remote (call it "gdrive")
rclone sync /Volumes/ssk/code/squirrelops/docs/enablement gdrive:squirrelops-enablement
```

Add a cron or a manual sync command when you update the corpus.

## Step 2. Create the notebooks

I recommend three separate notebooks, each scoped to a specific kind of conversation. Notebook LM works better with focused source sets than with everything dumped in at once.

### Notebook 1. "SquirrelOps Sales Prep"

For prospect calls. CISOs, AppSec leads, SOC managers, AI platform owners.

**Sources to add:**
- `00-overview.md`
- `01-architecture.md`
- `02-numbers-and-proof.md`
- `03-framework-alignment.md`
- `04-pricing.md`
- `07-competitive-landscape.md` (when written)
- `08-objections-and-answers.md` (when written)
- `09-buyer-personas.md` (when written)

**Suggested actions in this notebook:**

1. Click "Audio Overview" and generate a 10-15 min two-host podcast. Listen to it during a morning walk before any sales call. Notebook LM will summarize the product, surface the key proof points, and discuss the buyer personas conversationally.

2. Click "Study Guide" to get a structured glossary and Q&A list. Print or save as a PDF.

3. Use the chat interface to drill specific scenarios:
   - "What would a CISO at a fintech ask me about this product?"
   - "Walk me through how I'd respond if someone said 'we already have Lakera, why do we need this?'"
   - "Quiz me on the 98.5% capture rate. Where does it come from?"

### Notebook 2. "SquirrelOps Partnership Prep"

For partnership conversations with adjacent vendors. SIEM vendors, SOAR platforms, threat intel platforms (Flowsint, OpenCTI), AI security companies, security tooling integrators.

**Sources to add:**
- `00-overview.md`
- `01-architecture.md`
- `06-deployment-integration.md` (when written)
- `10-partnership-talk-track.md` (when written)
- Optionally: `04-pricing.md` (only if the conversation is going commercial)

**Suggested actions:**

1. Generate an Audio Overview. It'll cover the architecture and integration points. Useful prep before a partnership call.

2. Use the chat:
   - "How does SquirrelOps' STIX output integrate with OpenCTI?"
   - "What would a SOAR vendor want to know about us?"
   - "If a SIEM vendor asked to build a native connector, what's the technical spec they'd need?"

### Notebook 3. "SquirrelOps Technical Deep Dive"

For deeper technical conversations with engineers, AppSec teams, or red teams.

**Sources to add:**
- `01-architecture.md`
- `02-numbers-and-proof.md`
- `05-modules.md` (when written)
- `06-deployment-integration.md` (when written)
- `11-faq.md` (when written)

**Suggested actions:**

1. Use chat to walk through:
   - "Explain the four-layer detection pipeline in order, including latency at each layer."
   - "How would I explain bit-identical reproducible builds to a senior engineer?"
   - "What's the failure mode if the ML classifier is wrong? Does the customer notice?"

## Step 3. Daily drill loop

Once the notebooks are set up, the drill loop is:

1. **Morning audio.** 10 minutes. Listen to the Sales Prep notebook's audio overview while making coffee. Once a week regenerate it with a fresh focus prompt (e.g., "focus on framework alignment this week").

2. **Five-minute quiz.** Open the notebook, use the chat to ask "Quiz me on three random topics." Notebook LM picks topics from the source material and asks questions. Answer them out loud. Self-grade.

3. **Pre-call drill.** Before any actual sales or partnership call, spend 10 minutes asking the relevant notebook scenario-specific questions. "I'm meeting with a CISO at a healthcare company tomorrow. What should I anticipate?"

## Audio overview tips

Notebook LM's audio overview is the killer feature. Two AI hosts discuss the source material in a podcast format, ~10-15 minutes. To make it more useful:

- **Use the focus prompt.** When generating, click "Customize" and tell it what you want emphasized. Example: "Focus on the framework alignment discussion and how to handle GRC buyer objections."
- **Regenerate weekly.** The audio is generative. Different runs surface different angles.
- **Listen on 1.5x speed.** The hosts are slow on default. Most useful at 1.25 to 1.5x.

## What Notebook LM is not great at

- Direct citation of specific text passages. It will paraphrase. If you need exact quotes for a customer-facing doc, go to the source markdown.
- Numerical accuracy in audio. The hosts sometimes round numbers. Trust the source docs, not the audio, when citing.
- Real-time learning. If you update the source docs, you need to re-sync the notebook (remove and re-add the source). Audio overviews are not auto-regenerated.

## Maintenance

When you update any markdown file in this directory:

1. Re-sync Drive (rclone sync command above, or manual re-upload)
2. In Notebook LM, remove the updated source and re-add it
3. Regenerate the audio overview if the change was substantive

Plan a weekly 15-minute maintenance window: re-sync Drive, regenerate audio overviews, check that the notebooks still reflect current product state.

## What good looks like after 30 days

If you've used this consistently for a month:

- You can articulate the product in 30 seconds without notes
- You can name and describe each of the four detection layers
- You can map SquirrelOps to NIST CSF, AI RMF, CIS Controls v8, and OWASP LLM Top 10 in real time
- You can quote the headline numbers (98.5%, 0 FP, <2 min) with provenance
- You can handle the top 10 objections without hesitation
- You can adapt the pitch on the fly for CISO vs. AppSec vs. GRC vs. SOC manager

That's the goal. Notebook LM is the practice harness. The corpus is the material.

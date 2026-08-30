# V1 Qwen×Gemma Access Preflight Failure

Date: 2026-08-30
Status: `FAILED_BEFORE_ANY_CORRECTION OUTCOME`

The v1 error bank completed outcome-blind construction: 480 unique erroneous traces over
60 common GSM8K and 60 common MATH-500 problems. The local tokenizer/config preflight then
received HTTP 403 for `google/gemma-2-2b-it` at the frozen revision. Read-only server
inspection found no cached Gemma 2B or 9B weights. The 4090 host could reach Qwen through
`hf-mirror`, while the same frozen Gemma path returned HTTP 403.

No model generated a correction, no outcome was scored, and no scientific threshold was
changed. V1 is not a scientific negative result. It is preserved as an external-access
engineering failure. The separately versioned v2 Qwen2.5×Qwen3 grid narrows the claim to
lineage interaction and cannot substitute for eventual cross-provider replication.

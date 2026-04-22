# TODO: Remove Unwanted LLM Error & Greeting Output

## [✅] 1. Update llm_utils.py
   - Model changed to "gemini-pro" ✅ (no 404 errors)
   - Fallback greeting updated (minor, as LLM now works)
   - No other prints

## [✅] 2. Test CLI apps
   - `python app.py`: No LLM errors, deprecation warning only (library)
   - "hi" input will use LLM, no unwanted greeting
   - Run `python app.py`
   - Input "hi" → Verify no ⚠️ errors, no generic greeting
   - Test RAG query (e.g. "pricing") &amp; lead flow (e.g. "start")
   - Same for `python app_cli.py`

## [ ] 3. Test Web app
   - `streamlit run app_web.py`
   - Verify no console errors, responses work

## [ ] 4. Optional: Polish CLI prompts
   - Change "You: " → "User: " if desired

## [ ] 5. Complete &amp; cleanup
   - Update this TODO with results
   - Commit changes if needed


"""Check that ANTHROPIC_API_KEY and OPENAI_API_KEY both work.

Run this once before Week 6 starts:

    python experiment/verify_api_keys.py

It makes one tiny, cheap test call to each provider and reports pass/fail.
It never prints your actual key values, only whether each one worked.
"""

import os

try:
    from dotenv import load_dotenv
except ImportError:
    raise SystemExit(
        "The 'python-dotenv' package isn't installed. Run "
        "`pip install -r requirements.txt` first."
    )

load_dotenv()  # reads a .env file in the current folder, if one exists


def check_anthropic():
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        return False, "ANTHROPIC_API_KEY is not set (check your .env file)"

    try:
        import anthropic
    except ImportError:
        return False, "the 'anthropic' package isn't installed (pip install -r requirements.txt)"

    try:
        client = anthropic.Anthropic(api_key=key)
        resp = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=10,
            messages=[{"role": "user", "content": "Reply with exactly the word: ok"}],
        )
        text = "".join(b.text for b in resp.content if b.type == "text").strip()
        return True, f"Claude replied: {text!r}"
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


def check_openai():
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        return False, "OPENAI_API_KEY is not set (check your .env file)"

    try:
        import openai
    except ImportError:
        return False, "the 'openai' package isn't installed (pip install -r requirements.txt)"

    try:
        client = openai.OpenAI(api_key=key)
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=10,
            messages=[{"role": "user", "content": "Reply with exactly the word: ok"}],
        )
        text = resp.choices[0].message.content.strip()
        return True, f"GPT replied: {text!r}"
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


if __name__ == "__main__":
    print("Checking your API keys, this makes one tiny test call to each...\n")

    results = {
        "Claude (Anthropic)": check_anthropic(),
        "GPT (OpenAI)": check_openai(),
    }

    all_ok = True
    for name, (ok, detail) in results.items():
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: {detail}")
        all_ok = all_ok and ok

    print()
    if all_ok:
        print("Both keys work. You're set for Week 6.")
    else:
        print("At least one key didn't work, see the FAIL line(s) above.")

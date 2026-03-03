# Fixed Easy Crackme — Reverse Engineering Write-Up

**Category:** Reverse Engineering  
**Difficulty:** Easy  
**Files:** `698d2206e2ba6023bfacaa4f.zip` (password: `crackmes.one`) → `CrackMeEasy.exe`

---

## TL;DR

The binary stores the correct password **in plaintext** inside the `.data` section as the ASCII string:

> **EasyPassword**

User input is read into a `std::string`, its length is checked, then `memcmp()` compares it directly against the plaintext password.

---

## Environment / Tools

You can solve this with pure static analysis (no Windows needed):

- `file`, `strings`, `objdump` (Linux/macOS)
- (Optional) Ghidra/IDA/BinaryNinja
- (Optional) x64dbg on Windows for dynamic confirmation

---

## Artifact Fingerprint

### File identification

```bash
file CrackMeEasy.exe
# PE32+ executable (console) x86-64, for MS Windows, 6 sections

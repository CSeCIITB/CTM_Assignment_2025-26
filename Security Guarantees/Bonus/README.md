# Description



Help! I tried the previous binary with a different version of libc but the exploit stopped working!!!


---

# Instructions

Use the libc and challenge binary provided in this folder in place of the original ones. The simplest exploit possible in the previous one will not work here. Figure out why (perhaps a divisibility error).
<details>
  <summary>Hint</summary>
  You’ve gotta ROP your way in and ret your way out.
</details>

---

The instructions are the same as the main challenge — just run `pwninit` in the **Bonus** directory.

Try connecting to the bonus challenge remotely using:

```bash
nc challs.breachers.in 1345
```

# Submission
As before submit a writeup, the flag and the solve.py. Bonus Bonus for explaining why the previous exploit does not work here.


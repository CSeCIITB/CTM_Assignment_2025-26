
# Description

Everyone tells me to never use `gets`, but I just don't get the memo! I'm not afraid at all — in fact, here, I'll give you a binary with `gets`. I bet you can't exploit it!

Try connecting to the challenge remotely using:

```bash
nc challs.breachers.in 1343
```

Note: The flag present in the binary is just a **placeholder**. You’ll have to exploit the binary and get the **real flag from the remote server**.

# Instructions

This challenge, along with the bonus, will be a great introduction to binary exploitation — a field that often seems mysterious even to some moderately experienced people.

---

## 🔧 Setup Instructions

### 🔹 Install `pwninit`

[`pwninit`](https://github.com/io12/pwninit) helps you quickly set up boilerplate for pwning challenges.

#### On Linux (using `cargo`):

```bash
# Step 1: Install Rust (if not already installed)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Step 2: Install pwninit
cargo install pwninit

# Step 3: Install dependencies required by pwninit
sudo apt update
sudo apt install -y patchelf elfutils
```

Once installed, navigate to the folder containing the binary and run:

```bash
pwninit
```

This will generate a `solve.py` file.

In `solve.py`, there's a section where you can add your payload — use the [pwntools documentation](https://docs.pwntools.com/) To get started crafting your exploit. If you feel stuck a good place to begin would be decompiling the binary (figure out how).

Update the `conn()` function in `solve.py`:

```python
r = remote("addr", )  # Replace this line
```

with:

```python
r = remote("challs.breachers.in", 1343)
```

Now you can test your exploit locally by running:

```bash
python solve.py LOCAL
```

If it prints the test flag (like `test{flag}`), you're on the right track!  
Then, run:

```bash
python solve.py
```

to get the **real flag from the server**!

---

### 🔹 Install `pwntools` (Python Exploitation Library)

[`pwntools`](https://docs.pwntools.com/) is a powerful Python framework for binary exploitation.

To install it, simply run:

```bash
pip install pwntools
```

---

## 📤 Submission

Your submission should include:

- A brief **write-up** explaining how you exploited the binary.  
  If you couldn’t solve the challenge, explain what approaches you tried and where you got stuck.

- The **flag** you obtained from the remote server.

- Your final **`solve.py`** script used to exploit the binary.

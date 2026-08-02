# Packed transcripts

Phrase-level, grouped on silences ≥ 0.5s or speaker change.
Use `[start-end]` ranges to address cuts in the EDL.

## Teleprompter-2026-07-07_21-27-15  (duration: 1m 24.4s, 16 phrases)
  [002.90-005.84] S0 If a company can email you your password,
  [006.34-006.74] S0 run.
  [012.10-015.10] S0 If a company can email you your password, run.
  [015.68-018.64] S0 Let me show you what should actually happen when you sign up.
  [022.50-023.36] S0 The naive way:
  [023.96-027.06] S0 store your password in a table as plain text.
  [027.64-033.06] S0 One database leak and every account is wide open, and people reuse passwords everywhere.
  [033.68-038.20] S0 So we never store the password. We run it through a one-way hash function,
  [038.70-042.16] S0 easy to compute forwards, basically impossible to reverse.
  [042.96-051.12] S0 But hackers precompute rainbow tables of common passwords. So we add a salt, a random string mixed and hacked before hashing.
  [054.78-059.78] S0 So we add a salt, a random string mixed in before hashing unique per user.
  [060.42-064.66] S0 Now identical passwords get different hashes and precomputed tables are useless.
  [065.30-067.18] S0 Slow hashes like bcrypt.
  [072.56-076.52] S0 Slow hashes like bcrypt make brute force painful too.
  [077.80-082.50] S0 Good apps don't store your password. They store a riddle only you can answer.
  [083.06-087.34] S0 Next episode, we'll talk about how Netflix loads instantly

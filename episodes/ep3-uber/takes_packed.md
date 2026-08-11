# Packed transcripts

Phrase-level, grouped on silences ≥ 0.5s or speaker change.
Use `[start-end]` ranges to address cuts in the EDL.

## ep3  (duration: 2m 22.8s, 20 phrases)
  [007.54-008.78] S0 There are tens of...
  [018.10-024.98] S0 There are tens of thousands of drivers moving around your city. Uber finds the nearest, closest one...
  [037.06-041.12] S0 There are tens of thousands of drivers moving around your city.
  [041.98-045.28] S0 Uber finds the closest one in about two hundred milliseconds.
  [045.96-046.26] S0 How?
  [053.64-054.62] S0 Here's the naive way.
  [055.12-059.14] S0 We calculate the distance from you to every single driver and sort.
  [059.92-065.28] S0 That's fine for fifty drivers, but it's a disaster for fifty thousand updating every second.
  [066.16-074.46] S0 Instead, we index space itself. A quadtree splits the map into four squares, then splits the busy squares again, recursively.
  [076.10-083.64] S0 To find nearby drivers, we just walk down to your square and check its neighbors, ignoring the entire rest of the city.
  [084.32-092.06] S0 Geohashing does the same trick by turning coordinates into a short string, so nearby becomes a simple prefix match.
  [094.08-100.46] S0 Surge pricing and ETA come from ML models predicting demand on top of this geoindex.
  [106.72-112.48] S0 Surge pricing and ETA come from ML models predicting demand on top of this geoindex.
  [113.01-116.76] S0 The index makes the lookup fast enough to feed the model in real time.
  [118.56-121.60] S0 Next episode, we'll learn how don't search...
  [130.66-132.06] S0 Don't search the whole city.
  [132.72-133.70] S0 Search the right square.
  [134.50-138.64] S0 Next episode, we'll look into how sites know that you're not a robot.
  [142.72-145.63] S0 Don't search the whole city. Search the right square.
  [146.44-150.36] S0 Next episode, we'll learn how sites know that you're not a robot

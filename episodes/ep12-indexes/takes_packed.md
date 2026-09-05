# Packed transcripts

Phrase-level, grouped on silences ≥ 0.5s or speaker change.
Use `[start-end]` ranges to address cuts in the EDL.

## 12  (duration: 2m 13.7s, 20 phrases)
  [001.48-001.66] S0 In,
  [003.34-006.60] S0 in two milliseconds, Google searches a billion rows.
  [007.30-009.92] S0 That shouldn't be possible until you understand indexes.
  [016.50-023.58] S0 Here's the problem. Without an index, the database does a full scan. It reads every single row to find matches. At a billion rows,
  [024.14-024.68] S0 it's hopeless.
  [030.92-033.18] S0 An index is a separate sorted structure.
  [036.26-043.68] S0 An index is a separate sorted structure, usually a B-tree, that points to where data lives, like the index at the back of a book.
  [045.40-047.28] S0 Instead of rereading every page,
  [050.72-063.70] S0 instead of reading every page, the database does a few quick comparisons to jump straight to the rows that it needs. The trade-off is that indexes take space and slightly slow down writes because every insert must update the index too.
  [064.50-067.04] S0 So you index what you search, not everything.
  [068.74-071.30] S0 Vector databases extend this exact idea.
  [074.20-076.82] S0 Vector databases, vector databases.
  [078.72-086.44] S0 Vector databases extend this exact idea with specialized indexes like HNSW, so AI can do nearest neighbor search,
  [087.42-090.52] S0 nearest neighbor search over billions of embeddings just as fast.
  [098.12-107.94] S0 Vector databases extend this exact idea with specialized indexes like HNSW, so AI can do nearest neighbor search over billions of embeddings just as fast.
  [113.32-117.12] S0 An index is like a table of contents that your database reads first.
  [117.84-118.10] S0 Next,
  [118.88-119.64] S0 we'll talk about how--
  [120.32-122.96] S0 Next, we'll talk about why you get too many requests.
  [128.08-135.19] S0 An index is just a table of contents that your database reads first. Next episode, we'll talk about why you get too many requests.

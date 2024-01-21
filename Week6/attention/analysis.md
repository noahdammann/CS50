# Analysis

## Layer 1, Head 4

The attention pattern produced by this head, is a diagonal line, which indicates that the head's attention helps the AI understand the order of words in sentences.

Example Sentences:
- I ordered the most delicious [MASK] at my favourite restuarant.
    - I ordered the most delicious meal at my favourite restuarant.
    - I ordered the most delicious food at my favourite restuarant.
    - I ordered the most delicious breakfast at my favourite restuarant.
- I enjoyed going for a [MASK] last night.
    - I enjoyed going for a walk last night.
    - I enjoyed going for a run last night.
    - I enjoyed going for a swim last night.

## Layer 7, Head 12

The image depicts the words preceding the [MASK] token with higher attention scores than the any other words. This head's attention helps our AI to predict a word which will make sense given the context of the words immediately before it, ensuring the sentence 'flows' logically.

Example Sentences:
- I arrived by [MASK] in Germany today.
    - I arrived by train in Germany today.
    - I arrived by bus in Germany today.
    - I arrived by air in Germany today.
- I enjoyed travelling [MASK] in Italy.
    - I enjoyed travelling around in Italy.
    - I enjoyed travelling alone in Italy.
    - I enjoyed travelling extensively in Italy.

